import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from problems.drone_problem import DroneProblem

class TestDrone(unittest.TestCase):
    def setUp(self):
        #grid reduzido para teste: . (1), W (3), X (parede)
        self.grid = [
            ['.', 'W'],
            ['X', 'G']
        ]
        self.prob = DroneProblem((0,0), (1,1), self.grid)

    def test_custo_movimentacao_simples(self):
        #simula mover de (0,0) para baixo, mas como tem 'X', 
        #vamos testar o cálculo de custo para uma célula '.'
        #supondo que (0,0) é '.' e o destino fosse '.', custo deve ser 1
        custo = self.prob.path_cost(0, (0,0), 'RIGHT', (0,1))
        #(0,1) no grid de teste é 'W', então deve ser 3
        self.assertEqual(custo, 3)

    def test_verificacao_obstaculo(self):
        #o drone em (0,0) não deve poder ir para baixo ('DOWN') pois tem um 'X' em (1,0)
        acoes_possiveis = self.prob.actions((0,0))
        self.assertNotIn('DOWN', acoes_possiveis)

    def test_heuristica_manhattan(self):
        #testa se a conta |x1-x2| + |y1-y2| está correta
        #de (0,0) para (1,1) a distância é 1 + 1 = 2
        class MockNode:
            def __init__(self, state): self.state = state
        
        node = MockNode((0,0))
        distancia = self.prob.h(node)
        self.assertEqual(distancia, 2)

if __name__ == '__main__':
    unittest.main()