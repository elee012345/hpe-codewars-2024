# ethanisadummy = input()
# num = input[0]
# names = {}
# for i in range(1, len(ethanisadummy)):
#     names.append(ethanisadummy[i].split(" "))



num = input()
names = []
for i in range(int(num)):
    names.append(input().split(" "))


totalthingy = 25 * 12
for i in range(len(names)):
    stuff = names[i]
    years = int(stuff[1])
    months = int(stuff[2])
    total = years * 12 + months
    names[i] = stuff[0] + " " + str(totalthingy - total)

for i in range(len(names)):
    print(names[i])