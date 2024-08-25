from subprocess import getoutput
from time import sleep

print(".....Welcome to wifi-password-export.....\n")

output_ssid = getoutput("netsh wlan show profiles | findstr All")

export = "no"

split_data = []
for item in output_ssid.split(", "):
    parts = item.split(": ")
    for part in parts:
        split_data.extend(part.split("\n"))

def get_wifi_data():
	u = 0
	one_input = False
	for wifi_name in split_data:
		u += 1
		if u%2 == 0:
			output_password = getoutput(f'netsh wlan show profile "{wifi_name}" key="clear" | findstr Key').split(": ")
			output_secure = getoutput(f'netsh wlan show profile "{wifi_name}" | findstr Auth').split(": ")
			if(export == "e"):
				try:
					if(not(one_input)):
						one_input = True
						export_file = open(input("\nFile name: ") + ".txt", "a")
					export_file.write(f"{wifi_name} / {output_password[1]} / {output_secure[2]}\n")
				except:
					print("\nError!\n")	
			else:
				print(f"{wifi_name} / {output_password[1]} / {output_secure[2]}")
        
get_wifi_data()		

export = input("\nPress [e] key and [Enter] to export to *.txt file or press [Enter] to exit: ").lower()

if(export == "e"):
	get_wifi_data()

	print("\nExport finish...\nProgram ending...")
	sleep(2)
	exit()

