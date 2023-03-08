#!/usr/bin/python3
def fizzbuzz():
    fizz = "Fizz"
    buzz = "Buzz"
    fizzbuzz = "FizzBuzz"
    last = "Buzz"
    for pau in range(1, 101):
        if pau % 3 == 0 and pau % 5 == 0:
            print("{}".format(fizzbuzz), end=" ")
        elif pau % 3 == 0:
            print("{}".format(fizz), end=" ")
        elif pau % 5 == 0:
            print("{}".format(buzz), end=" ")
        elif pau == 100:
            print("{}".format(last))
        else:
            print("{}".format(pau), end=" ")
