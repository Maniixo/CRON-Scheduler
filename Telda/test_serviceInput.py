import time
import unittest

import Helper.helper
from Models import Hangfire
import threading
from Helper import helper


class TestHangfire(unittest.TestCase):

    def test_FaliedGroup(self):

        inputList = Helper.helper.GetInputFromFile("Many Service [TimeExceded]")

        self.ServicesList = {}

        for serives in inputList:

            # region Task's identifier
            identifier = serives["Identifier"]
            # endregion
            # region Task's implementation
            taskImplementation = serives["Implementation"]
            # endregion
            # region Expected time
            expectedTime = serives["Expected time"]
            # endregion
            # region Scheduler time
            scheduleTimer = serives["SchedulerTime"]
            # endregion

            serviceObj = Hangfire.Hangfire(expectedTime, taskImplementation, scheduleTimer, identifier)

            serviceThread = threading.Thread(target=serviceObj.work)

            print("Service[" + identifier + "] created and will start soon !")

            serviceThread.start()
            self.ServicesList[serviceObj] = serviceThread

        outputString = ""

        commandInput = input("Click [q/Q] to quit :")
        if commandInput.lower() == "q":
            print("Ending running services")

            for serviceObj in self.ServicesList.keys():

                failed = False;

                serviceRemoveObj = threading.Thread(target=serviceObj.StopWorking)
                serviceRemoveObj.start()

                self.ServicesList[serviceObj].join()

                loggFile = open(str(serviceObj.identifier + "_Logs.txt"), "r")
                loggFile_Lines = loggFile.readlines()
                loggFile.close()

                for serviceOutput in loggFile_Lines:
                    if serviceOutput == "" or serviceOutput == "\n":
                        continue
                    elif ": Time exceded" in serviceOutput :
                        failed = True
                    elif "STOPED" in serviceOutput  or ": Starting to execute" in serviceOutput :
                        continue
                if failed :
                    outputString += "Failed"
                else:
                    outputString += "Okay"

        self.assertEqual(outputString, str("Okay" * len(inputList)))

if __name__ == '__main__':
    unittest.main()
