#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Name           : texttoaudio
# Author         : cjoke
# url            :https://github.com/cjoke
# Releasedate    : 24.10.2023
# License        : GPL3

"""
This is a simple script to read the text from the clipboard and convert it to audio.
It uses the Google Cloud Translate API to translate the text to the desired language.
you can translate from any language to any language.
"""

import os
from tempfile import NamedTemporaryFile

import gtts.lang
from google.cloud import translate_v2 as translate
from gtts import gTTS
from pandas.io.clipboard import clipboard_get
from playsound import playsound

# Set your Google Cloud credentials
credentials = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]


# Class to get the available languages
class InfoLang:
    def __init__(self):
        self.language_codes = gtts.lang.tts_langs()
        self.sorted_languages = sorted(self.language_codes.items(), key=lambda x: x[1])
        self.sorted_languages = dict(self.sorted_languages)

    def __call__(self):
        for code, language in self.sorted_languages.items():
            print(code, language)
        return self.sorted_languages


# Class to get the user's input for language
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


# Class to translate the text
class Translate:
    def __init__(self, target):
        text = clipboard_get()
        translate_client = translate.Client()
        self.translation = translate_client.translate(text, target_language=target)

    def __call__(self):
        return self.translation["translatedText"]


# Class to speak the translated text
class Speak:
    def __init__(self, text="my little text", lang="en"):
        gTTS(text=text, lang=lang, tld="com.au", slow=False).write_to_fp(
            voice := NamedTemporaryFile()
        )
        playsound(voice.name)
        voice.close()


# Main function
if __name__ == "__main__":
    target = UserInput()()
    translation = Translate(target)()
    if clipboard_get() != "":
        print(translation)
        Speak(translation, target)
    else:
        Speak("No text in clipboard.")
