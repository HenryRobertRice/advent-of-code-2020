from sys import stdin


def main():
    nums = [int(line) for line in stdin]
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == 2020:
                print(f"{nums[i] * nums[j]}")


if __name__ == "__main__":
    main()
