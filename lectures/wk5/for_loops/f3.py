dow = "monday tuesday wednesday thursday friday saturday sunday".split(" ")
print(dow)

for each_day in dow:
    print(each_day)
    for hour in range(1, 25):
        print("\t", "Hour", hour, end=" ")
    print()