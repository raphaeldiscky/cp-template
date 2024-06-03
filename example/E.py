#!/usr/bin/env python
import sys


def main():
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")

    def binary_search(array, value, low, high):
        if high < low:
            return -1
        else:
            mid = (low + high) // 2
            if array[mid] > value:
                return binary_search(array, value, low, mid - 1)
            elif array[mid] < value:
                return binary_search(array, value, mid + 1, high)
            else:
                return mid

    array = []
    for i in range(10000):
        array.append(int(input()))
    for i in range(10000):
        value = int(input())
        answer = binary_search(array, value, 0, len(array) - 1)
        print("%d" % answer)


# Start here --------------------

# END here -----------------------


if __name__ == "__main__":
    main()
