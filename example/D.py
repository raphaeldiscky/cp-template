#!/usr/bin/env python
import sys


def main():
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)


# Start here --------------------

# END here -----------------------


if __name__ == "__main__":
    main()
