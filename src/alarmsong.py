"""
alarmsong, was created to play to song
"""
import pyaudio
import wave
import os


def run_music():
    """
    Prepare and treat the song
    :return: return then sound
    """
    # define stream chunk
    chunk = 1024

    # open a wav format music
    f = wave.open(
        rf"{os.getcwd()}{os.sep}songs{os.sep}musica.wav",
        "rb",
    )
    # instantiate PyAudio
    p = pyaudio.PyAudio()
    # open stream
    stream = p.open(
        format=p.get_format_from_width(f.getsampwidth()),
        channels=f.getnchannels(),
        rate=f.getframerate(),
        output=True,
    )
    # read data
    data = f.readframes(chunk)

    # play stream
    while data:
        stream.write(data)
        data = f.readframes(chunk)

    # stop stream
    stream.stop_stream()
    stream.close()

    # close PyAudio
    p.terminate()
