#!/bin/bash

gpio -g pwm 12 850

gpio -g pwm 12 850

gpio -g write 24 1

gpio -g write 26 1

echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo ""
