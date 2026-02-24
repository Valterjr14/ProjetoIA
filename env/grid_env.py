class DroneEnvironment:
    def __init__(self, grid, initial_state):
        self.grid = grid
        self.drone_pos = initial_state

    def execute_action(self, action):
        x, y = self.drone_pos
        if action == 'UP': self.drone_pos = (x-1, y)
        elif action == 'DOWN': self.drone_pos = (x+1, y)
        elif action == 'LEFT': self.drone_pos = (x, y-1)
        elif action == 'RIGHT': self.drone_pos = (x, y+1)

    def render(self):
        for r, row in enumerate(self.grid):
            line = ""
            for c, cell in enumerate(row):
                if (r, c) == self.drone_pos: line += " 🚁 "
                elif cell == 'X': line += " ██ "
                elif cell == 'W': line += " ~~ "
                elif cell == 'G': line += " 🏁 "
                else: line += " .. "
            print(line)
        print("-" * 20)