""" Maze functions:
        - Contains functions for finding best path using BFS
"""
import time

START_X = 0
START_Y = 1


def is_free(content):
    """Check if content is equal to #"""
    return content != "#"


def can_go_right(maze, x_position, y_position, direction):
    """Checks if it's possible to go right based on direction so it can't go
    off the edges or collide with #"""

    if direction == "horizontal":
        return len(maze[0]) - 1 >= y_position + 2 and is_free(
            maze[x_position][y_position + 2]
        )
    return (
        len(maze[0]) - 1 >= y_position + 1
        and is_free(maze[x_position][y_position + 1])
        and is_free(maze[x_position - 1][y_position + 1])
        and is_free(maze[x_position + 1][y_position + 1])
    )


def can_go_left(maze, x_position, y_position, direction):
    """Checks if it's possible to go left based on direction so it can't go
    off the edges or collide with #"""

    if direction == "horizontal":
        return y_position - 2 >= 0 and is_free(maze[x_position][y_position - 2])
    return (
        y_position - 1 >= 0
        and is_free(maze[x_position][y_position - 1])
        and is_free(maze[x_position - 1][y_position - 1])
        and is_free(maze[x_position + 1][y_position - 1])
    )


def can_go_down(maze, x_position, y_position, direction):
    """Checks if it's possible to go down based on direction so it can't go
    off the edges or collide with #"""

    if direction == "horizontal":
        return (
            len(maze) - 1 > x_position
            and is_free(maze[x_position + 1][y_position - 1])
            and is_free(maze[x_position + 1][y_position])
            and is_free(maze[x_position + 1][y_position + 1])
        )
    return len(maze) - 2 > x_position and is_free(maze[x_position + 2][y_position])


def can_go_up(maze, x_position, y_position, direction):
    """Checks if it's possible to go up based on direction so it can't go
    off the edges or collide with #"""

    if direction == "horizontal":
        return (
            x_position - 1 >= 0
            and is_free(maze[x_position - 1][y_position - 1])
            and is_free(maze[x_position - 1][y_position])
            and is_free(maze[x_position - 1][y_position + 1])
        )
    return x_position - 2 >= 0 and is_free(maze[x_position - 2][y_position])


def can_rotate(maze, x_position, y_position, direction):
    """Check if it is possible to rotate the rod, checking at all times that
    there are no obstacles and that it does not go out of range"""

    if len(maze) - 2 > x_position >= 1 and len(maze[0]) - 2 > y_position >= 1:
        if direction == "horizontal":
            return (
                is_free(maze[x_position - 1][y_position - 1])
                and is_free(maze[x_position - 1][y_position])
                and is_free(maze[x_position - 1][y_position - 1])
                and is_free(maze[x_position + 1][y_position - 1])
                and is_free(maze[x_position + 1][y_position])
                and is_free(maze[x_position + 1][y_position + 1])
            )
        return (
            is_free(maze[x_position - 1][y_position - 1])
            and is_free(maze[x_position - 1][y_position - 1])
            and is_free(maze[x_position][y_position + 1])
            and is_free(maze[x_position][y_position - 1])
            and is_free(maze[x_position + 1][y_position - 1])
            and is_free(maze[x_position + 1][y_position + 1])
        )
    return False


def find_shortest_distance(maze):
    """BFS Algorithm for finding the shortest path in the maze
    Guaranteed constraints:
        - 3 ≤ labyrinth.length ≤ 1000,
        - 3 ≤ labyrinth[i].length ≤ 1000"""

    end_x_vertical = len(maze) - 2
    end_y_vertical = len(maze[0]) - 1
    end_x_horizontal = len(maze) - 1
    end_y_horizontal = len(maze[0]) - 2

    posibilities = []
    posibilities.append((START_X, START_Y, "horizontal"))
    visited = []
    counter = 0

    while len(posibilities) > 0:
        temp_possibilities = []
        for node in posibilities:
            if node not in visited:
                x_position = node[0]
                y_position = node[1]
                direction = node[2]
                if (x_position, y_position) == (end_x_vertical, end_y_vertical) or (
                    x_position,
                    y_position,
                ) == (end_x_horizontal, end_y_horizontal):
                    return counter
                if can_rotate(maze, x_position, y_position, direction):
                    temp_possibilities.append(
                        (
                            x_position,
                            y_position,
                            "horizontal" if direction == "vertical" else "vertical",
                        )
                    )
                if can_go_down(maze, x_position, y_position, direction):
                    temp_possibilities.append((x_position + 1, y_position, direction))
                if can_go_right(maze, x_position, y_position, direction):
                    temp_possibilities.append((x_position, y_position + 1, direction))
                if can_go_up(maze, x_position, y_position, direction):
                    temp_possibilities.append((x_position - 1, y_position, direction))
                if can_go_left(maze, x_position, y_position, direction):
                    temp_possibilities.append((x_position, y_position - 1, direction))
        visited.extend(posibilities)
        posibilities = temp_possibilities
        counter += 1

    return -1


if __name__ == "__main__":
    start_time = time.time()
    print(
        "Example 1 solution: ",
        find_shortest_distance(
            [
                [".", ".", ".", ".", ".", ".", ".", ".", "."],
                ["#", ".", ".", ".", "#", ".", ".", ".", "."],
                [".", ".", ".", ".", "#", ".", ".", ".", "."],
                [".", "#", ".", ".", ".", ".", ".", "#", "."],
                [".", "#", ".", ".", ".", ".", ".", "#", "."],
            ]
        ),
    )
    end_time = time.time()
    print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")
