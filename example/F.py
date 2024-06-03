#!/usr/bin/env python
from itertools import permutations


def main():
    with open("input.txt", "r") as input_file, open("output.txt", "w") as output_file:
        word = input_file.readline().strip()
        for p in permutations(word):
            output_file.write("".join(p) + "\n")


if __name__ == "__main__":
    main()
