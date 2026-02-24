from search import astar_search

class DroneAgent:
    def __init__(self, problem):
        self.problem = problem
        solucao = astar_search(self.problem, h=self.problem.h)
        self.plan = solucao.solution() if solucao else []

    def act(self):
        """Retorna uma ação por passo ao ambiente [cite: 43]"""
        if self.plan:
            return self.plan.pop(0)
        return None