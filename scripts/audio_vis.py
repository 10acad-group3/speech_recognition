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
  """Visualisation of the audio file, spectogram, mfcc....
  """
  
  def __init__(self):
    self.logger = get_logger("FileHandler")

  def play_audio(self, samples, sr=22000):
    return ipd.Audio(samples, rate=sr)

  def wav_plot(self, signal, title, x_label, y_label, sr=22000):
    plt.figure(figsize=(25, 5))
    librosa.display.waveplot(signal, sr=sr)
    plt.title(title)
    plt.ylabel(x_label)
    plt.xlabel(y_label)
    plt.show()

  def get_wc(self, df, column, stop_words):
    plt.figure(figsize=(30, 20))
    wordcloud = WordCloud(font_path='../fonts/NotoSansEthiopic-Medium.ttf', max_words=5000,
                          background_color="salmon", width=3000, height=2000, colormap='Pastel1',
                          collocations=False, stopwords=stop_words).generate(' '.join(df[column].values))
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
