# While loop
number = 20
while number <= 25:
    print(number)
    number += 1

# Decrementing
a = 10
while a >= 1:
    print(a)
    a -= 1

# Break
x = 20
while x <= 25:
    print(x)
    if x == 22:
        break
    x += 1

# Decrementing
a = 10
while a >= 1:
    print(a)
    a -= 1

# Break
x = 20
while x <= 25:
    print(x)
    if x == 22:
        break
    x += 1
# Continue
y = 20
while y <= 25:
    y += 1
    if y == 22:
        continue
    print(y)

# For loop
languages = ["python", "PHP", "kotlin"]
for x in languages:
    print(x)

# Range
for num in range(60, 70):
    print(num)
    for z in range(90, 100, 2):
        print(z)
