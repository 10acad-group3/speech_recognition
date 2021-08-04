import json
import pickle
import pandas as pd
from config import Config
from log import get_logger
from tqdm import tqdm
import librosa
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
