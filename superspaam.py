import threading, requests, os, random
from itertools import cycle
from pystyle import Write, Colors, Colorate
from time import strftime, gmtime
from datetime import datetime
import sys
from pystyle import Colors, Colorate
import time

session = requests.Session()

#colors
#a = fg('#a005ed')
#b = attr('reset')
#c = fg('#00D7D3')  

main = """


┌┬┐┌─┐┬─┐┌┬┐┬┌┐┌┌─┐┬    ┌┬┐┌─┐┌─┐┬  ┌─┐
 │ ├┤ ├┬┘│││││││├─┤│     │ │ ││ ││  └─┐
 ┴ └─┘┴└─┴ ┴┴┘└┘┴ ┴┴─┘   ┴ └─┘└─┘┴─┘└─┘

  ░                    ░                               ░                 ░                               

      """
print(Colorate.Horizontal(Colors.yellow_to_red, main, 1))
#webhook link
#web=input(f"{a}[{c}ECSTACY{b}{a}]{b} {c}Webook{a}: ")


web = input(Colorate.Horizontal(Colors.yellow_to_red, "webhook url? : ", 1))

#webhook username
rando=[".gg/xfhvUvmtH"," join .gg/xfhvUvmtH","lol","spammed","notfound.0","$","idk","webhook","thats ez","rip"]

#webhook message
#spam=input(f"{a}[{c}ECSTACY{b}{a}]{b} {c}Message{a}: ")
spam = input(Colorate.Horizontal(Colors.yellow_to_red, "spam message?: ", 1))
#webhook avatars
avatars = cycle(["https://cdn.discordapp.com/avatars/1045007021616922697/a_e041e034733cec726125fdf0f764bff0.gif?size=4096"])

#proxies


def ehook(webhook):
# while True:
                now = datetime.now()
                s = now.strftime("%S")
                x = f'{strftime(f"[%H:%M:{s}]", gmtime())} Sent Webhook {spam}'
                yes = f'{strftime(f"[%H:%M:{s}]", gmtime())}'
                
                
                einfo={
                    'username': random.choice(rando),
                    'content': spam,
                    "avatar_url": next(avatars)
                }
                r = session.post(webhook, json=einfo)
                if "retry_after" in r.text:
                    print(f"{yes} ratelimited sleeping for {r.json()['retry_after']} secs.")
                elif r.status_code == 204:
                    print(x)
                else:
                    pass


if __name__ == "__main__":
    os.system('cls')
    logo = """


┌┬┐┌─┐┬─┐┌┬┐┬┌┐┌┌─┐┬    ┌┬┐┌─┐┌─┐┬  ┌─┐
 │ ├┤ ├┬┘│││││││├─┤│     │ │ ││ ││  └─┐
 ┴ └─┘┴└─┴ ┴┴┘└┘┴ ┴┴─┘   ┴ └─┘└─┘┴─┘└─┘
tool is starting
      """
    print(Colorate.Horizontal(Colors.yellow_to_red, logo, 1))
    while True:
     for i in range(35):
      threading.Thread(target=ehook, args=(web,)).start()
