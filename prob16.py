nums = input()
counts = [0] * 60000
for i in range(len(nums)):
    if nums[i] == 0:
        break
    counts[i] += 1

biggest = 0
biggestIndex = ""
secondBiggest = 0
secondBiggestIndex = ""
for i in range(len(nums)):
    num = counts[i]
    if num > secondBiggest:
        if num > biggest:
            biggest = num
            biggestIndex = i
        else:
            secondBiggest = num
            secondBiggest = i

print(f"Trending: {biggestIndex} [{biggest} count]")
print(f"Second Place: {secondBiggestIndex} [{secondBiggest} count]")