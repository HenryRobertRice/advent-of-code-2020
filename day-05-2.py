from sys import stdin

def main():
    nums = [process(line.strip()) for line in stdin]
    nums.sort()
    for i in range(1, len(nums) - 1):
        if nums[i + 1] == nums[i] + 2:
            print(nums[i] + 1)
            return


def process(binary):
    row = "".join(["1" if c == "B" else "0" for c in binary[:7]])
    col = "".join(["1" if c == "R" else "0" for c in binary[7:]])
    return 8 * int(row, 2) + int(col, 2)


if __name__ == "__main__":
    main()
