import numpy as np
import librosa
from log import get_logger
import IPython.display as ipd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
from IPython.display import Image
from mpl_toolkits.axes_grid1 import make_axes_locatable
import librosa.display


class AudioVis():
  def __init__(self):
    self.logger = get_logger("FileHandler")

  def play_audio(self, samples, sr=22000):
    return ipd.Audio(samples, rate=sr)

  def wav_plot(self, signal, sr=22000):
    plt.figure(figsize=(24, 4))
    librosa.display.waveplot(signal, sr=sr)
    plt.show()

  def get_wc(self, df, stop_words):
    plt.figure(figsize=(30, 20))
    wordcloud = WordCloud(font_path='../fonts/NotoSansEthiopic-Medium.ttf', max_words=5000,
                          background_color="salmon", width=3000, height=2000, colormap='Pastel1',
                          collocations=False, stopwords=stop_words).generate(' '.join(df.text.values))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.title('Most Frequent Words In Amharic Audio Transcription', fontsize=16)
    plt.show()

  def plot_raw_audio(vis_raw_audio, title='Audio Signal', size=(12, 3)):
    fig = plt.figure(figsize=size)
    ax = fig.add_subplot(111)
    steps = len(vis_raw_audio)
    ax.plot(np.linspace(1, steps, steps), vis_raw_audio)
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.show()

  def plot_mfcc_feature(self, vis_mfcc_feature):
    # plot the MFCC feature
    fig = plt.figure(figsize=(12, 5))
    ax = fig.add_subplot(111)
    im = ax.imshow(vis_mfcc_feature, cmap=plt.cm.jet, aspect='auto')
    plt.title('Normalized MFCC')
    plt.ylabel('Time')
    plt.xlabel('MFCC Coefficient')
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    plt.colorbar(im, cax=cax)
    ax.set_xticks(np.arange(0, 13, 2), minor=False)
    plt.show()

  def plot_spectrogram_feature(self, vis_spectrogram_feature):
    # plot the normalized spectrogram
    fig = plt.figure(figsize=(12, 5))
    ax = fig.add_subplot(111)
    im = ax.imshow(vis_spectrogram_feature, cmap=plt.cm.jet, aspect='auto')
    plt.title('Normalized Spectrogram')
    plt.ylabel('Time')
    plt.xlabel('Frequency')
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    plt.colorbar(im, cax=cax)
    plt.show()

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


  def spectrogram_from_file(self, filename, step=10, window=20, max_freq=None,
                            eps=1e-14):
      """ Calculate the log of linear spectrogram from FFT energy
      Params:
          filename (str): Path to the audio file
          step (int): Step size in milliseconds between windows
          window (int): FFT window size in milliseconds
          max_freq (int): Only FFT bins corresponding to frequencies between
              [0, max_freq] are returned
          eps (float): Small value to ensure numerical stability (for ln(x))
      """
      with soundfile.SoundFile(filename) as sound_file:
          audio = sound_file.read(dtype='float32')
          sample_rate = sound_file.samplerate
          if audio.ndim >= 2:
              audio = np.mean(audio, 1)
          if max_freq is None:
              max_freq = sample_rate / 2
          if max_freq > sample_rate / 2:
              raise ValueError("max_freq must not be greater than half of "
                              " sample rate")
          if step > window:
              raise ValueError("step size must not be greater than window size")
          hop_length = int(0.001 * step * sample_rate)
          fft_length = int(0.001 * window * sample_rate)
          pxx, freqs = spectrogram(
              audio, fft_length=fft_length, sample_rate=sample_rate,
              hop_length=hop_length)
          ind = np.where(freqs <= max_freq)[0][-1] + 1
      return np.transpose(np.log(pxx[:ind, :] + eps))
