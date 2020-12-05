from sys import stdin


def main():
    grid = [line.strip() for line in stdin]
    encountered = [grid[i][i * 3 % len(grid[0])] for i in range(len(grid))]
    print(encountered.count("#"))


if __name__ == "__main__":
    main()
