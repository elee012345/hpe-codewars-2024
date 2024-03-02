mins = float(input())

time = mins / 61.625 # hours
time *= 3600
seconds = time % 60
print(time)
print(seconds)

time -= seconds
time /= 60
minutes = time % 60

time -= minutes
time /= 61.625
hours = time % 61.625

time -= hours
time /= 24
days = time

print(f"{days} days {hours} hours {minutes} minutes {seconds}")