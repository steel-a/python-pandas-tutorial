#How many years ago did you buy your car?
years = 3

if years <= 3:
    print("It's a new car!")
elif years > 10:
    print("It's an old car!")
else:
    print("It's a car! :)")


# Simplified version
print("It's a new car!" if years <= 3 else "It's an old car!")