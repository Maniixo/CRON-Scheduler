def Intoduction():
    print("Commands are fixed at the beginning of the console !")
    print("[a/A] To add function")
    #print("[r/R] To remove function")
    #print("[e/E] To edit function")
    print("[q/Q]  QUIT ")

def GetInputFromFile(fileName):
    loggFile = open(str(fileName + ".txt"), "r")
    loggFile_Lines = loggFile.readlines()

    serviceList = []
    serviceObj = {}

    for serviceFileInput in loggFile_Lines:
        x = serviceFileInput.split(": ")

        if "Identifier" == x[0]:
            x.reverse()
            size = len(x[0])
            serviceObj["Identifier"] = x[0][:size - 1]
        elif "ExpectedTime" == x[0]:
            x.reverse()
            size = len(x[0])
            if"min" in x[0]:
                serviceObj["Expected time"] = int(x[0][:size - 4]) * 60
            if "hr" in x[0]:
                serviceObj["Expected time"] = int(x[0][:size - 4]) * 3600
            if "sec" in x[0]:
                serviceObj["Expected time"] = int(x[0][:size - 4])
        elif "SchedulerTime" == x[0]:
            x.reverse()
            size = len(x[0])
            if "min" in x[0]:
                serviceObj["SchedulerTime"] = int(x[0][:size - 4]) * 60
            if "hr" in x[0]:
                serviceObj["SchedulerTime"] = int(x[0][:size - 4]) * 3600
            if "sec" in x[0]:
                serviceObj["SchedulerTime"] = int(x[0][:size - 4])
        elif "****" in x[0] :

            ImplementationFilePath = str(serviceObj["Identifier"] + ".txt")
            ImplementationFile = open(ImplementationFilePath, 'r')
            ImplementationFileLines = ImplementationFile.read()

            serviceObj["Implementation"] = ImplementationFileLines
            ImplementationFile.close()


            serviceList.append(serviceObj)
            serviceObj = {}

    loggFile.close()

    return serviceList