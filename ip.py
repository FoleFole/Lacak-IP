import sys
import requests
import urllib
import time
import random
import os
#Jangan Recode Asu_-
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

import os, sys, time, random
from sys import exit as keluar
from time import sleep as waktu
from random import random as acak
from random import choice as pilih
from sys import stdout
from os import system
os.system("clear")
I='\33[0;32m'
GL='\33[32;1m'
B='\33[0;36m'
BL='\33[36;1m'	
M='\33[31;1m'	
P='\33[37;1m'	
D='\33[30;1m'
Y='\33[33;1m'	
YL='\33[1;33m'
print
m = '\x1b[1;91m'
h = '\x1b[1;92m'
k = '\x1b[1;93m'
b = '\x1b[1;94m'
u = '\x1b[1;95m'
c = '\x1b[1;96m'
p = '\x1b[0m'
i = '\x1b[1;90m'
v = '\x1b[1;38;5;198m'
j = '\x1b[1;38;5;208m'
w = (m, v, j, p, k, b, u, c)
W = pilih(w)


def load():
    l = '# '
    a = 'W '
    g = 'E '
    i = 'L '
    n = 'C '
    P = 'O '
    r = 'M '
    h = '. '
    w = '. '
    u = '. '
    o = 'E '
    s = '  '
    e = 'T '
    S = 'O '
    for z in range(80):
        waktu(0.2)
        stdout.write('\x1b[1;95m\r             [\x1b[1;32m' + l[z % len(l)] + l[z % len(l)] +  a[z % len(a)] + g[z % len(g)] + i[z % len(i)] + n[z % len(n)] + P[z % len(P)] + r[z % len(r)] + o[z % len(o)] + s[z % len(s)] + e[z % len(e)] + S[z % len(S)] + s[z % len(s)] + w[z % len(w)] + h[z % len(h)] + u[z %len(u)] + w[z % len(w)] + '\x1b[1;95m]')
        stdout.flush()
        
load()


def load():
    l = 'T '
    a = 'O '
    g = 'L '
    i = 'S '
    n = '. '
    P = 'A '
    r = 'C '
    h = '. '
    w = '. '
    u = 'K '
    o = '. '
    s = '  '
    e = 'I '
    S = 'P '
    for z in range(80):
        waktu(0.2)
        stdout.write('\x1b[1;96m\r                    [\x1b[1;38;5;208m' + l[z % len(l)] +  a[z % len(a)] + a[z % len(a)] + g[z % len(g)] + i[z % len(i)] + s[z % len(s)] + g[z % len(g)] + P[z % len(P)] + r[z % len(r)] + P[z % len(P)] + u[z % len(u)] + s[z % len(s)] + e[z % len(e)] + S[z % len(S)] + o [z % len(o)] + h[z % len (h)] + w[z % len(w)] + n[z % len(n)] + '\x1b[1;96m]')
        stdout.flush()
        
load()

os.system("clear")
time.sleep(2)
print "\33[31;1m                 `-////::////-`                  "
print "\33[31;1m                 `+/.          ./+`                "
print "\33[31;1m                s.              .y            "
print "\33[31;1m               .so.            `so-   \33[33;1m{====LACAK  IP====}         "
print "\33[31;1m                y:o ...`  `...`+/y`   \33[35;1m{=================}        "    
print "\33[31;1m             `  .ssomNNs  oNNms+s-  . \33[33;1m{==Creator : Z03==}     "  
print "\33[31;1m            +/+- //-hds./:.odh--o .o:o\33[35;1m{=================}     "      
print "\33[31;1m           +o.-:/+h+:. +dho .:+yo/:-.oo   "
print "\33[31;1m           .-.-//:/sys-----.syy/://-.-.  "       
print "\33[31;1m                 `:yoo+/+o/+s+y:`       "        
print "\33[31;1m             /:://:/h-.-::-.-h/-//::/` "         
print "\33[31;1m             /o`://.`://:://:`.///`++`"          
print "\33[31;1m              +/:                :/+ "
print "\33[33;1m<=========================================>"
os.system("date")
def tulis(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#Buatnya Susah Kentod
        time.sleep(random.random() * 0.1)
#Tapi Boleh Pelajari Source Codenya :)
#Baik Kan Gw Cok :v
tulis('\33[36;1m\n\n(*)TOOLS : \33[32;1mLACAK IP\n\33[33;1m<=========================================>\n\33[36;1m(*)CREATOR : \33[32;1mZ03\n\33[33;1m<=========================================>\n\33[36;1m(*)GITHUB : \33[32;1mhttps://github.com/kingcracker\n\33[33;1m<=========================================>\n\33[36;1m(*)CONTACT : \33[32;1mthecyberr31@gmail.com')
time.sleep(1)
os.system('xdg-open https://github.com/kingcracker')
print "\33[33;1m<=========================================>"
time.sleep(2)
print "\33[36;1mTOOLS INI DIBUAT SENDIRI ANTI RECODE CLUB2"
time.sleep(1)
print "\33[33;1m<=========================================>"
print "\33[36;1mMasukan Ip Nya Cok!"
kc = raw_input("\x1b[1;38;5;208mInput IP @~> ")
print "\33[32;1mOtw Search,Sabar Ya Tod!!"
time.sleep(3)
true = True
url = "http://free.ipwhois.io/json/"+kc+"?lang=en"
json_open = urllib.urlopen(url)
data = {"ip":"8.8.8.8"}
r = requests.post(url = url, data = data)
file = eval(r.text)
print "\33[31;1mIp yang di lacak : %s"%(file['ip'])
time.sleep(2)
print "\33[31;1mIp Type: %s"%(file['type'])
time.sleep(3)
print "\33[36;1mKota : %s"%(file['city'])
time.sleep(2)
print "\33[36;1mNegara : %s"%(file['country'])
time.sleep(2)
print "\33[32;1mIbukota : %s"%(file['country_capital'])
time.sleep(2)
print "\33[32;1mKode Negara :%s"%(file['country_code'])
time.sleep(2)
print "\33[33;1mMata Uang : %s"%(file['currency'])
time.sleep(2)
print "\33[32;1mBenua : %s"%(file['continent'])
time.sleep(2)
print "\33[33;1mKode Telp : %s"%(file['country_phone'])
time.sleep(2)
print "\33[31;1mGMT : %s"%(file['timezone_gmt'])
time.sleep(2)
print "\33[36;1mGaris Lintang : %s"%(file['latitude'])
time.sleep(2)
print "\33[31;1mGaris Bujur : %s"%(file['longitude'])
print
def tulis(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#Buatnya Susah Kentod
        time.sleep(random.random() * 0.1)
#Tapi Boleh Pelajari Source Codenya :)
#Baik Kan Gw Cok :v
tulis('\33[1;33mTerima Kasih Udah Gunakan Tools Ini\nSemoga Kalian Suka :)\nSampai Jumpa Lagi Tod :v')
time.sleep(1)
