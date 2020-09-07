#!/bin/bash

gpio -g mode 18 ALT5

sudo aplay /home/pi/Desktop/Pranad_Folder/42_electronics/robot/hello.wav

gpio -g mode 18 IN

gpio -g mode 12 PWM
gpio -g mode 13 PWM

echo "Status: 204 No Content"
echo "content-type: text/plain"
echo ""
