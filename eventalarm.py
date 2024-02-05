#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import time
import json
import pygame
import threading
import tkinter as tk
from tkinter import messagebox, simpledialog


class Alarm:
    def __init__(self):
        self.alarms = self.load_alarms()

    def load_alarms(self):
        try:
            with open("alarms.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def add_alarm(self, alarm_time, sound_file):
        self.alarms.append(
            {"id": len(self.alarms), "alarm_time": alarm_time, "sound_file": sound_file}
        )
        self.save_alarms()

    def save_alarms(self):
        with open("alarms.json", "w") as file:
            json.dump(self.alarms, file)

    def check_alarms(self):
        while True:
            for alarm in self.alarms:
                alarm_time = datetime.datetime.strptime(
                    alarm["alarm_time"], "%d.%m.%y %H.%M.%S"
                )
                if datetime.datetime.now() >= alarm_time:
                    self.ring_alarm(alarm["id"])
            time.sleep(1)

    def ring_alarm(self, id):
        for alarm in self.alarms:
            if alarm["id"] == id:
                pygame.mixer.init()
                pygame.mixer.music.load(alarm["sound_file"])
                pygame.mixer.music.play()
                self.show_popup(f"Alarm {id} is ringing!")
                self.alarms.remove(alarm)
                self.save_alarms()
                break

    def show_popup(self, message):
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Alarm", message)
        root.destroy()

    def delete_alarm(self, id):
        for alarm in self.alarms:
            if alarm["id"] == id:
                self.alarms.remove(alarm)
                self.save_alarms()
                break

class AlarmGUI:
    def __init__(self, alarm):
        self.alarm = alarm
        self.root = tk.Tk()
        self.root.title("Alarm App")
        self.create_widgets()

    def create_widgets(self):
        self.list_button = tk.Button(
            self.root, text="List Alarms", command=self.list_alarms
        )
        self.list_button.pack()

        self.set_button = tk.Button(self.root, text="Set Alarm", command=self.set_alarm)
        self.set_button.pack()

        self.delete_button = tk.Button(
            self.root, text="Delete Alarm", command=self.delete_alarm
        )
        self.delete_button.pack()

    def list_alarms(self):
        alarms = self.alarm.alarms
        if alarms:
            alarm_list = "\n".join(
                f"ID: {alarm['id']}, Time: {alarm['alarm_time']}, Sound file: {alarm['sound_file']}"
                for alarm in alarms
            )
            messagebox.showinfo("Alarms", alarm_list)
        else:
            messagebox.showinfo("Alarms", "No alarms set.")

    def set_alarm(self):
        alarm_time = simpledialog.askstring(
            "Set Alarm", "Enter the alarm time (dd.mm.yy hh.mm.ss):"
        )
        sound_file = simpledialog.askstring("Set Alarm", "Enter the sound file (.wav):")
        self.alarm.add_alarm(alarm_time, sound_file)

    def delete_alarm(self):
        id = simpledialog.askinteger(
            "Delete Alarm", "Enter the ID of the alarm to delete:"
        )
        self.alarm.delete_alarm(id)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    alarm = Alarm()
    threading.Thread(target=alarm.check_alarms).start()
    gui = AlarmGUI(alarm)
    gui.run()
