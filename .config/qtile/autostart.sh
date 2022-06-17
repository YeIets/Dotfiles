#!/bin/zsh

#Resolucion de pantalla
xrandr --output Virtual1 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output Virtual2 --off --output Virtual3 --off --output Virtual4 --off --output Virtual5 --off --output Virtual6 --off --output Virtual7 --off --output Virtual8 --off

#Setear teclado español
setxkbmap latam &

#Setear Wallpaper
feh --bg-fill /home/yelets/wallpapers/luchitas.jpg

#Refresh Qtile config
qtile cmd-obj -o cmd -f reload_config

#Start picom
#picom --no-vsync
