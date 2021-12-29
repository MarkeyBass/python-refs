import sys

print("the name of the program is:", sys.argv[0])

for i, argument in enumerate(sys.argv[1:], start=1):
    print("{}) {}".format(i, argument))

print()
print("argv:")
print(sys.argv)



