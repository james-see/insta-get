from tkinter import*
import tkgen.gengui
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



if __name__ == '__main__':
    root = tkgen.gengui.TkJson('window.json', title='INSTAGET')
    root.lift()
    root.call('wm', 'attributes', '.', '-topmost', True)
    root.after_idle(root.call, 'wm', 'attributes', '.', '-topmost', False)

    def hello(event=None):
        username = v.get()
        print('getting user json for {}...'.format(username))
        userjson = get_user_data(username)
        print('setting up user data table...')
        htmldata,fullpath = report_table(userjson,username)
        print('generating pdf report...')
        gen_pdf(htmldata,fullpath,username)
        print('done')
        v.set('done!')
        # print(v.get()) # test 
        # print('Hello world') # test

    def open_popup():
        root.toplevel('window.json', title='A dialog')
        root.button('cancel_dialog', close_popup)

    def close_popup():
        dialog = root.get('dialog')
        dialog.master.destroy()

    def exit_app():
        root.destroy()

    # Traditional menu
    root.create_menu({'Exit': exit_app}, name='File')
    some_menu = root.create_menu({'About': hello}, name='Menu')
    root.create_menu({'Subitem': hello}, name='Submenu', parent=some_menu)
    root.create_menu({'?': hello})

    # Popup menu
    popup_menu = root.create_menu({'Foo': open_popup, 'Bar': open_popup},
                                  popup=True)

    def popup(event):
        popup_menu.post(event.x_root, event.y_root)

    # attach popup to frame
    v = root.entry('instauser', key='<Return>', cmd=hello, focus=True)
    frame = root.get('content')
    frame.bind("<Button-3>", popup)

    root.button('cancel', exit_app)
    root.button('ok', hello)

    root.mainloop()
