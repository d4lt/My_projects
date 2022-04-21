import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Cell:
    def __init__(self, row, col, gap, total_rows):
        self.gap = gap
        self.row = row
        self.col = col
        self.x = gap * row
        self.y = gap * col
        self.color = BLACK
        self.total_rows = total_rows
        self.neighbors = 0

    def is_dead(self):
        return self.color == BLACK

    def is_alive(self):
        return self.color == WHITE

    def make_dead(self):
        self.color = BLACK

    def make_alive(self):
        self.color = WHITE

    #check the number of alive neighbors around the Cell
    def update_neighbors(self, grid):
        count = 0

        #UP
        if not self.row - 1 < 0:
            if grid[self.row - 1][self.col].is_alive():
                count += 1
        #DOWN
        if not self.row + 1 > self.total_rows - 1:
            if grid[self.row + 1][self.col].is_alive():
                count += 1
        #LEFT
        if not self.col - 1 < 0:
            if grid[self.row][self.col - 1].is_alive():
                count += 1
        #RIGHT
        if not self.col + 1 > self.total_rows - 1:
            if grid[self.row][self.col + 1].is_alive():
                count += 1
        #UPPERLEFT DIAGONAL
        if not self.row - 1 < 0 and not self.col - 1 < 0:
            if grid[self.row - 1][self.col - 1].is_alive():
                count += 1
        #UPPERRIGHT DIAGONAL
        if not  self.row - 1 < 0 and not self.col + 1 > self.total_rows - 1:
            if grid[self.row - 1][self.col + 1].is_alive():
                count += 1
        #LOWERLEFT DIAGONAL
        if not self.row + 1 > self.total_rows - 1 and not self.col + 1 > self.total_rows - 1:
            if grid[self.row + 1][self.col - 1].is_alive():
                count += 1
        #LOWERRIGHT DIAGONAL
        if not self.row + 1 > self.total_rows - 1 and not self.col + 1 > self.total_rows - 1:
            if grid[self.row + 1][self.col + 1].is_alive():
                count += 1

        self.neighbors = count

    #based on the number of alive neighbors, update the state of the Cell (stay alive, live, die)
    def update_state(self):
        count = self.neighbors

        if count > 3 or count < 2:
            self.make_dead()
        
        if count == 3 and self.is_dead():
            self.make_alive()

    def reset(self):
        self.color = BLACK
        self.neighbors = 0

    def draw(self, win):
        pygame.draw.rect(win, self.color, pygame.Rect(self.x, self.y, self.gap, self.gap))