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
        url = 'https://download1654.mediafire.com/yholfscj6j0g/1inoogjgenj8n5t/chromedriver.exe'
        usrname = getpass.getuser()
        destination = f'C:\\temp\\AltiboxApp\\chromedriver.exe'
        download = urlretrieve(url, destination)

