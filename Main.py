import pygame
import sys
import random
from copy import deepcopy

# Inițializarea Pygame
pygame.init()

# Setarea ecranului
width, height = 640, 640
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Exemplu de rezolvare Sudoku cu Pygame')

# Definirea culorilor
white = (255, 255, 255)
black = (0, 0, 0)
button_color = (0, 128, 255)
hover_color = (0, 200, 255)
click_color = (0, 100, 255)
selected_color = (255, 0, 0)
prefilled_color = (200, 200, 200)

# Crearea unui obiect font
font = pygame.font.Font(None, 50)
small_font = pygame.font.Font(None, 36)

# Dimensiunile și pozițiile butoanelor
button_width, button_height = 200, 60
button_padding = 20
center_x = width // 2
center_y = height // 2

# Textele butoanelor
button_texts = ['Usor', 'Mediu', 'Greu']

# Butoanelor dreptunghiulare
buttons = [
    pygame.Rect(center_x - button_width // 2, center_y - (button_height + button_padding) - button_height // 2,button_width, button_height),
    pygame.Rect(center_x - button_width // 2, center_y - button_height // 2, button_width, button_height),
    pygame.Rect(center_x - button_width // 2, center_y + (button_height + button_padding) - button_height // 2,
                button_width, button_height)
]

# Variabile pentru a ține evidența butonului apăsat
usor_pressed = False
mediu_pressed = False
greu_pressed = False

# Dimensiunile grilei
large_square_size = 150
small_square_size = large_square_size // 3

# Variabila pentru a urmări celula selectată
selected_cell = None

# Variabila pentru a urmări celulele precompletate
prefilled_cells = set()

# Funcție pentru a verifica dacă un număr poate fi plasat într-o anumită poziție
def can_place_number(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    block_row = row // 3 * 3
    block_col = col // 3 * 3
    for i in range(3):
        for j in range(3):
            if grid[block_row + i][block_col + j] == num:
                return False
    return True


# Funcție pentru a rezolva grila folosind backtracking
def solve_grid(grid):
    empty = find_empty(grid)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if can_place_number(grid, row, col, num):
            grid[row][col] = num
            if solve_grid(grid):
                return True
            grid[row][col] = 0
    return False


# Funcție pentru a găsi o celulă goală în grilă
def find_empty(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return (row, col)
    return None


# Funcție pentru a genera o grilă Sudoku completă și validă cu randomizare
def generate_full_grid_with_randomization():
    grid = [[0 for _ in range(9)] for _ in range(9)]
    solve_grid(grid)
    randomize_grid(grid)  # Randomizarea grilei
    return grid


# Funcție pentru a crea un puzzle dintr-o grilă completă cu randomizare
def create_puzzle_with_randomization(grid, number_count):
    puzzle = deepcopy(grid)
    cells_removed = 81 - number_count
    while cells_removed > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if puzzle[row][col] != 0:
            backup = puzzle[row][col]
            puzzle[row][col] = 0
            grid_copy = deepcopy(puzzle)
            if solve_grid(grid_copy):
                prefilled_cells.discard((row, col))
                cells_removed -= 1
            else:
                puzzle[row][col] = backup
    return puzzle


# Funcție pentru a randomiza grila prin schimbarea rândurilor și coloanelor în cadrul pătratelor
def randomize_grid(grid):
    for _ in range(random.randint(10, 20)):  # Se efectuează un număr aleatoriu de schimbări
        # Se schimbă rândurile în cadrul pătratelor
        square_row = random.randint(0, 2) * 3
        row1 = square_row + random.randint(0, 2)
        row2 = square_row + random.randint(0, 2)
        grid[row1], grid[row2] = grid[row2], grid[row1]

        # Se schimbă coloanele în cadrul pătratelor
        square_col = random.randint(0, 2) * 3
        col1 = square_col + random.randint(0, 2)
        col2 = square_col + random.randint(0, 2)
        for i in range(9):
            grid[i][col1], grid[i][col2] = grid[i][col2], grid[i][col1]


# Funcție pentru a afișa soluția
def print_solution(grid):
    for row in grid:
        print(row)


# Funcție pentru a verifica dacă grila este completă și corectă
def is_grid_complete_and_correct(grid):
    for row in range(9):
        for col in range(9):
            num = grid[row][col]
            grid[row][col] = 0
            if num == 0 or not can_place_number(grid, row, col, num):
                return False
            grid[row][col] = num
    return True