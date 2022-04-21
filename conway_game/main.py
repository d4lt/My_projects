import pygame
import sys
import grid as grid_
import time
import Cell

pygame.init()

WIDTH = 650
WIN = pygame.display.set_mode((WIDTH,WIDTH))
title = "Conway's game of life."
pygame.display.set_caption(title)
icon = pygame.image.load("./images/forma-de-estrela-negra-de-asterisco.png")
pygame.display.set_icon(icon)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (50, 50, 50)

def get_clicked_pos(pos, width, rows):
    gap = width // rows

    y, x = pos

    row = y//gap
    col = x//gap

    return row, col

def algorithm(grid, main_grid):
    started = True
    while started:

        for row in grid:
            for cell in row:
                cell.update_neighbors(grid)      #* updating neighbors

        for row in grid:
            for cell in row:
                cell.update_state()          #* making the cells dead or alive

        
        finished = True
        for row in grid:
            for cell in row:
                if cell.is_alive():
                    finished = False
                    continue
        if finished:
            started = False
        
        main_grid.draw(grid)


def main(win, width):
    ROWS = 50

    gap = width // ROWS
    main_grid = grid_.Grid(win, ROWS, width, gap)
    started = False
    grid = main_grid.make_grid(Cell.Cell)

    running = True
    while running:
        main_grid.draw(grid)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, width, ROWS)
                cell = grid[row][col]

                if cell.is_dead():
                    cell.make_alive()

            if pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, width, ROWS)
                cell = grid[row][col]

                if cell.is_alive():
                    cell.make_dead()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    algorithm(grid, main_grid)
                
                if event.key == pygame.K_c:
                    for row in grid:
                        for cell in row:
                            cell.reset()



    pygame.quit()

if __name__ == '__main__':
    main(WIN, WIDTH)