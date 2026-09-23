import sys


def shrink(text):
    print(text[:8])


def enlarge(text):
    print(text + "Z" * (8 - len(text)))


params = sys.argv[1:]

if len(params) < 1:
    print("none")
else:
    for param in params:
        if len(param) > 8:
            shrink(param)
        elif len(param) < 8:
            enlarge(param)
        else:
            print(param)