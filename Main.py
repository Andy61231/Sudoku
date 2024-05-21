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