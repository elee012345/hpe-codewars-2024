output = []
while True:
    try:
        stuff = input()
        output.append(stuff)
    except:
        break

addresses = []
for i in output:
    if i == "END":
        break
    addresses.append(i)
print(addresses)
for address in addresses:
    address = address.split(", ")
    print(address[0])
    print(address[1])
    print(f"{address[2]}, {address[3]} {address[4]}")
    print()

print()