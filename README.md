This is a Rasbperry Pi-based doorbell.

It sets up a service to 'listen' for an input on GPIO pin 23. 

The circuit should be connected on GPIO 23 and ground on the RPi.

When the circuit is closed, it triggers a script that plays an audio file.

This is written for a Raspberry Pi Zero W with an Adafruit I2S DAC bonnet.

To add:
- incorporate links to components, libraries
- steps for setting up service
- steps for adding audio file
- add script to randomise audio files
- using omxplayer to play audio file
- links to lights
- integration with other tools within network for broader notifications


GPIO Zero documentation: https://gpiozero.readthedocs.io/en/stable/
Adafruit bonnet: https://learn.adafruit.com/adafruit-i2s-audio-bonnet-for-raspberry-pi
...and its setup: https://learn.adafruit.com/adafruit-i2s-audio-bonnet-for-raspberry-pi/raspberry-pi-usage
Omxplayer, using alsa: https://www.raspberrypi.org/documentation/raspbian/applications/omxplayer.md


