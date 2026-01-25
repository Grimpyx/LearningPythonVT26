def pepLineLength(filename):
    file = open(filename)
    lines = file.readlines()
    file.close()

    lineCounter = 0
    errorCounter = 0
    for line in lines:
        length = len(line)
        if length > 79:
            print(f"line {lineCounter} too long: {length}")
            errorCounter += 1
        lineCounter += 1
    print(f"{errorCounter} lines are too long")

pepLineLength("LearningPythonVT26/8 Files/PEPLines.txt")