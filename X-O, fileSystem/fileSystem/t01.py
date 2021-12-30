import os


# דריסה
# def myFunc():
#     print('Hello')
#     file = open('hello.txt', 'w')
#     file.write('text')
# file.close()


# def myFunc():
#     print('Hello')
#     if os.path.exists('hello.txt'):
#         file = open('hello.txt', 'r+')
#         file.seek(18)
#         file.write('NEW TEXT 1')
#         file.close()


def readFile():
    file = open('hello.txt')
    data = file.read()
    file.close()
    return data


def saveToFile(ans):
    try:
        file = open('ans.txt', 'w')
        file.write('Answer: ' + str(ans))
        file.close()
        return True
    except():
        return False


def findOcuurences(tarStr, locStr):
    count = 0

    if len(tarStr) > 1:
        analize = locStr.split(' ')
        for word in analize:
            if word.lower() == tarStr.lower():
                count += 1

    if len(tarStr) == 1:
        for letter in locStr:
            if letter == tarStr:
                count += 1

    return count


if __name__ == '__main__':
    #
    # f = open('lorem.txt', 'r')
    # count = findOcuurences('lorem', f.read())
    # print(count)
    #
    # f2 = open('count.txt', 'w')
    # f2.write(str(count))

    status = saveToFile(findOcuurences('Lorem', readFile()))

    if status:
        print(':)')
    else:
        print(':(')

