from clean_audio import CleanAudio
import os
import sys
import unittest
import numpy as np
import pandas as pd
sys.path.append(os.path.abspath(os.path.join('../scripts')))


class TestCleanAudio(unittest.TestCase):

  def setUp(self):
    self.clean_audio = CleanAudio()

  def test_normalize_audio():
    pass

  def test_trim_audio():
    pass


if __name__ == '__main__':
  unittest.main()
