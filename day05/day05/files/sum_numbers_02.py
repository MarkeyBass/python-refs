
f = open("numbers.txt")
s = 0

for line in f:
    if line.strip().isdigit():
        s += int(line)
    else:
        print("ignoring:", line)

f.close()
print(s)
