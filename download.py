from urllib.request import urlretrieve
import getpass
import os



def download_d():
    dir = os.path.join("C:\\","temp","AltiboxApp")
    if not os.path.exists(dir):
        os.mkdir(dir)
    if os.path.isfile('C:\\temp\\AltiboxApp\\chromedriver.exe'):
        return "File already downloaded"
    else:
        url = 'https://download1654.mediafire.com/6h6wqs1pybmg/c6hwpyd16664ivn/chromedriver.exe'
        usrname = getpass.getuser()
        destination = f'C:\\temp\\AltiboxApp\\chromedriver.exe'
        download = urlretrieve(url, destination)

