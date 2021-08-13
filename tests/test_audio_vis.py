from audio_vis import AudioVis
import os
import sys
import unittest
import numpy as np
import pandas as pd

sys.path.append(os.path.abspath(os.path.join('../scripts')))


class TestAudioVis(unittest.TestCase):

  def setUp(self) -> pd.DataFrame:
    self.audio_vis = AudioVis()


if __name__ == '__main__':
  unittest.main()
