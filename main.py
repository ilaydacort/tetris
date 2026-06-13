import pygame
import sys
import random

CELL_SIZE = 30
COLS = 10
ROWS = 20
WIDTH = COLS * CELL_SIZE + 150
HEIGHT = ROWS * CELL_SIZE
FPS = 60


BG_COLOR = (25, 25, 25)
GRID_COLOR = (40, 40, 40)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()


grid = [[None for _ in range(COLS)] for _ in range(ROWS)]

shapes = {
    "I": [[1, 1, 1, 1]], 
    "O": [[1, 1], [1, 1]],
    "T": [[0, 1, 0], [1, 1, 1]],
    "L": [[1, 0], [1, 0], [1, 1]],
    "J": [[0, 1], [0, 1], [1, 1]],
    "S": [[0, 1, 1], [1, 1, 0]],
    "Z": [[1, 1, 0], [0, 1, 1]]
}


try:
    block_images = {
        "I": pygame.transform.scale(pygame.image.load("assets/blocks/I.png").convert_alpha(), (CELL_SIZE, CELL_SIZE)),
        "O": pygame.transform.scale(pygame.image.load("assets/blocks/kare.png").convert_alpha(), (CELL_SIZE, CELL_SIZE)),
        "T": pygame.transform.scale(pygame.image.load("assets/blocks/L.png").convert_alpha(), (CELL_SIZE, CELL_SIZE)),
        "L": pygame.transform.scale(pygame.image.load("assets/blocks/tersL.png").convert_alpha(), (CELL_SIZE, CELL_SIZE)),
        "J": pygame.transform.scale(pygame.image.load("assets/blocks/tersT.png").convert_alpha(), (CELL_SIZE, CELL_SIZE)),
        "S": pygame.transform.scale(pygame.image.load("assets/blocks/yatay.png").convert_alpha(), (CELL_SIZE, CELL_SIZE)),
        "Z": pygame.transform.scale(pygame.image.load("assets/blocks/z.png").convert_alpha(), (CELL_SIZE, CELL_SIZE))
    }
except:
    
    block_images = {k: pygame.Surface((CELL_SIZE, CELL_SIZE)) for k in shapes.keys()}
    for k, s in block_images.items(): s.fill((random.randint(50,255), random.randint(50,255), random.randint(50,255)))

class Block:
    def __init__(self, key):
        self.key = key
        self.shape = shapes[key]
        self.x = COLS // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        
        new_shape = [list(row) for row in zip(*self.shape[::-1])]
        if not self.check_collision(self.x, self.y, new_shape):
            self.shape = new_shape

    def check_collision(self, nx, ny, shape=None):
        if shape is None: shape = self.shape
        for r, row in enumerate(shape):
            for c, cell in enumerate(row):
                if cell:
                    target_x = nx + c
                    target_y = ny + r
                    
                    if target_x < 0 or target_x >= COLS or target_y >= ROWS:
                        return True
                   
                    if target_y >= 0 and grid[target_y][target_x]:
                        return True
        return False

    def draw(self, surface):
        for r, row in enumerate(self.shape):
            for c, cell in enumerate(row):
                if cell:
                    surface.blit(block_images[self.key], ((self.x + c) * CELL_SIZE, (self.y + r) * CELL_SIZE))

def clear_rows():
    full_rows = 0
    for r in range(ROWS):
        if all(grid[r]):
            del grid[r]
            grid.insert(0, [None for _ in range(COLS)])
            full_rows += 1
    return full_rows

def draw_grid_and_blocks():
    for r in range(ROWS):
        for c in range(COLS):
            rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRID_COLOR, rect, 1)
            if grid[r][c]:
                screen.blit(block_images[grid[r][c]], (c * CELL_SIZE, r * CELL_SIZE))


current_block = Block(random.choice(list(shapes.keys())))
drop_timer = 0
drop_speed = 30 
score = 0
font = pygame.font.SysFont("Arial", 24)

running = True
while running:
    clock.tick(FPS)
    drop_timer += 1
    screen.fill(BG_COLOR)

   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not current_block.check_collision(current_block.x - 1, current_block.y):
                current_block.x -= 1
            if event.key == pygame.K_RIGHT and not current_block.check_collision(current_block.x + 1, current_block.y):
                current_block.x += 1
            if event.key == pygame.K_DOWN and not current_block.check_collision(current_block.x, current_block.y + 1):
                current_block.y += 1
            if event.key == pygame.K_UP:
                current_block.rotate()

   
    if drop_timer >= drop_speed:
        if not current_block.check_collision(current_block.x, current_block.y + 1):
            current_block.y += 1
        else:
           
            for r, row in enumerate(current_block.shape):
                for c, cell in enumerate(row):
                    if cell:
                        if current_block.y + r < 0: 
                            running = False
                        else:
                            grid[current_block.y + r][current_block.x + c] = current_block.key
            
            score += clear_rows() * 100
            current_block = Block(random.choice(list(shapes.keys())))
            
            if current_block.check_collision(current_block.x, current_block.y):
                running = False
        drop_timer = 0

    draw_grid_and_blocks()
    current_block.draw(screen)
    
   
    score_text = font.render(f"Skor: {score}", True, (255, 255, 255))
    screen.blit(score_text, (COLS * CELL_SIZE + 20, 20))

    pygame.display.update()

pygame.quit()
sys.exit()