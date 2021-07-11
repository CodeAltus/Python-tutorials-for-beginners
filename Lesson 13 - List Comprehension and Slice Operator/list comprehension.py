[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

my_list = []

for x in range(0, 10):
    my_list.append(x)

print(my_list)

new_list = [0 for x in range(0, 10)]
print(new_list)

fruits = ["apples", "pears", "bananas"]
new_fruits = [fruit for fruit in fruits]
print(new_fruits)

new_list = [x for x in range(0, 10)]
print(new_list)