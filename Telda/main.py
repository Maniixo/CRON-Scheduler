# My Imports

from Helper import helper
from Models import Hangfire
import threading

HangireServices = {}

helper.Intoduction()

while True:
    commandInput = input("Enter a command :")
    if commandInput.lower() == "a":

        #region Task's identifier

        while True:
            identifier = input("Task's identifier ? ")
            if identifier in HangireServices:
                print("The identifier entered already exists, try again")
            else:
                break;

        #endregion

        # region Task's implementation

        taskImplementation = input("Enter the task's implementation :")

        # endregion

        # region Expected time

        expectedTime = input("Enter expected time to finish the task :")

        size = len(expectedTime)

        if "min" in expectedTime:
            expectedTime = int(expectedTime[:size - 3]) * 60
        if "hr" in expectedTime:
            expectedTime = int(expectedTime[:size - 2]) * 3600
        if "sec" in expectedTime:
            expectedTime = int(expectedTime[:size - 3])

        # endregion

        # region Scheduler time

        scheduleTimer = input("Enter the tasks' scheduler time ? ")

        size = len(scheduleTimer)

        if "min" in scheduleTimer:
            scheduleTimer = int(scheduleTimer[:size - 3]) * 60
        if "hr" in scheduleTimer:
            scheduleTimer = int(scheduleTimer[:size - 2]) * 3600
        if "sec" in scheduleTimer:
            scheduleTimer = int(scheduleTimer[:size - 3])
        # endregion

        #Create the Servive's object that contains all the service's details
        serviceObj = Hangfire.Hangfire(expectedTime, taskImplementation, scheduleTimer, identifier)

        HangireServices[identifier] = serviceObj
        print("Service created and will start soon !")
        serviceRunObj = threading.Thread(target= serviceObj.work)
        serviceRunObj.start()

        continue

    # elif commandInput.lower() == "r":
    #     removalIdentifier = input("Enter the task's identifier:")
    #
    #     taskObj = HangireServices[removalIdentifier]
    #     HangireServices.pop(removalIdentifier)
    #
    #     serviceRemoveObj = threading.Thread(target=taskObj.DeleteTask)
    #     serviceRemoveObj.start()
    #
    #     print("Service removed successfuly !")
    #     continue
    elif commandInput.lower() == "q":
        print("Running tasks will not execute again.")
        print("Please wait till running tasks finishes.")


        for taskObj in HangireServices.values():

            serviceRemoveObj = threading.Thread(target=taskObj.StopWorking())
            serviceRemoveObj.start()
        break;
    else:
        print("Unimplemented !")
