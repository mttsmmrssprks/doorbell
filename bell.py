from gpiozero import Button
from signal import pause
import os

def say_hello():
    print("Hello!")
    #location of shell script to run doorbell sound
    os.system("/home/pi/doorbell/doorbell-sound.sh")


button = Button(23)

button.when_pressed = say_hello

pause()

