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
        a = int(input("enter a new value for A:"))
    elif option == 'b':
        b = int(input("enter a new value for B:"))

    elif option == 's':
        with open(FILENAME, 'w') as f:
            f.write("{}\n{}".format(a, b))

        print("data saved successfully to: " + FILENAME)

    elif option == 'l':
        with open(FILENAME) as f:
            a = int(f.readline())
            b = int(f.readline())

        print("data loaded successfully fromq: " + FILENAME)

    elif option == 'q':
        break
    else:
        print("error: invalid option")