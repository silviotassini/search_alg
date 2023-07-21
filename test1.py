import unittest
from parameterized import parameterized
from bfs import bfs
from dfs import dfs

graph0 = {
    '0': ['2', '3', '4'],
    '1': ['2', '4'],
    '2': ['4'],
    '3': ['4','5'],
    '4': ['5'],
    '5': ['1']
}

bfs_expected0 = ['0', '2', '3', '4', '5', '1'] 
dfs_expected0 = ['0', '4', '5', '1', '2', '3']

class TestGraphTraversal(unittest.TestCase):

    @parameterized.expand([
        (graph0, bfs_expected0),     
    ])
    def test_bfs(self, graph, expected_output):
        # Call the BFS function and store the output in bfs_result
        bfs_result = bfs(graph, '0')
        print(bfs_result)
        # Assert that the bfs_result is equal to the expected_output
        self.assertEqual(bfs_result, expected_output)

    @parameterized.expand([
        (graph0, dfs_expected0),     
    ])
    def test_dfs(self, graph, expected_output):
        # Call the DFS function and store the output in dfs_result
        dfs_result = dfs(graph, '0')
        
        # Assert that the dfs_result is equal to the expected_output
        self.assertEqual(dfs_result, expected_output)

if __name__ == '__main__':
    unittest.main()

