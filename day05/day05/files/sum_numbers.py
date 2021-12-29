
f = open("numbers.txt")
s = 0

while True:
    line = f.readline()

    # if line is not empty
    if line:
        if line.strip().isdigit():
            s += int(line)
        else:
            print("ignoring:", line)
    else:
        break
f.close()
print(s)
