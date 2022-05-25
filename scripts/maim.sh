#! /bin/bash
if [ $1 == "save" ]; then
    maim -s | tee ~/Pictures/$(date +%s).png | xclip -selection clipboard -t image/png
else
    maim -s | xclip -selection clipboard -t image/png
fi
