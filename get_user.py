# What: Gets an insta users profile info and posts as necessary into a html and pdf file
# How: setup config.py with the output path you want

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
import sys
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
# tell the user what the current output path is set to and where to change it
print(Back.BLUE+'storage path set as {}, to change edit config.py\n\n'.format(storage_path))
username = ''
if len(sys.argv) > 1:
  username = sys.argv[1]
while username == '':
    # lets do a nice green input bar!
    print(Fore.GREEN+'---'*15)
    username = input('| Instagram username? | : ')
    print(Fore.GREEN+'---'*15)
# print ('working so far for {}'.format(username)) # for testing

def main(username):
    userjson = get_user_data(username)
    #get_user_images(userjson,username)
    #exit('works') # testing
    htmldata,fullpath = report_table(userjson,username)
    gen_pdf(htmldata,fullpath,username)
    print('\n\n\n')
    #print(json.dumps(userjson,sort_keys=True,indent=4))


main(username)

exit('thanks for playing')
