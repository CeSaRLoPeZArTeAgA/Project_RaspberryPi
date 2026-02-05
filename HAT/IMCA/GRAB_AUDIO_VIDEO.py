import time
import wave
import threading
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
import pyaudio

#configuracion de la grabacion
FORMAT=pyaudio.paInt16
CHANNELS=1
RATE=44100
CHUNK=1024
AUDIO_FILENAME='audio.wav'


def grabar_audio():
    audio=pyaudio.Pyaudio()
    strem = audio.open(format=FORMAT,channels=CHANNELS,
                       rate=RATE,input=True,
                       frame_per_buffer=CHUNK)
    frame=[]
    print("Grabando audio...")
    for _ in range(0,int(RATE/CHUNK*DURACION)):
        data=stream.read(CHUNK)
        frames.append(data)
    print("Grabacion de audio finalizada")
    stream.stop_stream()
    stream.close()
    audio.terminate()
    with wave.open(AUDIO_FILENAME,'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
    
DURACION=20
VIDEO_FILENAME='video.h264'

picam2=Picamera2()

video_config=picam2.create_video_configuration()
picam2.configure(video_config)

encoder=H264Encoder(bitrate=100000000)

picam2.start_recording(encoder,'video.h264')
print("Grabando video...")

time.sleep(10)

picam2.stop_recording()
print("Grabacion finalizada......")

#combinacion de audio y video en un archivo mp4
import ffmpeg