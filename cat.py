import RPi.GPIO as GPIO
import pygame
import datetime
import time
from gtts import gTTS
import picamera


now = datetime.datetime.now
pir_pin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_pin, GPIO.IN)


def catalarm():
    #start recording video, then sound the alarm!
    with picamera.PiCamera() as camera:
        vidname = "/home/pi/Desktop/Cat/video/"+str(now())+".h264"
        vidname = vidname.replace(':', '-')
        vidname = vidname.replace(' ','_')
        camera.start_recording(vidname)
        time.sleep(2)
        print("just started recording")
        #Playing sound:
        pygame.mixer.init()
        pygame.mixer.music.load("getOffCounter.mp3")
        print("playing sound")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        time.sleep(3)
        print("about to stop recording")
        camera.stop_recording()
        

def main_loop():
    try:
        while True:
            time.sleep(.5)
            if GPIO.input(pir_pin):
                catalarm()
            else:
                print("all safe and quiet")
    except KeyboardInterrupt:
        print("quitting...")
        GPIO.cleanup()

if __name__ == '__main__':
    main_loop()

