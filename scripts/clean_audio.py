import os
import sys
import librosa
import numpy as np
from log import get_logger


class CleanAudio():
  """Clean audio data by removing dead spaces, ...
  """

  def __init__(self):
    self.logger = get_logger("CleanAudio")

  def normalize_audio(self, signal):
    feats_mean = np.mean(signal, axis=0)
    feats_std = np.std(signal, axis=0)
    signal = (signal - feats_mean) / (feats_std + 1e-14)
    return signal

  def trim_audio(self, signal, trim_db=None):
    signal, index = librosa.effects.trim(signal, top_db=trim_db)
    return signal

  def split_audio(self, signal, clean_db=None):
    yt = librosa.effects.split(signal, top_db=clean_db)
    clean_signal = []
    for start_i, end_i in yt:
      clean_signal.append(signal[start_i: end_i])
    signal = np.concatenate(np.array(clean_signal), axis=0)
    return signal
