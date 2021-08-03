import json
import pickle
import pandas as pd
from config import Config
from log import get_logger


class FileHandler():
  """Read audio, audio transcription, Save cleaned Audio and transcriptions
  """

  def __init__(self):
    self.logger = get_logger("FileHandler")
