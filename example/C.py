#!/usr/bin/env python
import sys


def main():
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
    T = int(input())
    for i in range(1, T + 1):
        row, col = int(input()), int(input())
        maps = [list(input().strip()) for _ in range(row)]
        visited = [[False] * col for _ in range(row)]
        fractions = {}
        conquer = 0
        for j in range(row):
            for k in range(col):
                if not visited[j][k] and maps[j][k] not in ("#", "."):
                    temp_fractions = set()
                    find_and_contest(maps, visited, temp_fractions, row, col, j, k)
                    if len(temp_fractions) > 1:
                        conquer += 1
                    elif temp_fractions:
                        frac = temp_fractions.pop()
                        fractions[frac] = fractions.get(frac, 0) + 1
        print(f"Case {i}:")
        for key in sorted(fractions.keys()):
            print(f"{key} {fractions[key]}")
        print(f"contested {conquer}")


# Start here --------------------


def find_and_contest(maps, visited, temp_fractions, row, col, x, y):
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        if x < 0 or x >= row or y < 0 or y >= col or visited[x][y] or maps[x][y] == "#":
            continue
        visited[x][y] = True
        if maps[x][y] != ".":
            temp_fractions.add(maps[x][y])
        # Add adjacent cells to the stack
        stack.extend(
            [
                (x + dx, y + dy)
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]
                if 0 <= x + dx < row and 0 <= y + dy < col
            ]
        )


# END here -----------------------


if __name__ == "__main__":
    main()
