import requests,json
import datetime
from config import *
from datetime import date
import calendar
from subprocess import call
from insta_functions import *
try: from colorama import init
except: exit('you must pip install colorama first')
from colorama import Fore, Back, Style
from tqdm import tqdm
import argparse
#from termcolor import colored
init(autoreset=True)
call('clear')
print('')
print(Style.BRIGHT+Fore.YELLOW + '''  _____ _   _  _____ _______             _____ ______ _______
 |_   _| \ | |/ ____|__   __|/\         / ____|  ____|__   __|
   | | |  \| | (___    | |  /  \ ______| |  __| |__     | |
   | | | . ` |\___ \   | | / /\ \______| | |_ |  __|    | |
  _| |_| |\  |____) |  | |/ ____ \     | |__| | |____   | |
 |_____|_| \_|_____/   |_/_/    \_\     \_____|______|  |_|

''')
print(Back.BLUE+'storage path set as /Users/jclabpro/Downloads/, to change edit config.py\n\n')
username = ''
while username == '':
    print(Fore.GREEN+'---'*15)
    username = input('| Instagram username? | : ')
    print(Fore.GREEN+'---'*15)
print ('working so far for {}'.format(username))

def main(username):
    userjson = get_user_data(username)
    report_table(userjson)
    print('\n\n\n')
    #print(json.dumps(userjson,sort_keys=True,indent=4))


main(username)

exit('thanks for playing')
