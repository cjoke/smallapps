#!/usr/bin/env python3
import speech_recognition as sr


class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def recognize_speech(self):
        with sr.Microphone() as source:
            print("Speak something...")
            AudioData = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(AudioData)
            if "exit" in text:
                exit()
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand you.")

        except sr.RequestError as e:
            print("Sorry, an error occurred while connecting to Google Speech \
                  Recognition service:", str(e))


if __name__ == "__main__":
    speech_recognizer = SpeechRecognizer()
    speech_recognizer.recognize_speech()

