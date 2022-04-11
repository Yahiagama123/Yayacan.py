import colorama
from colorama import Fore
from ast import Pass
import socket
from IPy import IP

def scan (targets):
    convert_ip=check_ip(targets)
    print ('\n'+' '+'[-_0 scan trget >'+' '+str(targets)+' ')
    for port in (22.23,25,80,443,161,8080):
        scan_port(convert_ip,port)


def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):
    return s.recv(1024)

def scan_port(ipadress,port):
    try:
        sock=socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipadress,port))
        try:
            banner=get_banner(sock)
            print ('[+] port' +' '+str(port) + Fore.GREEN +' Is open ' +Fore.RED + str(banner.decode().strip('\n')))
        except:
            print (Fore.WHITE +'[+] port' +' '+Fore.GREEN +str(port) )
    except:
       Pass



Targets=input("[+] Enter the Target/s  ")
if ',' in Targets:
    for ip_add in Targets.split(','):
        scan (ip_add.strip(  ))

else:
    scan (Targets)
        

