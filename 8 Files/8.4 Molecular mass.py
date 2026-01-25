def m_mass(molecule):
    # Idea, read next character. If it's a number, we add another of the previous by n-1.
    # (CH4 should become C H 3*H)

    # Read atom data
    file = open("atoms.txt")
    atomsDict = {}
    print(file.readline(0))
    
    # Very short way of writing:
    # "For each line, split it, and unpack the data as firstElement and secondElement"
    # Because the data in atoms.txt looks a bit weird, we have to not only
    # remove '\n' but also all white spaces to the right, otherwise the split
    # gives more then two elements, where most are just empty chars ''.
    for (firstElement, secondElement) in (line.rstrip('\n').rstrip(' ').split(' ') for line in file.readlines()):
        atomsDict[firstElement] = float(secondElement)
    file.close()

    # Look up molemass for each atom in the molecule
    sum = 0
    previousCharValue = 0
    for char in molecule:
        # If char is a number (n), we add the previous char value and multiply it by n-1
        if char.isdigit(): sum += previousCharValue * (int(char) - 1)
        else:
            previousCharValue = atomsDict.get(char, 0) # if atom doesnt exist its iterpreted as having weight 0
            sum += previousCharValue # Add to sum
    return sum
    

