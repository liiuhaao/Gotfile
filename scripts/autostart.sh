#! /bin/bash

export GTK_IM_MODULE=fcitx5
export XMODIFIERS=@im=fcitx5
export QT_IM_MODULE=fcitx5
fcitx5 &

picom &
blueman-applet &
nm-applet &
slstatus &
dunst &
qv2ray &
flameshot &
unclutter -idle 1 -jitter 2 -root &


# Increase key repeat speed
# Disable screen power saving settings
# Disable screen blanking
C
xset r rate 250 30
xset -dpms
xset s off

# make CapsLock behave like Ctrl:
setxkbmap -option ctrl:nocaps
# make short-pressed Ctrl behave like Escape:
xcape -e 'Control_L=Escape'

feh --randomize --bg-fill ~/Pictures/Wallpapers/

brightnessctl set 20% &
