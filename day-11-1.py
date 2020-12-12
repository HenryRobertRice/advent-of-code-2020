from sys import stdin


def main():
    grid = [list(line.strip()) for line in stdin]
    while True:
        next_grid = update(grid)
        if next_grid == grid:
            break
        grid = next_grid
    print(sum([row.count("#") for row in grid]))


def update(grid):
    next_grid = [list("?" * len(grid[0])) for _ in range(len(grid))]
    dirs = [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, 1], [1, -1]]
    for i1 in range(len(grid)):
        for j1 in range(len(grid[0])):
            adj = 0
            for d in dirs:
                i2 = i1 + d[0]
                j2 = j1 + d[1]
                if 0 <= i2 < len(grid) and 0 <= j2 < len(grid[0]):
                    if grid[i2][j2] == "#":
                        adj += 1
            if grid[i1][j1] == "L":
                next_grid[i1][j1] = "#" if adj == 0 else "L"
            elif grid[i1][j1] == "#":
                next_grid[i1][j1] = "L" if adj >= 4 else "#"
            else:
                next_grid[i1][j1] = "."
    return next_grid


if __name__ == "__main__":
    main()
