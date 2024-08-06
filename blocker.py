import subprocess
from os import system
from sys import exit
from  platform import system as sy
def clear_screen():
    if infosystem() == 'Windows':
        comand('cls')
    elif infosystem() in ['Linux', 'Darwin']: 
        comand('clear')
clear_screen()
if sy() == "Windows":
    exit()
system('clear')
print('''
1.Block
2.Unblock
''')
x1=int(input('Enter >> '))
if x1 == 1 :
    print('''
    1.mci
    2.shatel
    3.mtn
    4.rightel
    5.parsonline
    6.afranet
    7.asiatech
    8.ict
    ''')
    x=int(input("Enter >> "))
    if x == 1:
        IP_LIST='isp/mci.ipv4'
    elif x==2:
        IP_LIST='isp/shatel.ipv4'
    elif x==3:
        IP_LIST='isp/irancell.ipv4'
    elif x==4:
        IP_LIST='isp/rightel.ipv4'
    elif x==5:
        IP_LIST='isp/parsonline.ipv4'
    elif x==6:
        IP_LIST='isp/afranet.ipv4'
    elif x==7:
        IP_LIST='isp/asiatech.ipv4'
    elif x==8:
        IP_LIST='isp/ict.ipv4'

    def block_ip_range(ip_range):
        try:
            subprocess.run(["sudo", "iptables", "-A", "INPUT", "-p", "tcp", "-s", ip_range, "-j", "DROP"], check=True)
            subprocess.run(["sudo", "iptables", "-A", "OUTPUT", "-p", "tcp", "-d", ip_range, "-j", "DROP"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to block IP range {ip_range}: {e}")
    def main():
        with open(IP_LIST, "r") as file:
            for line in file:
                ip_range = line.strip()
                if ip_range:
                    block_ip_range(ip_range)

    if __name__ == "__main__":
        print('Wait ....')
        main()
        print('ISP Blocked')
if x1 == 2 :
        print('''
        1.mci
        2.shatel
        3.mtn
        4.rightel
        5.parsonline
        6.afranet
        7.asiatech
        8.ict
        ''')
        x=int(input("Enter >> "))
        if x == 1:
            IP_LIST='isp/mci.ipv4'
        elif x==2:
            IP_LIST='isp/shatel.ipv4'
        elif x==3:
            IP_LIST='isp/irancell.ipv4'
        elif x==4:
            IP_LIST='isp/rightel.ipv4'
        elif x==5:
            IP_LIST='isp/parsonline.ipv4'
        elif x==6:
            IP_LIST='isp/afranet.ipv4'
        elif x==7:
            IP_LIST='isp/asiatech.ipv4'
        elif x==8:
            IP_LIST='isp/ict.ipv4'
        def block_ip_range(ip_range):
            try:
                subprocess.run(["sudo", "iptables", "-D", "INPUT", "-p", "tcp", "-s", ip_range, "-j", "DROP"], check=True)
                subprocess.run(["sudo", "iptables", "-D", "OUTPUT", "-p", "tcp", "-d", ip_range, "-j", "DROP"], check=True)
            except :
                print(f"Failed to block IP range {ip_range}")
        def main():
            with open(IP_LIST, "r") as file:
                for line in file:
                    ip_range = line.strip()
                    if ip_range:
                        block_ip_range(ip_range)
        if __name__ == "__main__":
            print('Wait ....')
            main()
            print('ISP Unblock')