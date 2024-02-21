# Small Programs for Daily Fun

This repository contains a collection of small programs that I enjoy using on a daily basis. I've learned Python programming, Git maintenance, and much more along the way. Feel free to download this repo and play with the code.

## Table of Contents
1. [Permbin](#permbin)
2. [Readtoaudio](#readtoaudio)
3. [Aichat](#aichat)
4. [Simple Task Manager](#simple-task-manager)
5. [audiocruncher](#audiocruncher)
6. [crawldir](#crawldir)
7. [Timemanagement](#timemanagement)

## Permbin
Permbin is a program that allows you to upload copied content to termbin.com. It's a great way to share error messages on IRC without being accused of spamming.

### Requirements
- `pyperclip`

### Usage
Copy some text and execute this program. It will upload the copied content to termbin.com. You can then paste the URL in a browser to view your content.

## Readtoaudio
Readtoaudio is a text-to-speech program with high-quality audio. It's application-independent, so you can copy text from anywhere and have it read back to you.

### Requirements
- `gTTS`
- `playsound`
- `pandas`

### Usage
Copy some text and execute this program. It will play back the text you just copied.

## Aichat
Aichat is a chatbot that uses OpenAI's GPT to generate responses. It also logs the conversation with timestamps.

### Requirements
- `openai`
- `speech_recognition`

### Usage
Execute the program to start a conversation with the chatbot.

## Simple Task Manager
This is a simple but dynamic task manager.

### Requirements
- `sqlalchemy`

### Usage
The task manager has a simple dialog:
- 0 = exit
- 1 = list tasks
- 2 = add task
- 3 = remove task

## Audiocruncher
Audiocruncher is a program that can convert audio to text

### Requirements
- `speech_recognition`

## Crawldir
Crawldir is a program that can crawl a directory and list all files and subdirectories.

## Timemanagement
Timemanagement is a program that can help you manage your time. It has a simple dialog:

### Requirements
- `sqlalchemy`
print("1. Add event")
print("2. Remove event")
print("3. Check event")
print("4. View events")
print("5. Exit")
choice = input("Enter choice: ")


