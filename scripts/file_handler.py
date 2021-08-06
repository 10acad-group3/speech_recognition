import json
import pickle
import pandas as pd
from config import Config
from numpy.lib.stride_tricks import as_strided
from mpl_toolkits.axes_grid1 import make_axes_locatable
from log import get_logger
from tqdm import tqdm
import librosa
import numpy as np
import os


class FileHandler():
    """Read audio, audio transcription, Save cleaned Audio and transcriptions
    """

    def __init__(self):
        self.logger = get_logger("FileHandler")

    def read_text(self, text_path):
        text = []
        with open(text_path) as fp:
          line = fp.readline()
          while line:
            # TODO: fix spaces in in amharic text
            text.append(line)
            line = fp.readline()
        return text

    def read_data(self, PATH_TRAIN_TEXT, PATH_TEST_TEXT, train_labels, test_labels):
        train_text = self.read_text(PATH_TRAIN_TEXT)
        test_text = self.read_text(PATH_TEST_TEXT)

        train_text.extend(test_text)
        train_labels.extend(test_labels)

        new_text = []
        new_labels = []
        for i in train_text:
            result = i.split()

            if result[0] in train_labels:  # if the audio file exists
                new_text.append(' '.join([elem for elem in result[1:]]))
                new_labels.append(result[0])

        return new_text, new_labels

    def read_audio_signal(self, audio_file_loc, sr=22000):
        samples, sample_rate = librosa.load(audio_file_loc, sr=sr)
        return (samples, sample_rate)

    def spectrogram(self, samples, fft_length=256, sample_rate=2, hop_length=128):
        """
        Compute the spectrogram for a real signal.
        The parameters follow the naming convention of
        matplotlib.mlab.specgram

        Args:
            samples (1D array): input audio signal
            fft_length (int): number of elements in fft window
            sample_rate (scalar): sample rate
            hop_length (int): hop length (relative offset between neighboring
                fft windows).

        Returns:
            x (2D array): spectrogram [frequency x time]
            freq (1D array): frequency of each row in x

        Note:
            This is a truncating computation e.g. if fft_length=10,
            hop_length=5 and the signal has 23 elements, then the
            last 3 elements will be truncated.
        """
        assert not np.iscomplexobj(samples), "Must not pass in complex numbers"

        window = np.hanning(fft_length)[:, None]
        window_norm = np.sum(window**2)

        # The scaling below follows the convention of
        # matplotlib.mlab.specgram which is the same as
        # matlabs specgram.
        scale = window_norm * sample_rate

        trunc = (len(samples) - fft_length) % hop_length
        x = samples[:len(samples) - trunc]

        # "stride trick" reshape to include overlap
        nshape = (fft_length, (len(x) - fft_length) // hop_length + 1)
        nstrides = (x.strides[0], x.strides[0] * hop_length)
        x = as_strided(x, shape=nshape, strides=nstrides)

        # window stride sanity check
        assert np.all(x[:, 1] == samples[hop_length:(hop_length + fft_length)])

        # broadcast window, compute fft over columns and square mod
        x = np.fft.rfft(x * window, axis=0)
        x = np.absolute(x)**2

        # scale, 2.0 for everything except dc and fft_length/2
        x[1:-1, :] *= (2.0 / scale)
        x[(0, -1), :] /= scale

        freqs = float(sample_rate) / fft_length * np.arange(x.shape[0])

        return x, freqs

    def plot_spectrogram_feature(self, vis_spectrogram_feature):
        # plot the normalized spectrogram
        fig = plt.figure(figsize=(12,5))
        ax = fig.add_subplot(111)
        im = ax.imshow(vis_spectrogram_feature, cmap=plt.cm.jet, aspect='auto')
        plt.title('Spectrogram')
        plt.ylabel('Time')
        plt.xlabel('Frequency')
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=0.05)
        plt.colorbar(im, cax=cax)
        plt.show()