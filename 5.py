chars = input().split(" ")
for i in range(len(chars)):
    if chars[i] == "":
        continue
    print(chr(int(chars[i])), end="")
    