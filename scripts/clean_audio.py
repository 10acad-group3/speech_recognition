import numpy as np
import librosa
from log import get_logger


class CleanAudio():
  """Clean audio data by removing dead spaces, ...
  """

  def __init__(self):
    self.logger = get_logger("CleanAudio")
