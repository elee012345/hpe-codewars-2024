def getInput():
    output = []
    while True:
        try:
            stuff = input()
            output.append(stuff)
        except:
            break
    return output

socks = getInput()[:-1]
stuff = {}
for i in range(len(socks)):
    sock = socks[i]
    if stuff.get(sock) == None:
        stuff[sock] = 1
    else:
        stuff[sock] += 1

printed = False
for i in stuff.items():
    if i[1] < 2:
        print(i[0])
        printed = True
if not printed:
    print("No lost socks")
