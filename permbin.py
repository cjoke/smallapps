#!/usr/bin/env python3
# Name              : permbin.py
# Author            : https://github.com/cjoke
# Version           : 0.1-rc1
# Releasedate       : 20.10.2023
# License           : GPL2 (read the document! I havent, but I know its good!)

import subprocess
from pyperclip import paste, copy

'''
Before use you will need paste and copy from pyperclip
pip install pyperclip

just copy some text and execute this program.
It will give no output. But, it will give back and store an url in system memory.
you can then paste your url in a browser and read the content your self or,
share the url with anyone that wants to read your content. Or both.
'''


class ClipnPaste:
    """This one just grabs stuff and return it"""
    def __init__(self):
        self.data = paste()

    def __str__(self):
        data = self.data.strip()
        return data


class Main:
    """Grabs stuff from ClipnPaste, uploads and returns an url in system memory"""
    def __init__(self):
        data = ClipnPaste()
        data = str(data)
        cmd = f"echo '{data}' | nc termbin.com 9999"
        send = subprocess.check_output(cmd, shell=True)
        url = send.decode("utf-8")
        copy(url)


if __name__ == "__main__":
    Main()
