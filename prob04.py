def getInput():
    output = []
    while True:
        try:
            stuff = input()
            output.append(stuff)
        except:
            break
    return output

output = getInput()
breakchar = output[0]
picture = output[1].split(breakchar)
for i in picture:
    print(i)

print()
print()