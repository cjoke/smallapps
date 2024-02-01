#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import time
import json
import pygame
import threading


class Alarm:
    def __init__(self):
        self.alarms = self.load_alarms()

    def load_alarms(self):
        try:
            with open("alarms.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def input_alarm(self):
        alarm_time = input("Enter the alarm time (dd.mm.yy hh.mm.ss): ")
        sound_file = input("Enter the sound file (.wav): ")
        self.alarms.append(
            {"id": len(self.alarms), "alarm_time": alarm_time, "sound_file": sound_file}
        )
        self.set_alarm()

    def set_alarm(self):
        with open("alarms.json", "w") as file:
            json.dump(self.alarms, file)

    def check_alarm(self):
        while True:
            for alarm in self.alarms:
                alarm_time = datetime.datetime.strptime(
                    alarm["alarm_time"], "%d.%m.%y %H.%M.%S"
                )
                if datetime.datetime.now() >= alarm_time:
                    self.play_alarm(alarm["id"])
            time.sleep(1)

    def play_alarm(self, id):
        for alarm in self.alarms:
            if alarm["id"] == id:
                pygame.mixer.init()
                pygame.mixer.music.load(alarm["sound_file"])
                pygame.mixer.music.play()
                print(f"Alarm {id} is ringing!")
                self.alarms.remove(alarm)
                self.set_alarm()
                break

    def list_alarms(self):
        for alarm in self.alarms:
            print(
                f"ID: {alarm['id']}, Time: {alarm['alarm_time']}, Sound file: {alarm['sound_file']}"
            )

    def delete_alarm(self, id):
        for alarm in self.alarms:
            if alarm["id"] == id:
                self.alarms.remove(alarm)
                self.set_alarm()
                print(f"Alarm {id} has been deleted.")
                break


if __name__ == "__main__":
    alarm = Alarm()
    threading.Thread(target=alarm.check_alarm).start()

    while True:
        print("1. Set alarm")
        print("2. List alarms")
        print("3. Delete alarm")
        option = input("Choose an option: ")
        if option == "1":
            alarm.input_alarm()
        elif option == "2":
            alarm.list_alarms()
        elif option == "3":
            id = int(input("Enter the ID of the alarm to delete: "))
            alarm.delete_alarm(id)
