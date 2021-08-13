from file_handler import FileHandler
import os
import sys
import unittest
import numpy as np
import pandas as pd
sys.path.append(os.path.abspath(os.path.join('../scripts')))


class TestFileHandler(unittest.TestCase):

  def setUp(self):
    self.file_handler = FileHandler()

  def test_read_text():
    pass

  def test_read_data():
    pass

  def test_read_audio_signal():
    pass

  def test_save_audio_as_numpy():
    pass


if __name__ == '__main__':
  unittest.main()
