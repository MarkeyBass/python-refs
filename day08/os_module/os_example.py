import  os

# For more protection use subprocess module instead os

print(os.listdir())
os.chdir('../../')
print(os.listdir())

lessonIndex = open('lessonIndex.TXT').read()
print(lessonIndex)

