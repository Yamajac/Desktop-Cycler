import os, sys
import config
import glob
import json
import random

from subprocess import run
def readMonitorFile():
	try:
		with open('monitor', 'r') as f:
			monitor = int(f.read())
		if monitor == config.monitors:
			nextMonitor=1
		else:
			nextMonitor=monitor+1
		with open('monitor', 'w') as f:
			f.write(str(nextMonitor))
		return monitor
	except FileNotFoundError:
		with open('monitor', 'w') as f:
			f.write('1')
		return 1
		
def getWallpaperFromMonitor(monitor):
	skin_path = os.path.expanduser('~\documents\Rainmeter\Skins\Desktop-Cycler-RM\Monitor{0}\path.txt'.format(monitor))
	with open(skin_path, 'r') as f:
		wallpaper = f.read()
	return wallpaper
	
def changeWallpaper(monitor):
	skin_path = os.path.expanduser('~\documents\Rainmeter\Skins\Desktop-Cycler-RM\Monitor{0}\path.txt'.format(monitor))
	with open(skin_path, 'w') as f:
		f.write(random.choice(getWallpapers()))
	run([r"C:\Program Files\Rainmeter\Rainmeter.exe", r"!refresh", "Desktop-Cycler-RM\Monitor{0}".format(monitor)])
	return
	
def getWallpapers():
	return glob.glob(r"C:\Users\Lauren\Desktop\Media\wallpapers\*")
		
		
def deleteWallpaper(monitor):
	confirmation = input("Are you sure you want to delete the wallpaper? (y\\n)")
	if confirmation == 'y':
		wallpaper = getWallpaperFromMonitor(monitor)
		os.remove(wallpaper)
		changeWallpaper(monitor)
	else:
		return

if __name__ == '__main__':
	
	if len(sys.argv) > 1:
		if sys.argv[1] == 'delete':
			deleteWallpaper(sys.argv[2])
		else:
			changeWallpaper(sys.argv[1])
	else:
		monitor = str(readMonitorFile())
		changeWallpaper(monitor)
	
	