
import os
import time
import colorama
from colorama import Fore, Back, init

Percent = 0

init(convert=True)
for i in range(100):
    Percent += 1
    print(Fore.BLUE+ "Loading Epic Things....." + str(Percent) + "Percent has been completed")
    time.sleep(0.25) # edit the number for the delay between each second
os.system("start https://www.youtube.com/watch?v=xvFZjo5PgG0")
##time.sleep(4)
## added sleep because the msg.vbs launched before the rickroll loaded
## change number to how many seconds delay between load rickroll and vbs opens
## uncomment to enable
os.system("start msg.vbs")
time.sleep(10)
