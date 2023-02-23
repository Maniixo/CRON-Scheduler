import time
from datetime import date, datetime
import os


class Task:

    def __init__(self ,expectedTime, taskImplementation, scheduleTimer, identifier):
        self.expectedTime = expectedTime
        self.taskImplementation = taskImplementation
        self.scheduleTimer = scheduleTimer
        self.identifier = identifier

        try:
            os.remove(self.identifier + "_Logs.txt")
        except FileNotFoundError:
            pass

        self.loggFile = open(self.identifier + "_Logs.txt", "a")


        self.version = 0
        self.versionTry = 0

    def DoSomthing(self):
        # Track time
        startTime = time.time()
        today = date.today()

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        # start the Task
        beginOfTaskStr = str(today) + " " + str(current_time) + " : "+"Starting to execute " + self.identifier ;
        beginOfTaskStr += "\n"
        # time.sleep(5)
        exec(self.taskImplementation)

        # Logging
        endTime = time.time()

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        if( int(round(endTime - startTime)) > int(self.expectedTime)):
            self.WriteInFile(str(self.version) + "." + str(self.versionTry) + " - "
                             + beginOfTaskStr + str(today) + " " + str(current_time) + " : Time exceded ! \nExpected to finish after "
                             + str(self.expectedTime) + " seconds, but it took " + str(round(endTime - startTime)) + " seconds !")
            self.loggFile.write("\n")
        elif (int(round(endTime - startTime)) <= int(self.expectedTime)):
            self.WriteInFile(str(self.version) + "." + str(self.versionTry) + " - "
                             + beginOfTaskStr + str(today) + " " + str(current_time) + " : Done\nFinished in "
                             + str(self.expectedTime) +" seconds, which is less than or equal"
                             + str(self.expectedTime) + " seconds")
            self.loggFile.write("\n")
    def WriteInFile(self, logInfo):
        if self.versionTry == 9:
            self.versionTry = 0
            self.version += 1
        else:
            self.versionTry += 1

        self.loggFile.write(logInfo)
        self.loggFile.write("\n")

    # region end/stop Task

    def TaskStop(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.WriteInFile(
            "****************************** Servies " + self.identifier + " got STOPED at " + current_time + "******************************")

    def TaskDeleted(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.WriteInFile("****************************** Servies " + self.identifier + " got DELETED at " + current_time + "******************************")

    def __del__(self):
        # body of destructor
        self.loggFile.close()

    #endregion