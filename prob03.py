# times = []
# '\n'.join()
# for i in range(3):
#     times.append(input())

times = []
while True:
    try:
        time = input()
    except:
        break
    if time == -1:
        break
    times.append(time)

for i in range(len(times)):
    time = int(times[i])
    if i == len(times) - 1:
        break
    if time != 1 and i != len(times):
        print(f"You, {times[i]} minutes ago.")
    else:
        print(f"You, {times[i]} minute ago.")   




