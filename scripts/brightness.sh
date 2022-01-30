#!/bin/bash

msgId="2"
if [ $1 == "up" ]; then
	brightnessctl set +5%
else
	brightnessctl set 5%-
fi

brightness="$(cat /sys/class/backlight/nvidia_0/brightness)"
dunstify -a "changeLight" \
	-r "$msgId" \
	-h int:value:"$brightness" \
	"Brightness: ${brightness}%"
