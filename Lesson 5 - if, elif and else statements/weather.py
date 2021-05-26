# Write a program to take in temperature and print out:
# "Very cold": 0 to 10
# "Cold": 10 to 20
# "Normal": 20 to 25
# "Hot": 25 to 30
# "Very Hot": 30 to 35

temperature = 33

if temperature >= 0 and temperature < 10:
    print("Very cold")

elif temperature >= 10 and temperature < 20:
    print("Cold")

elif temperature >= 20 and temperature < 25:
    print("Normal")

elif temperature >= 25 and temperature < 30:
    print("Hot")

elif temperature >= 30 and temperature < 35:
    print("Very hot")