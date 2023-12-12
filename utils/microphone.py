#!/usr/bin/env python3
import speech_recognition as sr
'''
A little helper for Buttler.py  I did put in a control for when either
user want to send data or exit application.
'''
# TODO need to drag out the control should not be in this class!


class SpeechRecognizer:
    def __init__(self):
        # Initialize recognizer class
        self.recognizer = sr.Recognizer()

    def recognize_speech(self):
        # Capture audio from microphone
        with sr.Microphone() as source:
            print("Speak something...")
            AudioData = self.recognizer.listen(source)

        try:
            # Recognize speech using Google Speech Recognition
            text = self.recognizer.recognize_google(AudioData)
            if "exit" in text:
                exit()
            """print("you said : " + text)
            reply = input("Do you want to apply content? (y/n)")
            if reply == "n":
                exit()"""
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand you.")

        except sr.RequestError as e:
            print("Sorry, an error occurred while connecting to Google Speech \
                  Recognition service:", str(e))


if __name__ == "__main__":
    speech_recognizer = SpeechRecognizer()
    speech_recognizer.recognize_speech()

