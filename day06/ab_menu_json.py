import json

FILENAME = "data.json"
values = {'a': 0, 'b': 0}

while True:
    print("""
    A = {}; B = {}
    
    Set (A)
    Set (B)
    (S)ave
    (L)oad
    (Q)uit
    """.format(values['a'], values['b']))

    option = input("enter option:").lower()

    if option == 'a':
        values['a'] = int(input("enter a new value for A:"))
    elif option == 'b':
        values['b'] = int(input("enter a new value for B:"))

    elif option == 's':
        f = open(FILENAME, 'w')
        json.dump(values, f)
        f.close()
        print("data saved successfully to: " + FILENAME)

    elif option == 'l':
        f = open(FILENAME)
        values = json.load(f)
        f.close()
        print("data loaded successfully from: " + FILENAME)

    elif option == 'q':
        break
    else:
        print("error: invalid option")
