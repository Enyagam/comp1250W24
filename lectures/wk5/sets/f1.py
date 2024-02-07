s1 = set("hello")  # helo
print(s1)

s2 = set("world")
print(s2)

print(s1.intersection(s2))
print(s1 & s2)

s3 = set([1, "hi", False])
print(s3)



for value in s1:
    print(value)