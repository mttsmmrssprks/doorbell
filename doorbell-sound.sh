#!/bin/bash

echo "uid is ${UID}"
echo "playing doorbell sound"

omxplayer -o alsa /home/pi/doorbell/tones/ding-dong.mp3

#omxplayer -o alsa /home/pi/Music/m11stN-lon_aphex-twin.mp3

