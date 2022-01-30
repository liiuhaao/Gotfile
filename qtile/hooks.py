import os
import subprocess

from libqtile import hook

home = os.path.expanduser('~')


# Run the autostart.sh script on startup
@hook.subscribe.startup
def startup():
    subprocess.call(home + "/.local/bin/autostart.sh")
