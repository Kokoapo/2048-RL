import random

class Game:
    def __init__(self, grid_size):
        self.size = grid_size
        self.reset()

    def reset(self):
        self.grid = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self._gen_number()
        self._gen_number()

    def step(self, dir):
        dx, dy = dir
        reward = 0
        if dx != 0:
            for r in range(self.size):
                new_line = self.grid[r].copy()
                if dx == 1:
                    new_line = new_line[::-1]
                    new_line, new_reward = self._move_line(new_line)
                    new_line = new_line[::-1]
                else:
                    new_line, new_reward = self._move_line(new_line)
                self.grid[r] = new_line.copy()
                reward += new_reward
        elif dy != 0:
            for c in range(self.size):
                new_column = [self.grid[r][c] for r in range(self.size)]
                if dy == 1:
                    new_column = new_column[::-1]
                    new_column, new_reward = self._move_line(new_column)
                    new_column = new_column[::-1]
                else:
                    new_column, new_reward = self._move_line(new_column)
                for r in range(self.size):
                    self.grid[r][c] = new_column[r]
                reward += new_reward

        self._gen_number()
        is_game_over = self._check_fail()
        return reward, is_game_over

    def _gen_number(self):
        while True:
            x = random.randint(0, self.size-1)
            y = random.randint(0, self.size-1)

            if self.grid[x][y] == 0:
                self.grid[x][y] = 2
                break

    def _move_line(self, line):
        nums = [x for x in line if x != 0]
        new_line = []
        i = 0
        reward = 0
        while i < len(nums):
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                new_line.append(nums[i] * 2)
                reward = nums[i] * 2
                i += 2
            else:
                new_line.append(nums[i])
                i += 1
        new_line += [0] * (len(line) - len(new_line))
        return new_line, reward

    def _check_fail(self):
        for line in self.grid:
            if 0 in line:
                return False

        for x in range(self.size):
            for y in range(self.size):
                for i in [-1, 1]:
                    if x+i >= 0 and x+i < self.size:
                        if self.grid[x][y] == self.grid[x+i][y]:
                            return False
                    if y+i >= 0 and y+i < self.size:
                        if self.grid[x][y] == self.grid[x][y+i]:
                            return False
        return True

    def print_grid(self):
        for line in self.grid:
            print(line)

    def get_state(self):
        state = []
        for row in self.grid:
            for num in row:
                state.append(num)
        return state