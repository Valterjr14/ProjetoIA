import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from problems.drone_problem import DroneProblem

class TestDrone(unittest.TestCase):
    def setUp(self):
        self.grid = [
            ['.', 'W'],
            ['X', 'G']
        ]
        self.prob = DroneProblem((0,0), (1,1), self.grid)

    def test_custo_movimentacao_simples(self):
        custo = self.prob.path_cost(0, (0,0), 'RIGHT', (0,1))
        self.assertEqual(custo, 3)

    def test_verificacao_obstaculo(self):
        acoes_possiveis = self.prob.actions((0,0))
        self.assertNotIn('DOWN', acoes_possiveis)

    def test_heuristica_manhattan(self):
        class MockNode:
            def __init__(self, state): self.state = state
        
        node = MockNode((0,0))
        distancia = self.prob.h(node)
        self.assertEqual(distancia, 2)

if __name__ == '__main__':
    unittest.main()