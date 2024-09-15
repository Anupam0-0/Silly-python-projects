import time

my_time = int(input("Enter the time in seconds: "))

# for x in range(0, my_time):
#     print(x)
#     time.sleep(1)

for x in range(my_time, 0, -1):
    hours = x // 3600
    rem = x % 3600
    minutes = rem // 60
    # minutes = (x // 60) % 60
    seconds = x % 60
    print(f"{hours}:{minutes}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP")
