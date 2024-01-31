import sounddevice
from scipy.io.wavfile import write

seconds = 5
fps = 44100 # sampling rate


myrecord = sounddevice.rec(frames=seconds * fps, samplerate=fps, channels=1) #numpyarray
sounddevice.wait()

write('output.mp3', fps, myrecord)