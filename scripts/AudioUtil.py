import librosa   #for audio processing
import IPython.display as ipd
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile #for audio processing
import warnings
warnings.filterwarnings("ignore")
class AudioUtil():
  # ----------------------------
  # Load an audio file. Return the audio as a array and rate
  # ----------------------------
  def opens(self, audio_file_loc, sr=22000):
    samples, sample_rate = librosa.load(audio_file_loc, sr=sr)
    return (samples, sample_rate)

  def play_audio(self, samples, sample_rate):
    return ipd.Audio(samples, rate=sample_rate)