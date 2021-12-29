
while True:
    try:
        x = int(input("Enter an integer: "))
        print(x, " is an integer")
        break
    except ValueError:
        print("you didn't enter an integer")
    except KeyboardInterrupt:
        print("KeyboardInterrupt quiting the program")
        quit()
