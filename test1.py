import unittest
from bfs import bfs
from dfs import dfs

graph = {
    '0': ['2', '3', '4'],
    '1': ['2', '4'],
    '2': ['4'],
    '3': ['4','5'],
    '4': ['5'],
    '5': ['1']
}

class TestGraphTraversal(unittest.TestCase):
    def test_bfs(self):
        expected_output = ['0', '2', '3', '4', '5', '1']   # The expected BFS traversal order

        # Call the BFS function and store the output in bfs_result
        bfs_result = bfs(graph, '0')
        
        # Assert that the bfs_result is equal to the expected_output
        self.assertEqual(bfs_result, expected_output)

    def test_dfs(self):
        expected_output = ['0', '2', '4', '5', '1', '3']   # The expected DFS traversal order

        # Call the DFS function and store the output in dfs_result
        dfs_result = dfs(graph, '0')
        
        # Assert that the dfs_result is equal to the expected_output
        self.assertEqual(dfs_result, expected_output)

if __name__ == '__main__':
    unittest.main()

