text_file = open("document.txt", "r")
lines = text_file.readlines()
new_list = []

for line in lines:
    new_list.append(line.strip())

print(new_list)
text_file.close()
