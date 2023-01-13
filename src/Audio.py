import numpy
import pyaudio


CHUNK = 32
RATE = 44100

class Audio:
    def __init__(self) -> None:
        
        self.audioContext = pyaudio.PyAudio()
        
        self.stream = self.audioContext.open(format=pyaudio.paInt16, channels=2, rate=RATE, input=True, frames_per_buffer=CHUNK)
        self.player = self.audioContext.open(format=pyaudio.paInt16, channels=2, rate=RATE, output=True, frames_per_buffer=CHUNK)

    def __del__(self) -> None:
        print("hi")
        self.stream.stop_stream()
        self.stream.close()
        self.audioContext.terminate()
    
    def getAudio(self, len: int) -> None:
        for i in range(int(len*RATE/CHUNK)):
            data = numpy.fromstring(self.stream.read(CHUNK), dtype=numpy.int16)
            self.player.write(data, CHUNK)
            