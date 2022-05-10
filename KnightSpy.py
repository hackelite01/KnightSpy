#!/usr/bin/env python3  
import sys
import socket
import os
import time
from helplist import help
from modules import cms,Traceroute,reverseip,portscan,iplocation,httpheader,findsharedns,whois,dnslookup,robots,finder,cloudflare,wordpress



try:
    from colorama import Fore
except:
    os.system("clear")
    print(Fore.RED+"""\n Please Install colorama\n
    pip3 install colorama
        """)

#---------------------------

try:
    import requests
except:
    os.system("clear")
    print(Fore.RED+"""\n Please Install requests\n
    pip3 install requests
        """)

#---------------------------


try:
    import ipapi
except:
    os.system("clear")
    print(Fore.RED+"""\n Please Install ipapi\n
    pip3 install ipapi
        """)

#---------------------------


try:
    import builtwith
except:
    os.system("clear")
    print(Fore.RED+"""\n Please Install builtwith\n
    pip3 install builtwith
        """)

#---------------------------
while True:
    

    try:
        help.Banner()
        help.infolist1()
        number = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"KnightSpy"+Fore.BLUE+"~"+Fore.WHITE+"@hackelite01"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ").lower()
    except:
        print("\n God Lock :) ")
        sys.exit()
    if number == '4':

        print
        sys.exit()
            
        #####################
        #####################

    elif number == "3":
        help.infolist3()

        #####################

    elif number == "":
        print(Fore.RED+" [!]"+Fore.BLUE+" Please Enter Number :))))")
        input("")

#----------------------------------------------------------------------------------

#Information Gathering

    elif number == '1':
        try:
            help.Banner()
            help.infolist2()
            infor = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"KnightSpy"+Fore.BLUE+"~"+Fore.WHITE+"@hackelite01"+Fore.RED+"/"+Fore.CYAN+"Information Gathering"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ").lower()
    
            if infor == "1":
                help.Banner()
                cloudflare.__start__()

                #####################

            elif infor == "2":
                help.Banner()
                cms.__start__()

                #####################


            elif infor == "3":
                help.Banner()
                Traceroute.__start__()

                #####################


            elif infor == "4":
                help.Banner()
                reverseip.__start__()

                #####################

            elif infor == "5":
                help.Banner()
                portscan.__start__()

                #####################
            
            elif infor == "6":
                help.Banner()
                iplocation.__start__()

                #####################

            elif infor == "7":
                help.Banner()
                httpheader.__start__()

                #####################

            elif infor == "8":
                help.Banner()
                findsharedns.__start__()

                #####################

            elif infor == "9":
                help.Banner()
                whois.__start__()    

                #####################

            elif infor == "10":
                help.Banner()
                dnslookup.__start__()  
                #####################

            elif infor == "11":
                help.Banner()
                robots.__start__()
                #####################

            elif infor == "12":
                help.Banner()
                finder.__start__()

                #####################

            elif infor == "13":
                input(Fore.RED+" [!]"+Fore.GREEN+" Back To Menu (Press Enter...) ")

                #####################
            elif infor == "14":
                sys.exit()
                
                #####################
            elif infor == "":
                input(Fore.RED+" [!]"+Fore.GREEN+" Please Enter Number (Press Enter...) ")
        except KeyboardInterrupt:
            print("")
            sys.exit()

#------------------------------------------------------------------------------------------------
    elif number == "2":
        help.infolist4()
        try:
            numcms = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"KnightSpy"+Fore.BLUE+"~"+Fore.WHITE+"@hackelite01"+Fore.RED+"/"+Fore.CYAN+"CMS Detection"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ").lower()

        except:
            print("")
            sys.exit()
        if numcms == "1":
            help.infowp()
            try:
                wp = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"KnightSpy"+Fore.BLUE+"~"+Fore.WHITE+"@hackelite01"+Fore.RED+"/"+Fore.CYAN+"CMN"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"WordPress"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"$ ").lower()
            except:
                print("")
                sys.exit()
            if wp == "1":
                help.Banner()
                wordpress.wpplug()
            elif wp == "2":
                help.Banner()
                wordpress.user()
            elif wp == "3":
                try:
                    input(Fore.GREEN+" [*] Back To Menu (Press Enter...) ")
                except:
                    print("\n")
                    sys.exit()
        elif numcms == "2":
            help.Banner()
            print(Fore.RED+" [!]"+Fore.BLUE+" Coming Soon ! ")
            try:
                input(Fore.GREEN+" [*] Back To Menu (Press Enter...) ")
            except:
                print("")
                sys.exit()
        elif numcms == "3":
            help.Banner()
            print(Fore.RED+" [!]"+Fore.BLUE+" Coming Soon ! ")
            try:
                input(Fore.GREEN+" [*] Back To Menu (Press Enter...) ")
            except:
                print("")
                sys.exit()
        
        elif numcms == "4":
            try:
                input(Fore.GREEN+" [*] Back To Menu (Press Enter...) ")
            except:
                print("")
                sys.exit()
        elif numcms == "" or False:
            try:
                input(Fore.GREEN+" [*] Back To Menu (Press Enter...) ")
            except:
                print("")
                sys.exit()





