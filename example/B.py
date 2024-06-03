#!/usr/bin/env python
import sys


def main():
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
    T = int(input())
    for case_number in range(1, T + 1):
        N = int(input())
        M = int(input())
        grid = [input().strip() for _ in range(N)]
        word = input().strip()
        result = search_word(grid, word)
        print(f"Case {case_number}: {result}")


# Start here --------------------
def search_word(grid, word):
    def search_direction(x, y, dx, dy):
        count = 0
        for i, char in enumerate(word):
            if 0 <= x + dx * i < len(grid) and 0 <= y + dy * i < len(grid[0]):
                if grid[x + dx * i][y + dy * i] != char:
                    return 0
            else:
                return 0
        return 1

    word_count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # Search in all directions from the current cell
            for dx, dy in [
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1),
                (-1, -1),
                (-1, 1),
                (1, -1),
                (1, 1),
            ]:
                word_count += search_direction(row, col, dx, dy)
    return word_count


# END here -----------------------


if __name__ == "__main__":
    main()
