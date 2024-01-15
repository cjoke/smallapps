# create a simple taskmanager using sqlalchemy
from dataclasses import dataclass
from typing import Callable, List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# create engine
engine = create_engine("sqlite:///task.db", echo=True)

# create session
Session = sessionmaker(bind=engine)
session = Session()

# create base class
Base = declarative_base()

class Task(Base):
    """
    This class represents the Task table in the database.
    """
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    subject = Column(String, max_length=50)
    task = Column(String)
    priority = Column(Integer)

    def __repr__(self):
        return "<Task(task='%s', priority='%s')>" % (self.task, self.priority)

# create table
Base.metadata.create_all(engine)

class AddTask:
    """
    This class is responsible for adding tasks to the database.
    """
    def __init__(self):
        self.user_input_subject = input("Enter subject: ")
        self.user_input_task = input("Enter task: ")
        self.user_input_priority = input("Enter priority: ")
        if (
            self.user_input_subject == ""
            or self.user_input_task == ""
            or self.user_input_priority == ""
        ):
            print("No input entered")
        else:
            self.task = Task(
                subject=self.user_input_subject,
                task=self.user_input_task,
                priority=self.user_input_priority,
            )
            session.add(self.task)
            session.commit()

    def __repr__(self):
        return "<UserInput(subject='%s', task='%s', priority='%s')>" % (
            self.user_input_subject,
            self.user_input_task,
            self.user_input_priority,
        )

class ShowAllTasks:
    """
    This class is responsible for showing all tasks in the database.
    """
    def __init__(self):
        self.tasks = session.query(Task).all()
        for task in self.tasks:
            print(
                f"\nTask id : {task.id} \nSubject : {task.subject}\nTask : {task.task} \nPriority : {task.priority} \n\n"
            )

    def __repr__(self):
        return "<UserQuery(subject='%s', task='%s', priority='%s')>" % (self.tasks)

class DeleteTask:
    """
    This class is responsible for deleting tasks from the database.
    """
    def __init__(self):
        self.task_id = input("Enter task id to delete: ")
        if self.task_id == "":
            print("No task id entered")
            exit()
        else:
            self.task = session.query(Task).filter_by(id=self.task_id).first()
            session.delete(self.task)
            session.commit()

    def __repr__(self):
        return "<UserDelete(task_id='%s', task='%s')>" % (self.task_id, self.task)

@dataclass
class Command:
    """
    This class represents a command that the user can execute.
    """
    name: str
    action: Callable[[], None]

class UserInput:
    """
    This class is responsible for processing user input.
    """
    def __init__(self):
        self.commands = self.initialize_commands()

    def initialize_commands(self) -> List[Command]:
        return [
            Command("0", self.exit),
            Command("1", ShowAllTasks),
            Command("2", AddTask),
            Command("3", DeleteTask),
        ]

    def exit(self):
        session.close()
        exit()

    def process_input(self):
        user_input = input(
            " \n 0 to exit :\n 1 to show all tasks \n 2 to add a task :\n 3 to delete a task : "
        )
        for command in self.commands:
            if user_input == command.name:
                command.action()
                break
        else:
            print("Invalid input")

    def __repr__(self):
        return "<UserInput(user_input='%s')>" % (self.user_input)

if __name__ == "__main__":
    user_input = UserInput()
    while True:
        user_input.process_input()
