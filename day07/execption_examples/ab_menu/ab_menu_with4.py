FILENAME = "data.txt"
a = b = 0

while True:
    print("""
    A = {}; B = {}
    
    Set (A)
    Set (B)
    (S)ave
    (L)oad
    (Q)uit
    """.format(a, b))

    option = input("enter option:").lower()

    if option == 'a':
        try:
            a = int(input("enter a new value for A:"))
        except ValueError:
            print("error: not an int!")

    elif option == 'b':
        try:
            b = int(input("enter a new value for B:"))
        except ValueError:
            print("error: not an int!")

    elif option == 's':
        try:
            with open(FILENAME, 'w') as f:
                f.write("{}\n{}".format(a, b))
        except FileNotFoundError:
            print("cannot find the file:", FILENAME)
        except PermissionError:
            print("cannot write to:", FILENAME)
        else:
            print("data saved successfully to: " + FILENAME)

    elif option == 'l':
        try:
            with open(FILENAME) as f:
                a = int(f.readline())
                b = int(f.readline())
        except OSError:
            print("could not open for writing:", FILENAME)
        except ValueError:
            print(FILENAME, "is corrupted (does not contain two lines of ints)")
        else:
            print("data loaded successfully from: " + FILENAME)

    elif option == 'q':
        break
    else:
        print("error: invalid option")