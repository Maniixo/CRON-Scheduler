import time
import threading
from datetime import datetime
from Models import Task

class Hangfire:
    working = True

    def __init__(self, expectedTime, taskImplementation, scheduleTimer, identifier):

        self.identifier = identifier
        self.scheduleTimer = scheduleTimer
        self.expectedTime = expectedTime
        self.taskImplementation = taskImplementation

        self.newTask = Task.Task(expectedTime, taskImplementation, scheduleTimer, identifier)
        self.newTaskThread = threading.Thread(target = self.newTask.DoSomthing)

    def work(self):
        while self.working:
            self.newTaskThread = threading.Thread(target = self.newTask.DoSomthing)
            self.newTaskThread.start()
            time.sleep(int(self.scheduleTimer))
        self.newTaskThread.join()
        self.newTask.loggFile.close()

    def StopWorking(self):
        self.working = False
        self.newTask.TaskStop()

    def DeleteTask(self):
        self.working = False
        self.newTask.TaskDeleted()