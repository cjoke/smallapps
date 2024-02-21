#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created 25.01.2024 23:12
Author: cjoke
"""

import speech_recognition as sr
import audioop
from threading import Thread
from queue import Queue


class SpeechRecognizer:
    def __init__(self, threshold=3000):
        # Initialize the speech recognizer and set the threshold
        self.r = sr.Recognizer()
        self.audio_queue = Queue()
        self.recognize_thread = Thread(target=self.recognize_worker)
        self.recognize_thread.daemon = True
        self.threshold = threshold

    def recognize_worker(self):
        # This function runs in a separate thread and processes the audio data
        while True:
            audio = self.audio_queue.get()
            if audio is None:
                break

            try:
                print("You said: " + self.r.recognize_google(audio))
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as errormsg:
                print(
                    "Could not request results from Google Speech Recognition service; {0}".format(
                        errormsg
                    )
                )

            self.audio_queue.task_done()

    def start(self):
        # Start the recognition thread and begin recording audio
        self.recognize_thread.start()
        with sr.Microphone(device_index=None) as source:  # Do not specify a device index
            try:
                while True:
                    audio = self.r.record(source, duration=5)
                    rms = audioop.rms(audio.frame_data, audio.sample_width)
                    # If the audio level is above the threshold, add it to the queue
                    if rms > self.threshold:
                        self.audio_queue.put(audio)
            except KeyboardInterrupt:
                pass

        self.audio_queue.join()
        self.audio_queue.put(None)
        self.recognize_thread.join()


if __name__ == "__main__":
    recognizer = SpeechRecognizer()
    recognizer.start()
