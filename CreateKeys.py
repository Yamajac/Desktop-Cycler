import winreg
import os

def SetValue(key, sub_key, value):
	winreg.SetValue(key, sub_key, winreg.REG_SZ, value)
def SetValueEx(key, value_name, value):
	winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, value)
	
def CreateKeys():
	key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, r'DesktopBackground\shell')
	
	directory = 'python "' + os.getcwd() + '\\' 
	SetValue(key, r'Cycler - NextBackground\command', directory + 'NextBackground.py\"')
	SetValue(key, r'Cycler - PrevBackground\command', directory + 'PrevBackground.py\"')
	SetValue(key, r'Cycler - DeleteBackground\command', directory + 'DeleteBackground.py\"')
	
	with winreg.OpenKey(key, 'Cycler - NextBackground', 0, winreg.KEY_SET_VALUE) as sub_key:
		SetValueEx(sub_key, 'Position', 'Bottom')
	with winreg.OpenKey(key, 'Cycler - PrevBackground', 0, winreg.KEY_SET_VALUE) as sub_key:
		SetValueEx(sub_key, 'Position', 'Bottom')
	with winreg.OpenKey(key, 'Cycler - DeleteBackground', 0, winreg.KEY_SET_VALUE) as sub_key:
		SetValueEx(sub_key, 'Position', 'Bottom')
		
	key.Close()