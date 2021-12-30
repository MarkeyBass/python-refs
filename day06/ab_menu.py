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
        f = open(FILENAME, 'w')
        f.write("{}\n{}".format(a, b))
        f.close()
        print("data saved successfully to: " + FILENAME)

    elif option == 'l':
        f = open(FILENAME)
        a = int(f.readline())
        b = int(f.readline())
        # list comprehension   https://www.w3schools.com/python/python_lists_comprehension.asp
        # a, b = (int(z) for z in f.readlines())
        f.close()
        print("data loaded successfully from: " + FILENAME)

    elif option == 'q':
        break
    else:
        print("error: invalid option")
