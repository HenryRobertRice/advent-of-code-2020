from sys import stdin

def main():
    nums = [process(line.strip()) for line in stdin]
    print(max(nums))


def process(binary):
    row = "".join(["1" if c == "B" else "0" for c in binary[:7]])
    col = "".join(["1" if c == "R" else "0" for c in binary[7:]])
    return 8 * int(row, 2) + int(col, 2)


if __name__ == "__main__":
    main()
