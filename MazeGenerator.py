import random

def generate_maze(rows, cols):
    # Create a grid where every cell has four walls
    maze = [
        [{"N": 1, "S": 1, "E": 1, "W": 1} for _ in range(cols)]
        for _ in range(rows)
    ]

    visited = [[False for _ in range(cols)] for _ in range(rows)]

    # Direction: row change, column change, current wall, opposite wall
    directions = [
        (-1, 0, "N", "S"),
        (1, 0, "S", "N"),
        (0, 1, "E", "W"),
        (0, -1, "W", "E")
    ]

    # Start DFS from the top-left cell
    stack = [(0, 0)]
    visited[0][0] = True

    while stack:
        r, c = stack[-1]

        # Find unvisited neighboring cells
        neighbors = []

        for dr, dc, wall, opposite in directions:
            nr, nc = r + dr, c + dc

            if (0 <= nr < rows and
                0 <= nc < cols and
                not visited[nr][nc]):
                neighbors.append((nr, nc, wall, opposite))

        if neighbors:
            # Choose a random unvisited neighbor
            nr, nc, wall, opposite = random.choice(neighbors)

            # Remove the wall between the two cells
            maze[r][c][wall] = 0
            maze[nr][nc][opposite] = 0

            visited[nr][nc] = True
            stack.append((nr, nc))

        else:
            # Backtrack when no unvisited neighbor exists
            stack.pop()

    return maze


def display_maze(maze):
    rows = len(maze)
    cols = len(maze[0])

    # Print the top boundary
    print("+" + "---+" * cols)

    for r in range(rows):
        # Print cell contents and vertical walls
        line = "|"
        for c in range(cols):
            line += "   " if maze[r][c]["E"] == 0 else "   |"
        print(line)

        # Print horizontal walls
        line = "+"
        for c in range(cols):
            line += "   +" if maze[r][c]["S"] == 0 else "---+"
        print(line)


def main():
    print("=== MAZE GENERATION USING DFS ===")

    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))

        if rows <= 0 or cols <= 0:
            print("Error: Rows and columns must be positive integers.")
            return

        maze = generate_maze(rows, cols)

        print("\nGenerated Maze:")
        display_maze(maze)

    except ValueError:
        print("Error: Please enter valid integers.")


if __name__ == "__main__":
    main()
