import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.screen = 0

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        self.screen = screen
        for j in range(0, self.height * self.cell_size, self.cell_size):
            for i in range(0, self.width * self.cell_size, self.cell_size):
                pygame.draw.rect(screen, (255, 255, 255),
                                 (i + self.left, j + self.top, self.cell_size, self.cell_size), 1)

    def get_cell(self, mouse_pos):
        if mouse_pos[0] in range(self.left, self.width * self.cell_size + self.left) and\
                mouse_pos[1] in range(self.top, self.height * self.cell_size + self.top):
            return (mouse_pos[0] - self.left) // self.cell_size, (mouse_pos[1] - self.top) // self.cell_size
        else:
            return None

    def on_click(self, cell_coords):
        for i in range(self.width):
           pygame.draw.rect(self.screen, (255 - ))

    def get_click(self, mouse_pos):
        self.on_click(self.get_cell(mouse_pos))


pygame.init()
size = wigth, height = 800, 500
screen = pygame.display.set_mode(size)
board = Board(5, 7)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
