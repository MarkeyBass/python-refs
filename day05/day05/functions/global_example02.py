# Function Definitions:
def modify_x():
    global x
    print("FUNCTION START")
    # x = 2
    # x += 10
    # x = x + 10
    x = 13
    print(x)
    # x = 13
    print("FUNCTION END")


# Main:
x = 5
modify_x()
print(x)

