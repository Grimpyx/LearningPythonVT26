def passwords(fileName):
    passDict = {}
    file = open(fileName)
    lines = file.readlines()
    file.close()
    for line in lines:
        elements = line.split(" ")
        passDict[elements[0]] = elements[1].rstrip('\n') # removes \n from the right hand side
    print(passDict)
    return passDict

passwords("LearningPythonVT26/8 Files/Passwords.txt")