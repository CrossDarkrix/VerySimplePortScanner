#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from colorama import init as InitingColor, Fore
import socket, sys, concurrent.futures
from os import cpu_count

InitingColor()
MaxWorker = int(cpu_count() * 15)

def Logo():
    print(Fore.RED + """___         _   ___               
 | _ \___ _ _| |_/ __| __ __ _ _ _  
 |  _/ _ \ '_|  _\__ \/ _/ _` | ' \ 
 |_| \___/_|  \__|___/\__\__,_|_||_|

 Simple TCP Port Scanner.
 Author: DarkRix.
 """ + Fore.RESET)

def scan_port(iPAdress, PortNum):
    OpenPort = None
    ClosedPort = None
    try:
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
    if Scan_Result == 0:
        try:
            OpenPort = '+ Open Port: {OPort}({ServiceName})'.format(OPort=PortNum, ServiceName=socket.getservbyport(PortNum))
        except:
            OpenPort = '+ Open Port: {OPort}({ServiceName})'.format(OPort=PortNum, ServiceName='unknow service')
    else:
        ClosedPort = '- Scan Port: {CPort}'.format(CPort=PortNum+1)
    return OpenPort, ClosedPort


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
        FastPort = int(input(Fore.RED + 'Fast Port Numbar(Mini: 0): ' + Fore.RESET))
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
        Scan_Results = concurrent.futures.Future.result(concurrent.futures.ThreadPoolExecutor(max_workers=MaxWorker).submit(scan_port, IPAdress, Port))
        try:
            print(Fore.GREEN + Scan_Results[0] + Fore.RESET)
        except:
            print(Fore.RED + Scan_Results[1] + Fore.RESET, end='\r', flush=True)

    print(Fore.YELLOW + '\n\nScanning Done.' + Fore.RESET)

if __name__== '__main__':
    main()

