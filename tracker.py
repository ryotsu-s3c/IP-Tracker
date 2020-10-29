#!/bin/python3

import requests
import json
import argparse
import time
import sys, random

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'


def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """ 
     ___ ____    _____ ____      _    ____ _  _______ ____  
    |_ _|  _ \  |_   _|  _ \    / \  / ___| |/ / ____|  _ \ 
     | || |_) |   | | | |_) |  / _ \| |   | ' /|  _| | |_) |
     | ||  __/    | | |  _ <  / ___ \ |___| . \| |___|  _ < 
    |___|_|       |_| |_| \_\/_/   \_\____|_|\_\_____|_| \_\
                                                        

   
        
 [{}+{}] Insta :  https://instagram.com/m.tanishq.kushwaha/
 [{}+{}] Hacker Banno Chutiya nhi(TEAM VENOM)
 [{}+{}] IP TRACKER 
 {}=============================={}

			                  """
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
        
logo()


    
parser = argparse.ArgumentParser()

parser.add_argument("-i","--ipaddress", help="IP Address to Track")

args = parser.parse_args()

ip = args.ipaddress

url = "http://ip-api.com/json/"+str(ip)

response = requests.get(url)

data = json.loads(response.content)

#print(data)

print("\t[+] STATUS\t\t\t\t", data["status"])
print("\t[+] IP \t\t\t", data["query"])
print("\t[+] CITY \t\t\t", data["city"])
print("\t[+] ISP \t\t\t", data["isp"])
print("\t[+] COUNTRYCODE \t\t", data["countryCode"])
print("\t[+] LOC \t\t\t", data["country"])
print("\t[+] REG \t\t\t", data["regionName"])
print("\t[+] TIMEZone \t\t\t", data["timezone"])
print("\t[+] ZIP \t\t\t", data["zip"])
print("\t[+] LAT \t\t\t", data["lat"])
print("\t[+] LON \t\t\t", data["lon"])

#If you can undersamt what the fuck is written above then by misfortune your are also programmer
