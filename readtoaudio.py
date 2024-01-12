#!/usr/bin/env python3
# Name           : readtoaudio
# Author         : https://github.com/cjoke
# Releasedate    : 24.10.2023
# License        : GPL3
# License        : GPL2 (read the document! I havent, but I know its good!)
import os
from tempfile import NamedTemporaryFile
import gtts.lang
from gtts import gTTS
from playsound import playsound
from pandas.io.clipboard import clipboard_get
from google.cloud import translate_v2 as translate

credentials = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]

class InfoLang:
    def __init__(self):
        self.lang = gtts.lang.tts_langs()
        self.lang = sorted(self.lang.items(), key=lambda x: x[1])
        self.lang = dict(self.lang)

    def __call__(self):
        for i, j in self.lang.items():
            print(i, j)
        return self.lang

class UserInput:
    def __init__(self, default="en"):
        self.default = default
        self.langs = InfoLang()()
        self.user_input = input("Enter your language: ")

    def __call__(self):
        if self.user_input in self.langs:
            return self.user_input
        else:
            print("Invalid language. Defaulting to English.")
            return self.default

class Translate:
    def __init__(self):
        self.text = clipboard_get()
        self.translate_client = translate.Client()
        self.target = UserInput()()
        self.translation = self.translate_client.translate(
            self.text, target_language=self.target
        )
    def __call__(self):
        return self.translation

class Speak:
    def __init__(self, text="my little text", lang=UserInput()()):
        gTTS(text=text, lang=lang, tld="com.au", slow=False).write_to_fp(
            voice := NamedTemporaryFile()
        )
        playsound(voice.name)
        voice.close()


if __name__ == "__main__":
    cb = clipboard_get()
    translation = Translate()()
    if cb:
        Speak(f"{translation}")
    else:
        Speak("hey my little angel")
