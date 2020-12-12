from sys import stdin


def main():
    grid = [list(line.strip()) for line in stdin]
    while True:
        # uncomment these lines to see something kind of neat
        # for row in grid:
        #     print("".join(row))
        # print()
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
                adj += int(is_occupied_visible(grid, i1, j1, d))
            if grid[i1][j1] == "L":
                next_grid[i1][j1] = "#" if adj == 0 else "L"
            elif grid[i1][j1] == "#":
                next_grid[i1][j1] = "L" if adj >= 5 else "#"
            else:
                next_grid[i1][j1] = "."
    return next_grid


def is_occupied_visible(grid, i, j, d):
    i += d[0]
    j += d[1]
    while 0 <= i < len(grid) and 0 <= j < len(grid[0]):
        if grid[i][j] == "#":
            return True
        if grid[i][j] == "L":
            return False
        i += d[0]
        j += d[1]
    return False

if __name__ == "__main__":
    main()
