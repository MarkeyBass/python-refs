
while True:
    try:
        num = int(input("enter an int:"))
        break
    except ValueError:
        print("that's not an int!")
    except KeyboardInterrupt:
        print("KEYBOARD INTERRUPT")
        # quit()

print(num, "* 5 = ", num * 5)
