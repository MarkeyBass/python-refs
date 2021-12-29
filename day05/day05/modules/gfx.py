"""
see shapes_menu.py using this as a module.
"""
# FUNCTIONS:
# print("GFX START")


def print_line(c, length, has_newline=True):
    print(c * length, end='')
    if has_newline:
        print()


def print_rectangle(width, height):
    for row in range(height):

        # print each column of the line
        print_line('* ', width, False)

        # print a newline
        print()


def print_hollow_rectangle(width, height):
    print_line('* ', width, True)
    if height > 1:
        for row in range(height-2):
            if width > 1:
                print("* ", end="")
                print_line('  ', width-2, False)
            print("* ")

        print_line('* ', width, True)


# MAIN
if __name__ == '__main__':
    print("GFX main code start:")
    w = 5
    h = 3
    print_rectangle(w, h)
    print()
    print_hollow_rectangle(8, 4)
    print("GFX main code end")

# print("GFX END")

