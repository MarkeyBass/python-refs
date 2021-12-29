f = open("demo.txt", "r+")
f.seek(11)
f.write("py3   ")
f.flush()

input("press enter to change back")

f.seek(11)
f.write("python")
f.close()

