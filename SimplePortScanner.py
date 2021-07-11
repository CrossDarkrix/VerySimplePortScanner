#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from colorama import init as InitingColor, Fore
import socket, sys
from threading import Thread

InitingColor()

class ScanThread(Thread):
    def __init__(self, iP, FaPort, LaPort):
        Thread.__init__(self)
        self.iP = iP
        self.FaPort = FaPort
        self.LaPort = LaPort

    def run(self):
        scan_port(self.iP, self.FaPort, self.LaPort)

def Logo():
    print(Fore.RED + """___         _   ___               
 | _ \___ _ _| |_/ __| __ __ _ _ _  
 |  _/ _ \ '_|  _\__ \/ _/ _` | ' \ 
 |_| \___/_|  \__|___/\__\__,_|_||_|

 Simple TCP Port Scanner.
 Author: DarkRix.
 """ + Fore.RESET)

def scan_port(iPAdress, FPort, LPort):
    global Scan_Result
    for PortNum in range(FPort, LPort):
        try:
            skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            skt.settimeout(0.02)
            Scan_Result = skt.connect_ex((iPAdress, PortNum))
            skt.close()
            if Scan_Result == 0:
                try:
                    print(Fore.GREEN + '+ Open Port: {OPort}({ServiceName})'.format(OPort=PortNum, ServiceName=socket.getservbyport(PortNum)) + Fore.RESET)
                except:
                    print(Fore.GREEN + '+ Open Port: {OPort}({ServiceName})'.format(OPort=PortNum, ServiceName='unknow service') + Fore.RESET)
            else:
                 print(Fore.RED + '- Scan Port: {CPort}'.format(CPort=PortNum+1) + Fore.RESET, end='\r', flush=True)
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
    try:
        StartScan = ScanThread(IPAdress, FastPort, LastPort)
        StartScan.start()
    except KeyboardInterrupt:
        sys.exit(0)
    except:
        sys.exit(0)
    StartScan.join()
    print(Fore.YELLOW + '\n\nScanning Done.' + Fore.RESET)

if __name__== '__main__':
    main()

