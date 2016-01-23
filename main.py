# Shortcut Name: Lock Screen
# Shortcut Key: Alt+L 

from threading import Timer

import subprocess

def lockScreen():
	subprocess.check_output(["gnome-screensaver-command", "-l"])

lockScreenTime = 2.5 * 60 * 60;

timer = Timer(lockScreenTime, lockScreen)
timer.start()