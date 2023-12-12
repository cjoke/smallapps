#!/usr/bin/env python
'''
This is a audio chat module that is ment for having
a conversation with chatGPT stationed at openai.com
'''

# TODO : Have to make this module useful for the main module.

import openai
import time
from utils.textformatter import TextFormatter
from utils import microphone


def get_api_key():
    with open("api_key.txt", "r") as file:
        api_key = file.read()  # .strip()
    return api_key


api_key = get_api_key()
openai.api_key = api_key

messages = [{"role": "system", "content": "You are a nice intelligent python code assistant."}]


def log_conversation(conversation, filename):
    with open(filename, 'a') as logfile:
        logfile.write(f"\n TIMESTAMP : {time.ctime()} " + "\n ")
        for line in conversation:
            logfile.write(line)


# TODO  fix this variable inside if statement
# luring = None


while True:
    # TODO get this out of this module
    recording = microphone.SpeechRecognizer()
    recorded_message = recording.recognize_speech()

    if recorded_message == "text please":
        recorded_message = input(" Message to chatGPT here : ")

    # message = input(f" Message to chatGPT here : ")
    if recorded_message == "exit":
        exit()

    if recorded_message:
        messages.append({"role": "user", "content": recorded_message}, )
        mycontent  = openai.chat.completions.create(model="gpt-3.5-turbo",
                                                messages=messages,
                                                temperature=0.7,
                                                max_tokens=256)

    reply = mycontent.choices[0].message.content
    formatter = TextFormatter(reply)
    formatted_output = formatter.format_output()
    reply = formatted_output
    logger = f"USER INPUT : {recorded_message} " + "\n" + f" ChatGPT :{reply} "
    print(f"CHAT GPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
    # TextEater(reply)
    log_conversation(logger, "conversation_log.txt")
