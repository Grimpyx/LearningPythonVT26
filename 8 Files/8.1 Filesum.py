def filesum(fileName):
    file = open(fileName)
    lines = file.readlines()
    file.close()

    sum = 0
    for line in lines:
        sum += int(line)
    return sum

print(filesum("LearningPythonVT26/8 Files/Testing.txt")) # the default directory is the vscode repo, PYTHON VT26