import json
import pickle
import pandas as pd
from config import Config
from log import get_logger
from tqdm import tqdm
import librosa
import os
import numpy as np
from clean_audio import CleanAudio


PATH_TRAIN_WAV = "../data/AMHARIC/train/wav/"
PATH_TEST_WAV = "../data/AMHARIC/test/wav/"


class FileHandler():
  """Read audio, audio transcription, Save cleaned Audio and transcriptions
  """

  def __init__(self):
    self.logger = get_logger("FileHandler")
    self.clean_audio = CleanAudio()

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

  def save_audio_as_numpy(self, df, sr):
    allFiles = []
    for index, row in df.iterrows():
      if(row["category"] == "Train"):
        allFiles.append(PATH_TRAIN_WAV + row["key"] + ".wav")
      else:
        allFiles.append(PATH_TEST_WAV + row["key"] + ".wav")

    count = 0
    for file in tqdm(allFiles):
      try:
        wav, rate = librosa.load(file, sr=None)
        y = librosa.resample(wav, rate, sr)

        y = self.clean_audio.normalize_audio(y)
        y = self.clean_audio.split_audio(y, 30)
        np.save(file.strip('.wav') + '.npy', y)
        os.remove(file)
        if((count % 1000) == 0):
          print(f"Done: {(count/len(allFiles)*100):.2f}%")
        count += 1

      except EOFError as e:
        pass
