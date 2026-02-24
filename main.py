import sys
import os

sys.path.append(os.getcwd())

from env.grid_env import DroneEnvironment
from problems.drone_problem import DroneProblem
from agents.drone_agent import DroneAgent
from search import astar_search
grid = [
    ['.', '.', '.', 'W', 'W'],
    ['.', 'X', '.', 'W', 'W'],
    ['.', '.', 'X', '.', 'G']
]

start = (0, 0)
goal = (2, 4) 

prob = DroneProblem(start, goal, grid)
env = DroneEnvironment(grid, start)
agente = DroneAgent(prob)

solucao = astar_search(prob, h=prob.h)
custo_total = solucao.path_cost if solucao else 0

print("--- INICIANDO SIMULAÇÃO ---")
print(f"O custo total planejado para esta rota é: {custo_total}")
print("-" * 30)

env.render() 

while True:
    acao = agente.act()
    if not acao:
        print(f"Destino alcançado! Energia total gasta: {custo_total}")
        break

    input("Pressione Enter para o próximo movimento...") 
    
    print(f"Executando ação: {acao}")
    env.execute_action(acao)
    env.render()