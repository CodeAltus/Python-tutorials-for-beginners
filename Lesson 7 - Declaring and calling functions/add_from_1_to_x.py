# Write a function named add_from_1_to_x
# that takes in one parameter
# and adds the consecutive values from 1 to parameter inclusive
# Eg. if parameter is 10 then return
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55

def add_from_1_to_x(x):
    result = x * (x + 1) / 2
    return result

print(add_from_1_to_x(1000000000000))
