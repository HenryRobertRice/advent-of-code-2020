from sys import stdin


def main():
    grid = [line.strip() for line in stdin]
    answer = 1
    params = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ]
    for p in params:
        answer *= slope(grid, p[0], p[1])
    print(answer)


def slope(grid, r, d):
    encountered = [grid[i * d][i * r % len(grid[0])] for i in range(len(grid) // d)]
    return encountered.count("#")


if __name__ == "__main__":
    main()
