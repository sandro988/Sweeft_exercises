import random

def grid_generator():
    """Function for generating random grid with randomly placed bombs in it"""

    rows = random.randint(3, 10)
    columns = random.randint(3, 10)

    grid = [[". " for i in range(columns)] for j in range(rows)]

    bomb_count = random.randint(
        round((rows * columns) / 10), (rows * columns) / max(rows, columns)
    )  # Choosing number of bombs depending on the row and column count
    bomb_positions = {
        (random.randint(0, rows - 1), random.randint(0, columns - 1))
        for i in range(bomb_count + 1)
    }  # Choosing positions for bombs in grid

    # Asigning 'O' to the positions that i randomly chose above
    for indexI, charI in enumerate(grid):
        for indexJ, charJ in enumerate(charI):
            if (indexI, indexJ) in bomb_positions:
                grid[indexI][indexJ] = "O "

    return rows, columns, grid, bomb_positions, bomb_count


def bomber_man(N, G):

    rows, columns, grid, first_batch_of_bombs = G[0], G[1], G[2], G[3]
    pretty_grid = "".join(["".join(k) + "\n" for k in grid]).rstrip()

    if N == 1 or N == 0:
        return pretty_grid
    elif N % 2 == 0:
        return pretty_grid.replace(".", "O")
    else:
        for _ in range(((N // 2) + 1) % 2 + 1):
            newgrid = [["O "] * columns for i in range(rows)]

            def blownUp(x, y):
                if 0 <= x < rows and 0 <= y < columns:
                    newgrid[x][y] = ". "

            xi = [0, 0, 0, 1, -1]
            yi = [0, -1, 1, 0, 0]

            for x in range(rows):
                for y in range(columns):
                    if grid[x][y] == "O ":
                        for i, j in zip(xi, yi):
                            blownUp(x + i, y + j)

            grid = newgrid
            result_grid = "".join(["".join(k) + "\n" for k in grid]).rstrip()

        return (
            f"Rows: {rows}, Columns: {columns}\n"
            f"Row and Column of first batch of bombs: {first_batch_of_bombs}\n\n"
            f"Initial Grid:\n\n{pretty_grid}\n\n"
            f"Result grid:\n\n{result_grid}"
        )


n = int(input("Enter number of seconds: "))
grid = grid_generator()

print(bomber_man(n, grid))
