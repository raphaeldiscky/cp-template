#!/usr/bin/env python
import sys


def main():
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
    T = int(input())
    for case in range(1, T + 1):
        A = int(input())
        B = int(input())
        K = int(input())

        divisible_count = count_divisible_numbers(A, B, K)

        print(f"Case {case}: {divisible_count}")


# Start here --------------------
def count_divisible_numbers(A, B, K):
    count = 0
    for i in range(A, B + 1):
        if i % K == 0:
            count += 1
    return count


# END here -----------------------


if __name__ == "__main__":
    main()
