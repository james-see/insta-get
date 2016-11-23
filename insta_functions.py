from time import sleep
import requests
import json
from config import *
from tqdm import tqdm,trange
from tabulate import tabulate
from weasyprint import HTML, CSS
from PIL import Image
from io import BytesIO
import os
#def get_user_data(username):
#    r = requests.get('https://www.instagram.com/'+username+'/?__a=1', stream=True)
#    total_length = int(r.headers.get('content-length'))
#    jsoned = ''
#    for i in trange(total_length):
#        pass
#    jsoned = json.loads(jsoned)
#    return jsoned

import urllib
#from tqdm import tqdm

def my_hook(t):
  """
  Wraps tqdm instance. Don't forget to close() or __exit__()
  the tqdm instance once you're done with it (easiest using `with` syntax).

  Example
  -------

  >>> with tqdm(...) as t:
  ...     reporthook = my_hook(t)
  ...     urllib.urlretrieve(..., reporthook=reporthook)

  """
  last_b = [0]

  def inner(b=1, bsize=1, tsize=None):
    """
    b  : int, optional
        Number of blocks just transferred [default: 1].
    bsize  : int, optional
        Size of each block (in tqdm units) [default: 1].
    tsize  : int, optional
        Total size (in tqdm units). If [default: None] remains unchanged.
    """
    if tsize is not None:
        t.total = tsize
    t.update((b - last_b[0]) * bsize)
    last_b[0] = b
  return inner

def get_user_data(username):
    eg_link = 'https://www.instagram.com/'+username+'/?__a=1'
    usernamefile = 'user_'+username+'.json'
    with tqdm(unit='B', unit_scale=True, miniters=1,desc=username) as t:
        urllib.request.urlretrieve(eg_link, filename=storage_path+usernamefile,
                       reporthook=my_hook(t), data=None)
    with open(storage_path+usernamefile) as f:
        jsonit = json.load(f)
    print("stored data as {}".format(usernamefile))
    return jsonit

def report_table(jsondata,username):
    try: os.mkdir(os.path.join(storage_path, username))
    except: print('directory for user already exists, continuing to write')
    try: os.mkdir(os.path.join(storage_path, username+'/images'))
    except: print('images sub directory already exists for profile image storage, continuing to write')
    projdir = storage_path+username+'/'
    usernamefile = 'user_'+username+'.html'
    fullpath = projdir+usernamefile
    reporter = {"info_type":[],"info":[]}
    # get profile image
    imagetodownload = jsondata['user']['profile_pic_url_hd']
    response = requests.get(imagetodownload)
    img = Image.open(BytesIO(response.content)).save(projdir+'images/'+username+'.jpg')
    for key in jsondata['user']:
        if key == 'media':
            continue
        if key == 'follows' or key == 'followed_by':
            reporter['info_type'].append(key)
            reporter['info'].append(jsondata['user'][key]['count'])
            continue
        reporter['info_type'].append(key)
        reporter['info'].append(jsondata['user'][key])
    htmltable = tabulate(reporter,headers="keys",tablefmt="html")
    htmldata = "<!DOCTYPE=HTML><body><img src='images/"+username+".jpg'>"+htmltable+"</body></html>"
    # print(htmltable) # testing html output
    with open(projdir+usernamefile,'w') as f:
        f.write(htmldata)
    return htmldata,fullpath

def gen_pdf(htmldata,fullpath,username):
    filename = fullpath.rsplit('/',1)[1]
    HTML(filename=fullpath).write_pdf(storage_path+username+'/'+filename+".pdf",
    stylesheets=[CSS(string='body { font-family: sans-serif !important; } @page { size: A3; margin: 1cm; } table {border-collapse: collapse;} table,th, td {border: 1px solid black;} th {background-color:#d3d3d3;}')])
    return "success"
