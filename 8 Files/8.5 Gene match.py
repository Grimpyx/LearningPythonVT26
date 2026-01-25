def gene_match(gene, genome):
    file = open(genome)
    geneAsListOfChar = list(gene)
    currentGene = list(file.read(len(gene)))

    # Step through the genome
    readChar = '0'
    currentIteration = 0
    while True:
        # Check match
        match = True # start assumption is true
        for i in range(len(geneAsListOfChar)):
            if geneAsListOfChar[i] != currentGene[i]:
                match = False
                break
        # If match, print the current iteration
        if match: print(currentIteration)
        
        # Read the next character
        readChar = file.read(1) # this method should ensure we can handle an "infinitely big" file
        currentIteration += 1
        # Stop if the next character is empty (reached end of file)
        if readChar == '':
            file.close()
            return
        currentGene.append(readChar)  # Append the next read character.
        currentGene = currentGene[1:] # Removes the first character.
        

gene_match("ACA", "LearningPythonVT26/8 Files/Genome.txt")