from tests.data import maze1, maze2, maze3, maze4, maze5, maze6, maze7
from maze import find_shortest_distance

class TestClass:
    """Maze testing"""

    # Acceptance criteria
    def test_maze1(self):
        """Shortest path for maze 1 should return 11"""
        assert find_shortest_distance(maze1) == 11

    def test_maze2(self):
        """Shortest path for maze 2 should return -1"""
        assert find_shortest_distance(maze2) == -1

    def test_maze3(self):
        """Shortest path for maze 3 should return 2"""
        assert find_shortest_distance(maze3) == 2

    def test_maze4(self):
        """Shortest path for maze 4 should return 16"""
        assert find_shortest_distance(maze4) == 16

    # Extra test
    def test_extra_maze1(self):
        """Shortest path for maze 5 should return -1"""
        assert find_shortest_distance(maze5) == -1
    
    def test_extra_maze2(self):
        """Shortest path for maze 6 should return 15"""
        assert find_shortest_distance(maze6) == 15

    def test_extra_maze3(self):
        """Shortest path for maze 7 should return 16"""
        assert find_shortest_distance(maze7) == 16
        
