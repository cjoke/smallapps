#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 14:51:37 2020

This program is a time management tool that allows the user to input a task

it will contain a main set of functions
* add/remove events

Classes
  - add event (name, date, time, duration)
  - remove event (name, date, time, duration)
  - add evencheck (name, date, time, duration)

  - add while loop to check for events

"""

from dataclasses import dataclass
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


@dataclass
class Event(Base):
    __tablename__ = "events"

    id: int
    name: str
    date: datetime
    duration: int

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(DateTime)
    duration = Column(Integer)


class TimeManagement:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add_event(self, name, date, duration):
        session = self.Session()
        event = Event(name=name, date=date, duration=duration)
        session.add(event)
        session.commit()

    def remove_event(self, name):
        session = self.Session()
        event = session.query(Event).filter_by(name=name).first()
        if event:
            session.delete(event)
            session.commit()

    def check_event(self, name):
        session = self.Session()
        event = session.query(Event).filter_by(name=name).first()
        return bool(event)

    def view_events(self):
        session = self.Session()
        events = session.query(Event).all()
        return events


def notify(self):
    session = self.Session()
    events = session.query(Event).all()
    now = datetime.now()
    for event in events:
        if event.date <= now:
            print(f"Event {event.name} is due")


class UserDialog:
    def __init__(self, tm):
        self.tm = tm

    def add_event(self):
        name = input("Enter event name: ")
        date = input("Enter event date (YYYY-MM-DD): ")
        time = input("Enter event time (HH:MM): ")
        duration = input("Enter event duration in minutes: ")
        date_time = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        self.tm.add_event(name, date_time, duration)

    def remove_event(self):
        name = input("Enter event name: ")
        self.tm.remove_event(name)

    def check_event(self):
        name = input("Enter event name: ")
        if self.tm.check_event(name):
            print("Event exists")
        else:
            print("Event does not exist")

    def view_events(self):
        events = self.tm.view_events()
        for event in events:
            print(event)


if __name__ == "__main__":
    db_url = "sqlite:///timemanagement.db"
    tm = TimeManagement(db_url)
    ud = UserDialog(tm)

    while True:
        notify()
        while True:
            print("1. Add event")
            print("2. Remove event")
            print("3. Check event")
            print("4. View events")
            print("5. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                ud.add_event()
            elif choice == "2":
                ud.remove_event()
            elif choice == "3":
                ud.check_event()
            elif choice == "4":
                ud.view_events()
            elif choice == "5":
                break
            else:
                print("Invalid choice")
