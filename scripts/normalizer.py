import logging

from pydub import AudioSegment
from pydub import effects

I = logging.getLogger("pydub.normalizer")
I.setLevel(logging.DEBUG)
I.addHandler(logging.StreamHandler())

class Normalizer():

    def __init__(self):
        self.audio_path = audio_path

    def normalize(self,audio_path):
        
