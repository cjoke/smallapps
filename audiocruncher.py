#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created 25.01.2024 23:12
Author: cjoke
"""

import speech_recognition as sr
from threading import Thread
from queue import Queue


class SpeechRecognizer:
    def __init__(self):
        self.r = sr.Recognizer()
        self.audio_queue = Queue()
        self.recognize_thread = Thread(target=self.recognize_worker)
        self.recognize_thread.daemon = True

    def recognize_worker(self):
        while True:
            audio = self.audio_queue.get()
            if audio is None:
                break

            try:
                print(
                    "You said : "
                    + self.r.recognize_google(audio)
                )
            except sr.UnknownValueError:
                print("You said ? : ")
            except sr.RequestError as errormsg:
                print(
                    "You need an api_key set up, you gready? ; {0}".format(
                        errormsg
                    )
                )

            self.audio_queue.task_done()

    def start(self):
        self.recognize_thread.start()
        with sr.Microphone() as source:
            try:
                while True:
                    self.audio_queue.put(self.r.listen(source))
            except KeyboardInterrupt:
                pass

        self.audio_queue.join()
        self.audio_queue.put(None)
        self.recognize_thread.join()


if __name__ == "__main__":
    recognizer = SpeechRecognizer()
    recognizer.start()
