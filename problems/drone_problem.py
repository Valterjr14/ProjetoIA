from search import Problem

class DroneProblem(Problem):
    def __init__(self, initial, goal, grid):
        super().__init__(initial, goal)
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def actions(self, state):
        x, y = state
        possible_actions = []
        moves = {'UP': (x-1, y), 'DOWN': (x+1, y), 'LEFT': (x, y-1), 'RIGHT': (x, y+1)}

        for action, (nx, ny) in moves.items():
            if 0 <= nx < self.rows and 0 <= ny < self.cols:
                if self.grid[nx][ny] != 'X':
                    possible_actions.append(action)
        return possible_actions

    def result(self, state, action):
        x, y = state
        if action == 'UP': return (x-1, y)
        if action == 'DOWN': return (x+1, y)
        if action == 'LEFT': return (x, y-1)
        if action == 'RIGHT': return (x, y+1)

    def path_cost(self, c, state1, action, state2):
        x, y = state2
        cost = 3 if self.grid[x][y] == 'W' else 1
        return c + cost

    def h(self, node):
        """Heurística: Distância de Manhattan [cite: 145, 146]"""
        x1, y1 = node.state
        x2, y2 = self.goal
        return abs(x1 - x2) + abs(y1 - y2)