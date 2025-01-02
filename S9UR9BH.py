import requests
import time
from bs4 import BeautifulSoup
import os
from os import system as shell
from rich import print
from rich import print_json
from rich import pretty
from rich.progress import track
from rich.markdown import Markdown
from rich.tree import Tree
from rich.panel import Panel
from rich.padding import Padding
pretty.install()

from datetime import datetime 
ct=str(datetime.now())
ct2=ct.split(" ")[0]
ct3=ct2.split("-")[1]
mon={"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June","07":"July","08":"August","09":"September","10":"October","11":"November","12":"December"}
month=mon[ct3]
datea=ct2.split("-")[2]


def lod(message):
    
    for i in track(range(300), description=f"[red][bold] {message}"):
        time.sleep(0.01)



def clear():
    shell("clear")
def lod(message):
    
    for i in track(range(300), description=f"[red][bold] {message}"):
        time.sleep(0.01)

lod("STARTING TOOL...")
lod("starting tools")
os.system("xdg-open https://facebook.com/groups/black.spammar.bd/")
os.system("clear")
logo = (f'''[bold red]
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┐
│    _____ _____                                                                                                         │
│   / ____|  __ \                                                                                                          │
│  | (___ | |__) ||                                                                                                         │
│   \___ \|  ___/                                                                                                         │
│   ____) | |                                                                                                                │
│  |_____/|_|                                                                                                              │
└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘
┌━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┐
│              INDIAN TEAM               │
└━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┘''')
class Main():
	print(logo)
	print(f' [1] RANDOM FRIEND ADD')
	
	choice = input( '[✙] CHOOSE : ')
	if choice == "1":
		print('')

os.system("clear")
print(logo)
cookie = input('Enter cookie: ')
if 'c_user=' in cookie:
    tg = input('Enter the delay time after each time (s): ')
    list = open('uid.txt', 'r')
    while True:
        uid = list.readline().strip()
        if uid == '':
            input('CHẠY XONG !!!!')
        headers1 = {
            'authority': 'mbasic.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': cookie,
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4685.46 Safari/537.36',
        }

        params1 = {
            'id': uid,
        }

        r1 = requests.get('https://mbasic.facebook.com/profile.php', params=params1, headers=headers1)
        soup = BeautifulSoup(r1.text, 'html.parser')
        for link in soup.find_all('a'):
            if 'profile_button' in str(link.get('href')):
                link1 = link.get('href')
        a1, b1 = link1.split('eav=')
        c1, d1 = b1.split('&paipv=0&ext=')
        e1, f1 = d1.split('&hash=')
        g1, h1 = f1.split('&')
        headers2 = {
            'authority': 'mbasic.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': cookie,
            'referer': f'https://mbasic.facebook.com/profile.php?id={uid}',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4685.46 Safari/537.36',
        }

        params2 = {
            'subject_id': uid,
            'is_timeline': '1',
            'how_found': 'profile_button',
            'ref_param': 'unknown',
            'referrer_id': '0',
            'eav': c1,
            'paipv': '0',
            'ext': e1,
            'hash': g1,
            'refid': '17',
        }
        try:
            r2 = requests.get('https://mbasic.facebook.com/a/friends/profile/add/', params=params2, headers=headers2)
            if r2.status_code == 200:
                print(f'Made friends with {uid}')
                print(f'Pause {tg}s')
                time.sleep(int(tg))
            else:
                print(f'Error making friends with {uid}')
                print(f'Pause {tg}s')
                time.sleep(int(tg))
        except:
            print('Unknown error...')
else:
    input('Please enter the correct Cookie format.!')
    
	
Main()
