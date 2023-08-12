START_X = 0
START_Y = 1


def is_free(content):
    return content != "#"


def can_go_right(maze, x_position, y_position, direction):
    if direction == "horizontal":
        return len(maze[0]) - 1 >= y_position + 2 and is_free(maze[x_position][y_position + 2])
    return (
        len(maze[0]) - 1 >= y_position + 1
        and is_free(maze[x_position][y_position + 1])
        and is_free(maze[x_position - 1][y_position + 1])
        and is_free(maze[x_position + 1][y_position + 1])
    )


def can_go_left(maze, x_position, y_position, direction):
    if direction == "horizontal":
        return y_position - 2 >= 0 and is_free(maze[x_position][y_position - 2])
    return (
        y_position - 1 >= 0
        and is_free(maze[x_position][y_position - 1])
        and is_free(maze[x_position - 1][y_position - 1])
        and is_free(maze[x_position + 1][y_position - 1])
    )


def can_go_down(maze, x_position, y_position, direction):
    if direction == "horizontal":
        return (
            len(maze) - 1 > x_position
            and is_free(maze[x_position + 1][y_position - 1])
            and is_free(maze[x_position + 1][y_position])
            and is_free(maze[x_position + 1][y_position + 1])
        )
    return len(maze) - 2 > x_position and is_free(maze[x_position + 2][y_position])


def can_go_up(maze, x_position, y_position, direction):
    if direction == "horizontal":
        return (
            x_position - 1 >= 0
            and is_free(maze[x_position - 1][y_position - 1])
            and is_free(maze[x_position - 1][y_position])
            and is_free(maze[x_position - 1][y_position + 1])
        )
    return x_position - 2 >= 0 and is_free(maze[x_position - 2][y_position])


def can_rotate(maze, x_position, y_position, direction):
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


def find_shortest_distance(maze):
    """BFS Algorithm"""
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
