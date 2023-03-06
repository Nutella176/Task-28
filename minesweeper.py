# Creating a 2D list
grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"],
]


def count_mines(grid, r_index, c_index):
    """Function which uses a loop to count the mines in the surrounding 8 cells of each cell."""
    numb_mine = 0
    for r_offset, c_offset in [
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
    ]:
        if 0 <= r_index + r_offset < len(grid) and 0 <= c_index + c_offset < len(
            grid[0]
        ):
            if grid[r_index + r_offset][c_index + c_offset] == "#":
                numb_mine += 1
    return numb_mine


def mine_field(grid):
    """Function which takes in grid, replaces its cell values (if not a "#") by the number of mines surrounding it and returns the updated 2D list."""
    output = []
    for r_index, row in enumerate(grid):
        output_row = []
        for c_index, cell in enumerate(row):
            if cell == "#":
                output_row.append("#")
            else:
                output_row.append(str(count_mines(grid, r_index, c_index)))
        output.append(output_row)
    return output


# Joining and printing each row on separate lines
result = mine_field(grid)
for row in result:
    print(" ".join(row))
