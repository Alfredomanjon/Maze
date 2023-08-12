"""Module with data to use in tests"""
from tests.data import maze1, maze2, maze3, maze4
from maze import find_shortest_distance

class TestClass:
    """Class representing test from maze"""

    def test_maze1(self):
        """Testing bfs function with example 1"""
        assert find_shortest_distance(maze1) == 11

    def test_maze2(self):
        """Testing bfs function with example 2"""
        assert find_shortest_distance(maze2) == -1

    def test_maze3(self):
        """Testing bfs function with example 3"""
        assert find_shortest_distance(maze3) == 2

    def test_maze4(self):
        """Testing bfs function with example 4"""
        assert find_shortest_distance(maze4) == 16
