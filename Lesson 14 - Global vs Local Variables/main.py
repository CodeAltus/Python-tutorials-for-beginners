hello = "Morning"

def func():
    global hello
    hello = hello * 2
    print(f"func: {hello}")

func()
print(hello)