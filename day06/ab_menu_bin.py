FILENAME = "data.bin"
SIZE = 4                # size limit of 4 byte per number
ORDER = 'little'        # endianess of the binary data to save/load

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
        f = open(FILENAME, 'wb')

        # data = a.to_bytes(SIZE, ORDER) + b.to_bytes(SIZE, ORDER)
        # f.write(data)

        f.write(a.to_bytes(SIZE, ORDER))
        f.write(b.to_bytes(SIZE, ORDER))

        f.close()
        print("data saved successfully to: " + FILENAME)

    elif option == 'l':
        f = open(FILENAME, 'rb')

        data = f.read(SIZE)
        a = int.from_bytes(data, ORDER)

        b = int.from_bytes(f.read(SIZE), ORDER)

        # data = f.read()
        # a = int.from_bytes(data[:SIZE], ORDER)
        # b = int.from_bytes(data[SIZE:], ORDER)

        f.close()
        print("data loaded successfully from: " + FILENAME)

    elif option == 'q':
        break
    else:
        print("error: invalid option")

