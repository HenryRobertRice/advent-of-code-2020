from sys import stdin


def main():
    valid = 0
    buffer_ = []
    for line in stdin:
        if line != "\n":
            buffer_.append(line.strip())
        else:
            valid += int(is_valid(buffer_))
            buffer_ = []
    print(valid)


def is_valid(buffer_):
    required_keys = [
        "byr", "iyr", "eyr", "hgt",
        "hcl", "ecl", "pid"
    ]
    passport = " ".join(buffer_)
    for key in required_keys:
        if key not in passport:
            return False
    return True


if __name__ == "__main__":
    main()
