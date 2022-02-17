from telethon import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

import os, sys
import configparser
import csv
import time

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

def banner():
    print(f"""
{re}╔╦╗{cy}┌─┐┬  ┌─┐{re}╔═╗  ╔═╗{cy}┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
{re} ║ {cy}├┤ │  ├┤ {re}║ ╦  ╚═╗{cy}│  ├┬┘├─┤├─┘├┤ ├┬┘
{re} ╩ {cy}└─┘┴─┘└─┘{re}╚═╝  ╚═╝{cy}└─┘┴└─┴ ┴┴  └─┘┴└─

            version : 3.1
youtube.com/channel/UCnknCgg_3pVXS27ThLpw3xQ
        """)

if os.path.isfile('N93NT0T_log.txt'):
    with open('N93NT0T_log.txt', 'r') as r:
        data = r.readlines()
    api_id = data[0]
    api_hash = data[1]

else:
    api_id = input('Enter api_id: ')
    api_hash = input('Enter api_hash: ')
    with open('N93NT0T_log.txt', 'w') as a:
        a.write(api_id + '\n' + api_hash)

client = TelegramClient('N93NT0T', api_id, api_hash)

async def main():
os.system('clear')
banner()
chats = []
last_date = None
chunk_size = 2000
groups=[]
 
result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)
 
for chat in chats:
    try:
        if chat.megagroup== True:
            groups.append(chat)
    except:
        continue
 
print(gr+'[+] Choose a group to scrape members :'+re)
i=0
for g in groups:
    print(gr+'['+cy+str(i)+gr+']'+cy+' - '+ g.title)
    i+=1
 
print('')
g_index = input(gr+"[+] Enter a Number : "+re)
target_group=groups[int(g_index)]
 
print(gr+'[+] Fetching Members...')
time.sleep(1)
all_participants = []
all_participants = client.get_participants(target_group, aggressive=True)
 
print(gr+'[+] Saving In file...')
time.sleep(1)
with open(group.title + ".csv","w",encoding='UTF-8') as f:
    writer = csv.writer(f,delimiter=",",lineterminator="\n")
    writer.writerow(['username','user id', 'access hash','name','group', 'group id'])
    for user in all_participants:
        if user.username:
            username= user.username
        else:
            username= ""
        if user.first_name:
            first_name= user.first_name
        else:
            first_name= ""
        if user.last_name:
            last_name= user.last_name
        else:
            last_name= ""
        name= (first_name + ' ' + last_name).strip()
        writer.writerow([username,user.id,user.access_hash,name,target_group.title, target_group.id])      
print(gr+'[+] Members scraped successfully.')
