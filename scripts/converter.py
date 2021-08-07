import logging

from pydub import AudioSegment

I = logging.getLogger("pydub.converter")
I.setLevel(logging.DEBUG)
I.addHandler(logging.StreamHandler())

class Converter():

    def __init__(self):
        self.audio_path = audio_path

    def mono_to_sterio(self,audio_path):
        audio = AudioSegment.from_wav(audio_path)
        
        #mono has 1 channel,sterio has 2 or more
        if audio.channels == 2:
            pass
        else:
            audio = audio.set_channels(2)
        return audio
            
