"""
alarmsong, was created to play to song
"""
import os
from pydub import AudioSegment
from pydub.playback import play

def run_music():
    """
    Prepare and treat the song
    :return: return then sound
    """
    song = AudioSegment.from_wav(f"{os.getcwd()}{os.sep}songs{os.sep}musica.wav")
    play(song)
