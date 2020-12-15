def main():
    est = int(input())
    times = [int(x) for x in input().split(",") if x.isdigit()]
    diffs = [get_diff(est, x) for x in times]
    min_diff = min(diffs, key = lambda d: d[0])
    print(min_diff[0] * min_diff[1])


def get_diff(est, x):
    y = x
    while y < est:
        y += x
    return [y - est, x]


if __name__ == "__main__":
    main()
