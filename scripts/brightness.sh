#!/bin/bash

msgId="2"
if [ $1 == "up" ]; then
	brightnessctl set +1%
else
	brightnessctl set 1%-
fi

brightness="$(cat /sys/class/backlight/nvidia_0/brightness)"
dunstify -a "changeLight" \
	-r "$msgId" \
	-h int:value:"$brightness" \
	"Brightness: ${brightness}%"
