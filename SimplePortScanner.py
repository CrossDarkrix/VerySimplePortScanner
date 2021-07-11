#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from colorama import init as InitingColor, Fore
import socket, sys, concurrent.futures

InitingColor()

def Logo():
    print(Fore.RED + """___         _   ___               
 | _ \___ _ _| |_/ __| __ __ _ _ _  
 |  _/ _ \ '_|  _\__ \/ _/ _` | ' \ 
 |_| \___/_|  \__|___/\__\__,_|_||_|

 Simple MultiThread TCP Port Scanner.
 Author: DarkRix.
 """ + Fore.RESET)

def scan_port(iPAdress, PortNum):
    global Scan_Result
    try:
        skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        skt.settimeout(0.245)
        Scan_Result = skt.connect_ex((iPAdress, PortNum))
        skt.close()
        if Scan_Result == 0:
            try:
                print(Fore.GREEN + '+ Open Port: {OPort}({ServiceName})'.format(OPort=PortNum, ServiceName=socket.getservbyport(PortNum)) + Fore.RESET)
            except:
                print(Fore.GREEN + '+ Open Port: {OPort}({ServiceName})'.format(OPort=PortNum, ServiceName='unknow service') + Fore.RESET)
        else:
            sys.stdout.write(Fore.RED + '- Scan Port: {CPort}\r'.format(CPort=PortNum+1) + Fore.RESET)
            sys.stdout.flush()
            
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
    StartScan = concurrent.futures.ThreadPoolExecutor(max_workers=None)
    for Port in range(FastPort, LastPort):
        StartScan.submit(scan_port, IPAdress, Port)
    StartScan.shutdown()
    print(Fore.YELLOW + '\n\nScanning Done.' + Fore.RESET)

if __name__== '__main__':
    main()
