def getInput():
    output = []
    while True:
        try:
            stuff = input()
            output.append(stuff)
        except:
            break
    return output


stringRect = getInput()
final = []
longest = len(stringRect[0])
for a in range(len(stringRect)):
    line = stringRect[a]
    newLine = [' '] * longest
    if a == 0 or a == len(stringRect) - 1:
        newLine = ['#'] * longest
    newLine[0] = "#"
    newLine[-1] = "#"
    final.append(newLine)

    
thing = []
for i in final:
    a = ""
    for j in i:
        a += j
    thing.append(a)

if stringRect == thing:
    print("Nothing to do.")
else:
    for i in final:
        for j in i:
            print(j, end="")
        print()
    
# height = len(stuff)
# width = len(stuff[0])
# result = []
# for i in range(height):
#     if i == 0 or i == height - 1:
