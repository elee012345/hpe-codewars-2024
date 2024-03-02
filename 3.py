# times = []
# '\n'.join()
# for i in range(3):
#     times.append(input())
times = input()
for i in range(len(times)):
    time = int(times[i])
    if time == -1:
        break
    if time != 1:
        print(f"You, {times[i]} minutes ago.")
    else:
        print(f"You, {times[i]} minute ago.")   




