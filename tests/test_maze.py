"""Module with data to use in tests"""
from tests.data import maze1, maze2, maze3, maze4
from maze import maze_bfs

class TestClass:
    """Class representing test from maze"""

    def test_maze1(self):
        """Testing bfs function with example 1"""
        assert maze_bfs(maze1) == 11

    def test_maze2(self):
        """Testing bfs function with example 2"""
        assert maze_bfs(maze2) == -1

    def test_maze3(self):
        """Testing bfs function with example 3"""
        assert maze_bfs(maze3) == 2

    def test_maze4(self):
        """Testing bfs function with example 4"""
        assert maze_bfs(maze4) == 16
        
