try:
    x = "10"
    f = open("hello.txt")
    c = x / 0

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Cannot convert string with characters to an integer")

except FileNotFoundError:
    print("File not found")

else:
    print(v)

finally:
    print("Done")

