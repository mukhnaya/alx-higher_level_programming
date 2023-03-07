#!/usr/bin/python3
import string
for x in string.ascii_lowercase:
    if (x == 'q'):
        continue
    if (x == 'e'):
        continue
    print("{}".format(x), end="")
