import sounddevice as sd
from scipy.io.wavfile import write,read
import numpy as np
from playsound import playsound
import multiprocessing



# Records audio for 10 seconds ---------------------------------------

fs = 44100
second = 10
print("Recording....")

record_voice = sd.rec(int(second*fs), samplerate=fs, channels=2)
sd.wait()
write("output.wav", fs, record_voice)

#---------------------------------------------------------------------



# Converting wav file to numpy array----------------------------------

def wav_to_array(wav_file):

    sam_rate, wav_to_array.signal = read(wav_file)
    duration = len(wav_to_array.signal)/sam_rate

    wav_to_array.time = np.arange(0, duration, 1/sam_rate)

#---------------------------------------------------------------------



# Saving recorded voice in wav form-----------------------------------

wav_to_array("output.wav")

#---------------------------------------------------------------------



# Creating opposite signals ------------------------------------------

rev_signal = wav_to_array.signal / -1
write("reversed.wav",fs,rev_signal)

#---------------------------------------------------------------------