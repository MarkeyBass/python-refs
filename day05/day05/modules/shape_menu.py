"""
this program uses gfx.py as a module
"""
# print("SHAPE START")

import gfx

while True:
    print("""
    Shape Printer:
    1) print a line
    2) print a full rectangle
    3) print a hollow rectangle
    -------
    0) quit
    """)

    option = input("enter option:")

    if option == '1':
        w = int(input("enter line length:"))
        c = input("enter line character:")
        gfx.print_line(c, w)

    elif option == '2':
        w = int(input("enter rectangle width:"))
        h = int(input("enter rectangle height:"))
        gfx.print_rectangle(w, h)

    elif option == '3':
        w = int(input("enter rectangle width:"))
        h = int(input("enter rectangle height:"))
        gfx.print_hollow_rectangle(w, h)

    elif option == '0':
        break
    else:
        print("error: invalid option")


# print("SHAPE END")
