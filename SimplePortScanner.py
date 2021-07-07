#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from colorama import init as InitingColor, Fore
import socket, sys
from threading import Thread as THd
InitingColor()

def Logo():
    print(Fore.RED + """___         _   ___               
 | _ \___ _ _| |_/ __| __ __ _ _ _  
 |  _/ _ \ '_|  _\__ \/ _/ _` | ' \ 
 |_| \___/_|  \__|___/\__\__,_|_||_|

 Simple Port Scanner.
  Author: DarkRix.
 """ + Fore.RESET)

def scan_port(iPAdress, PortNum):
    try:
        global Scan_Result
        skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        skt.settimeout(0.02)
        Scan_Result = skt.connect_ex((iPAdress, PortNum))
        skt.close()
    except socket.error:
        pass
    except OverflowError:
        pass
    except KeyboardInterrupt:
        sys.exit(0)
    except:
        pass

def main():
    Logo()
    host = input(Fore.RED + 'Target Host: ' + Fore.RESET)

    try:
        IPAdress = socket.gethostbyname(host)
    except:
        print('Error: Host IP not get....')
        sys.exit(0)

    print(Fore.RED + '\nSelected Host: {HOST}\n'.format(HOST=IPAdress) + Fore.RESET)

    try:
        FastPort = int(input(Fore.RED + 'Fast Port Numbar(Mini: 1): ' + Fore.RESET))
    except:
        print('Error: InputPort Numbar')
        sys.exit(0)
    try:
        LastPort = int(input(Fore.RED + 'Last Port Numbar(Max: 65535): ' + Fore.RESET))
    except:
        print('Error: InputPort Numbar')
        sys.exit(0)

    print(Fore.YELLOW + '\n\nScanning Port...\n' + Fore.RESET)

    for Port in range(FastPort, LastPort):
        THd(target=scan_port(IPAdress, Port)).start()
        if Scan_Result == 0:
            try:
                print(Fore.GREEN + '+ Open Port: {OPort}({ServiceName})'.format(OPort=Port, ServiceName=socket.getservbyport(Port)) + Fore.RESET)
            except:
                print(Fore.GREEN + '+ Open Port: {OPort}({ServiceName})'.format(OPort=Port, ServiceName='unknow service') + Fore.RESET)
        else:
            print(Fore.RED + '- Close Port: {CPort}'.format(CPort=Port) + Fore.RESET, end='\r', flush=True)

    print()
    print(Fore.YELLOW + '\nScanning Done.' + Fore.RESET)

if __name__== '__main__':
    main()

