from sys import stdin


def main():
    print(sum([int(is_valid(line)) for line in stdin]))


def is_valid(line):
    parts = line.split()
    min_, max_ = map(int, parts[0].split("-"))
    char = parts[1][0]
    password = parts[2]
    char_count = sum([int(c == char) for c in password])
    return min_ <= char_count and char_count <= max_


if __name__ == "__main__":
    main()
