# This code is write in pycharmCommunity
# step-1: In console paste the Command - " pip install pyshorteners" and press Enter.
# step-2: Again paste it - " pip install pyperclip " amd press Enter.


import pyshorteners

url = input('Enter OR Paste Your URL:>> ')


def shortenURL(full_link):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))

shortenURL(url)

