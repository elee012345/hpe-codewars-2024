thing = input()
count = 0
charthing = thing[0]
output = ""
for i in range(1, len(thing)):
    charthing = thing[i]
    if thing[i] == charthing:
        count += 1
    if i != len(thing) - 1 and thing[i+1] == charthing:
        pass
    else:
        if count == 4:
            output.append(charthing)
print(output)

for i in range(0, len(thing)):
    charthing = thing[i+1]
    if thing[i] == charthing:
        count += 1
    if count > 4:
        count = 0
        