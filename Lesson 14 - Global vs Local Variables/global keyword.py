hello = "Morning"

def func():
    global hello
    hello = "Evening"
    print(hello)

func()
print(hello)