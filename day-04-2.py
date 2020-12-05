from sys import stdin


def main():
    valid = 0
    buffer_ = []
    for line in stdin:
        if line != "\n":
            buffer_.append(line.strip())
        else:
            valid += int(is_valid_passport(buffer_))
            buffer_ = []
    print(valid)


def is_valid_passport(buffer_):
    required_keys = [
        "byr", "iyr", "eyr", "hgt",
        "hcl", "ecl", "pid"
    ]
    passport_string = " ".join(buffer_)
    passport_list = passport_string.split()
    passport_dict = {}
    for item in passport_list:
        k, v = item.split(":")
        passport_dict[k] = v
    for key in required_keys:
        if key not in passport_dict:
            return False
        if not is_valid_value(key, passport_dict[key]):
            return False
    return True


def is_valid_value(k, v):
    if k == "byr":
        return 1920 <= int(v) <= 2002 if v.isdigit() else False
    if k == "iyr":
        return 2010 <= int(v) <= 2020 if v.isdigit() else False
    if k == "eyr":
        return 2020 <= int(v) <= 2030 if v.isdigit() else False
    if k == "hgt":
        if v[-2:] == "cm":
            height = v[:len(v) - 2]
            return 150 <= int(height) <= 193 if height.isdigit() else False
        if v[-2:] == "in":
            height = v[:len(v) - 2]
            return 59 <= int(height) <= 76 if height.isdigit() else False
        return False
    if k == "hcl":
        return len(v) == 7 and v[0] == "#" and sum([int(c in "1234567890abcdef") for c in v[1:]]) == 6
    if k == "ecl":
        return v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if k == "pid":
        return len(v) == 9 and v.isdigit()
    if k == "cid":
        return True
    return False


if __name__ == "__main__":
    main()
