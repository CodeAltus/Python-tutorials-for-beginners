total = 0

def add(x, y):
    global total
    total = x + y
    print(f"Inside function: {total}")

add(1, 2)
print(f"Outside function: {total}")