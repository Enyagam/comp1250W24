floors = 1

while floors <= 20:
    if floors == 13:
        floors += 1
        continue
    print("You are on floor", floors)
    floors += 1
print("*" * 20)

for floor in range(1, 21):
    if floor == 13:
        continue
    print(floor)

