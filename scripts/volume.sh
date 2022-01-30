#!/bin/bash
# changeVolume

msgId="3"

if [[ $1 == "up" ]]; then
	amixer set Master 5%+ umute
elif [[ $1 == "down" ]]; then
	amixer set Master 5%- umute
else
	amixer set Master toggle
fi

volume="$(amixer get Master | tail -1 | awk '{print $4}' | sed 's/[^0-9]*//g')"
mute="$(amixer get Master | tail -1 | awk '{print $6}' | sed 's/[^a-z]*//g')"
if [[ $volume == 0 || "$mute" == "off" ]]; then
	dunstify -a "changeVolume" \
		-r "$msgId" \
		"Volume muted"
else
	dunstify -a "changeVolume" \
		-r "$msgId" \
		-h int:value:"$volume" \
		"Volume: ${volume}%"
	canberra-gtk-play -i audio-volume-change -d "changeVolume"
fi
