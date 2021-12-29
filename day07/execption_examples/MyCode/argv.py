import sys
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

# py argv.py input_exeption.py
# C:\dev\python\daysShmuel\day07\execption_examples\MyCode>py argv.py input_exeption.py
# input_exeption.py has 11 lines
