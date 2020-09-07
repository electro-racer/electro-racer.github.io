#!/bin/bash

gpio -g pwm 12 1000

gpio -g pwm 13 1000

gpio -g write 23 1

gpio -g write 26 1

echo "Status: 204 No Content"
echo "content-type: text/plain"
echo ""
