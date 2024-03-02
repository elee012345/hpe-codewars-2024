def getInput():
    output = []
    while True:
        try:
            stuff = input()
            output.append(stuff)
        except:
            break
    return output
