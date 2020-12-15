from sympy.ntheory.modular import crt


def main():
    est = int(input())
    times = [x for x in input().split(",")]
    nums = [int(t) for t in times if t != "x"]
    mods = [int(times[i]) - i for i in range(len(times)) if times[i] != "x"]
    # realizing i needed the chinese remainder theorem was a challenge in itself
    # i decided i'd earned the right to "cheat" by importing an implementation
    print(crt(nums, mods)[0])


if __name__ == "__main__":
    main()
