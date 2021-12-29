import sys

try:
    f = open('myfilee.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as e:
    print("OS error({0}): {1}".format(e.errno, e.strerror))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
