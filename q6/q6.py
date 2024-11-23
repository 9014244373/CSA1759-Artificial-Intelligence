import random

# Define the environment
class Environment:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]  # 0: clean, 1: dirty

    def display(self):
        print("Environment:")
        for row in self.grid:
            print(" ".join("D" if cell else "C" for cell in row))
        print()

# Define the Vacuum Cleaner
class VacuumCleaner:
    def __init__(self, env, start_row=0, start_col=0):
        self.env = env
        self.row = start_row
        self.col = start_col
        self.cleaned_cells = 0

    def clean(self):
        if self.env.grid[self.row][self.col] == 1:
            print(f"Cleaning cell ({self.row}, {self.col})")
            self.env.grid[self.row][self.col] = 0
            self.cleaned_cells += 1

    def move(self):
        # Move to the next cell
        if self.col < self.env.cols - 1:
            self.col += 1
        elif self.row < self.env.rows - 1:
            self.col = 0
            self.row += 1
        else:
            print("Finished cleaning the environment.")

    def run(self):
        print("Starting vacuum cleaner...")
        while True:
            self.env.display()
            self.clean()
            prev_row, prev_col = self.row, self.col
            self.move()
            if (prev_row, prev_col) == (self.row, self.col):  # No more moves
                break

        print(f"Cleaning complete. Total cells cleaned: {self.cleaned_cells}")
        self.env.display()

# Simulation
rows, cols = 4, 4  # Grid size
environment = Environment(rows, cols)
vacuum = VacuumCleaner(environment)
vacuum.run()
