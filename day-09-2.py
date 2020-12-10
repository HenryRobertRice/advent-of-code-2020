from itertools import combinations
from sys import stdin

def main():
    nums = [int(line) for line in stdin]
    for i in range(25, len(nums)):
        if not is_valid(nums[i], nums[i - 25: i]):
            print(find_weakness(nums[i], nums))
            return


def is_valid(n, prev):
    for c in combinations(prev, 2):
        if n == c[0] + c[1]:
            return True
    return False


def find_weakness(n, nums):
    for i in range(2, len(nums)):
        seqs = [nums[j: j + i] for j in range(0, len(nums) - i)]
        for s in seqs:
            if sum(s) == n:
                return min(s) + max(s)
    return -1


if __name__ == "__main__":
    main()
