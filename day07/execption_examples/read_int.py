
while True:
    try:
        num = int(input("enter an int:"))
        break
    except ValueError:
        print("that's not an int!")

print(num, "* 5 = ", num * 5)
