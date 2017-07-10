import CreateKeys
import config

def RegistryHackConfirm():
	confirmation = input("Having registryhack turned on can cause damage to your computer. Are you sure you want to continue? (y/n) \n")
	if confirmation.lower() == 'y':
		print("Desktop Cycler will create the desktop context menus.")
		return True
	else:
		print("Desktop Cycler will not create the desktop context menus.")




if __name__ == '__main__':
	if config.registryhack and RegistryHackConfirm():
		
		CreateKeys.CreateKeys()
	
	while True:
		pass