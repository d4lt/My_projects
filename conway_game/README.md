Hello

This is my try at Conway's game of life with pygame.
Its an interesting challenge

BRIEF TO THE GAME:
    its an algorithm that display multiples independent cells 
    which will live to the next generation or dies based on 3 main rules
    
    1. EVERY LIVING CELL WITH MRE THAN 3 NEIGHBORS (including diagonals) WILL DIE AS FOR OVERPOPULATION

    2. LIVING CELL WITH LESS THAN 2 NEIGHBORS WILL DIE AS FOR EXTINCTION

    3. EVERY DEAD CELL WITH EXACTLY 3 NEIGHBORS WILL LIVE


besides its 3 simple rules, the game creates beautiful patterns  

TO USE:
    -press LEFT MOUSE button to put cells
    -RIGHT MOUSE to delete
    -hold SPACE to go forward on the generations
    -press C to clean the grid


STRUCTURE THAT I USED:

                                    GRID
                  DRAW_GRID FUNC __|    |__MAKE_GRID FUNC
          (the visual lines of              (actual 2D ARRAY representing 
           the grid)                         row/columns with each cell represented as a class object)