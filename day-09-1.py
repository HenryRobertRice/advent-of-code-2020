from itertools import combinations
from sys import stdin

def main():
    nums = [int(line) for line in stdin]
    for i in range(5, len(nums)):
        if not is_valid(nums[i], nums[i - 5: i]):
            print(f"invalid {nums[i]}")
            print(nums[i])
            return


def is_valid(n, prev):
    for c in combinations(prev, 2):
        if n == c[0] + c[1]:
            return True
    return False


if __name__ == "__main__":
    main()
