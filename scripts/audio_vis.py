import numpy as np
import librosa
from log import get_logger
import IPython.display as ipd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
from IPython.display import Image


class AudioVis():
  def __init__(self):
    self.logger = get_logger("FileHandler")

  def play_audio(self, samples, sample_rate):
    return ipd.Audio(samples, rate=sample_rate)

  def wav_plot(self, signal, sr=8000):
    return librosa.display.waveplot(signal, sr=sr)

  def get_wc(self, df, stop_words):
    plt.figure(figsize=(30, 20))
    wordcloud = WordCloud(font_path='../fonts/NotoSansEthiopic-Medium.ttf', max_words=5000,
                          background_color="salmon", width=3000, height=2000, colormap='Pastel1', 
                          collocations=False, stopwords=stop_words).generate(' '.join(df.text.values))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.title('Most Frequent Words In Amharic Audio Transcription', fontsize=16)
    plt.show()
