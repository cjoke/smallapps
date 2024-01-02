# create a simple taskmanager using sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# create engine
engine = create_engine('sqlite:///task.db', echo=True)

# create session
Session = sessionmaker(bind=engine)
session = Session()

# create base class
Base = declarative_base()

# create table
class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    subject = Column(String, max_length=50)
    task = Column(String)
    priority = Column(Integer)

    def __repr__(self):
        return "<Task(task='%s', priority='%s')>" % (self.task, self.priority)


# create table
Base.metadata.create_all(engine)

# user input class for input
class AddTask:
    def __init__(self):
        self.user_input_subject = input("Enter subject: ")
        self.user_input_task = input("Enter task: ")
        self.user_input_priority = input("Enter priority: ")
        if self.user_input_subject == "" or self.user_input_task == "" or self.user_input_priority == "":
            print("No input entered")
        else:
            self.task = Task(subject=self.user_input_subject, task=self.user_input_task, priority=self.user_input_priority)
            session.add(self.task)
            session.commit()

    def __repr__(self):
        return "<UserInput(subject='%s', task='%s', priority='%s')>" % (self.user_input_subject, self.user_input_task, self.user_input_priority)

# create a user query class to show all tasks
class ShowAllTasks:
    def __init__(self):
        self.tasks = session.query(Task).all()
        for task in self.tasks:
            print(f"\nTask id : {task.id} \nSubject : {task.subject}\nTask : {task.task} \nPriority : {task.priority} \n\n")

    def __repr__(self):
        return "<UserQuery(subject='%s', task='%s', priority='%s')>" % (self.tasks)

# create a class to delete a task
class DeleteTask:
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


# create a choose class, to show all tasks, add or delete a task.
class ChooseOption:
    def __init__(self):
        self.user_input = input(" \n 0 to exit :\n 1 to show all tasks \n 2 to add a task :\n 3 to delete a task : ")
        if self.user_input == "0":
            session.close()
            exit()
        elif self.user_input == "1":
            ShowAllTasks()
        elif self.user_input == "2":
            AddTask()
        elif self.user_input == "3":
            DeleteTask()
        else:
            print("Invalid input")

    def __repr__(self):
        return "<UserInput(user_input='%s')>" % (self.user_input)


if __name__ == '__main__':
    while True:
        ChooseOption()
