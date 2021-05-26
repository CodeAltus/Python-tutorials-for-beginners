my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

Sum = 0

for item in my_list:
    print("Hello")
    if item == 5 or item == 8:
        continue
    Sum += item
    print(item)

print(Sum)