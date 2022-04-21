import pygame

BLACK = (0, 0, 0)
GREY = (50, 50, 50)


class Grid():
    def __init__(self, win, rows, width, gap):
        self.win = win
        self.rows = rows
        self.width = width
        self.gap = gap

    def make_grid(self, Cell_class):  # an 2D array to represents the cells in the grid
        
        grid = []

        for i in range(self.rows):
            grid.append([])
            for j in range(self.rows):
                cell = Cell_class(i, j, self.gap, self.rows)
                grid[i].append(cell)

        return grid


    def draw_grid(self):                # draw the actual and visible grid on the plane
        gap = self.width // self.rows

        #draw horizontal lines
        for i in range(self.rows):
            pygame.draw.line(self.win, GREY, (0, gap * i), (self.width, gap * i))

        #draw vertical lines
        for j in range(self.rows):
            pygame.draw.line(self.win, GREY, (gap * j, 0), (gap * j, self.width))

    def draw(self, grid):
        # self.win.fill(BLACK)

        for row in grid:
            for cell in row:
                cell.draw(self.win)
        
        self.draw_grid()
        pygame.display.update()