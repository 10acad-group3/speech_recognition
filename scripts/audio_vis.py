import numpy as np
import librosa
from log import get_logger
import IPython.display as ipd


class AudioVis():
  def __init__(self):
    self.logger = get_logger("FileHandler")

  def play_audio(self, samples, sample_rate):
    return ipd.Audio(samples, rate=sample_rate)

  def wav_plot(self, signal, sr=8000):
    return librosa.display.waveplot(signal, sr=sr)
