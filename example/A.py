import sys

"""
Sample input:
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0


Sample output:
19
"""


def main():
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
    data = [list(map(int, input().split())) for _ in range(6)]
    print(hourglassSum(data))


def hourglassSum(arr: list[list[int]]) -> int:
    max_sum = float("-inf")

    for i in range(4):
        for j in range(4):
            # sum top three element
            top = sum(arr[i][j : j + 3])
            # sum of mid element
            mid = arr[i + 1][j + 1]
            # sum bottom three element
            bottom = sum(arr[i + 2][j : j + 3])

            cur_sum = top + mid + bottom

            max_sum = max(max_sum, cur_sum)
    return int(max_sum)


if __name__ == "__main__":
    main()
