from sys import stdin


def main():
    adapters = [int(line) for line in stdin]
    adapters.sort()
    nums = [0] + adapters + [adapters[-1] + 3]
    diffs = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
    print(diffs.count(1) * diffs.count(3))


if __name__ == "__main__":
    main()
