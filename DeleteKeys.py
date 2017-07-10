import winreg

def DeleteKeys():
	winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r'DesktopBackground\shell\Cycler - NextBackground\command')
	winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r'DesktopBackground\shell\Cycler - PrevBackground\command')
	winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r'DesktopBackground\shell\Cycler - DeleteBackground\command')
	winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r'DesktopBackground\shell\Cycler - NextBackground')
	winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r'DesktopBackground\shell\Cycler - PrevBackground')
	winreg.DeleteKey(winreg.HKEY_CLASSES_ROOT, r'DesktopBackground\shell\Cycler - DeleteBackground')

if __name__ == '__main__':
	DeleteKeys()