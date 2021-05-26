# 1 + 2 + 3 + ... + n >= 100

Sum = 0
number = 1

while True:
    Sum += number
    if Sum >= 100:
        break
    number += 1

print(number)
print(Sum)