import sys
import requests
from colorama import Fore

def __start__():
        try:
                
                print(Fore.RED+" [!] Plase Enter Domain")
                inp = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"KnightSpy"+Fore.BLUE+"~"+Fore.WHITE+"@hackelite01"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"TraceRoute"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ")
                result = requests.get('https://api.hackertarget.com/mtr/?q=' + inp).text
                print(result)
                try:
                        input(Fore.RED+" [!] "+Fore.GREEN+"Back To Menu (Press Enter...) ")
                except:
                        print("")
                        sys.exit()  
        except:
                print("\nExit :)")
                
        
