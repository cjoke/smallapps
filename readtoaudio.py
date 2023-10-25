#!/usr/bin/env python3
#Name           : readtoaudio 
#Author         : https://github.com/cjoke
#Releasedate    : 24.10.2023
#License        : GPL2 (read the document! I havent, but I know its good!)
import gtts.lang
from gtts import gTTS
from tempfile import NamedTemporaryFile
from playsound import playsound
from pandas.io.clipboard import clipboard_get

class ChooseLang:
    # TODO implenent dialog with user and establish language
    def __init__(self):
        languages = gtts.lang.tts_langs()
        print(languages)

    def user_dialog(self):
        choice = input('What language do you prefer? : ')
        return choice

class Speak:
    def __init__(self, text='my little text', lang='en'):
        gTTS(text=text, lang=lang, tld='com.au', slow=False).write_to_fp(voice := NamedTemporaryFile())
        playsound(voice.name)
        voice.close()

if __name__ == '__main__':
    cb = clipboard_get()
    Speak(f'{cb}')
