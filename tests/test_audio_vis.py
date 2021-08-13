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

  def test_plot_raw_audio():
    pass

  def test_plot_mfcc_feature():
    pass

  def test_plot_spectrogram_feature():
    pass

  def test_get_wc():
    pass


if __name__ == '__main__':
  unittest.main()
