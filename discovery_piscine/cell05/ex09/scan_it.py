import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    count = len(re.findall(re.escape(sys.argv[1]), sys.argv[2]))
    if count == 0:
        print("none")
    else:
        print(count)