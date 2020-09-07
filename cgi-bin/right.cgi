#!/bin/bash

gpio -g pwm 12 850

gpio -g pwm 13 850

gpio -g write 23 1

gpio -g write 19 1

echo "Status: 204 No Content" 
echo "content-type: text/plain"
echo ""
