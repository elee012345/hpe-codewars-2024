def getInput():
    output = []
    while True:
        try:
            stuff = input()
            output.append(stuff)
        except:
            break
    return output


stuff = getInput()
a = stuff[0]
z = []
for i in range(len(a)):
    if not str(stuff[i]).isnumeric():
        z.append(stuff[i])
checksum = stuff[1].split("=")
checksum = checksum[1]
