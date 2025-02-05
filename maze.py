import pygame
import math
from queue import PriorityQueue

# Set up display
WIDTH = 600
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Pathfinding Visualizer")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

# Define grid constants
ROWS = 30
COLS = 30
GRID_SIZE = WIDTH // ROWS

# Node class to represent each square in the grid
class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = row * GRID_SIZE
        self.y = col * GRID_SIZE
        self.color = WHITE
        self.neighbors = []
    
    def get_pos(self):
        return self.row, self.col
    
    def is_closed(self):
        return self.color == RED
    
    def is_open(self):
        return self.color == GREEN
    
    def is_barrier(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == BLUE
    
    def is_end(self):
        return self.color == GREY
    
    def reset(self):
        self.color = WHITE
    
    def make_closed(self):
        self.color = RED
    
    def make_open(self):
        self.color = GREEN
    
    def make_barrier(self):
        self.color = BLACK
    
    def make_start(self):
        self.color = BLUE
    
    def make_end(self):
        self.color = GREY
    
    def make_path(self):
        self.color = (64, 224, 208)  # Turquoise
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, GRID_SIZE, GRID_SIZE))
    
    def update_neighbors(self, grid):
        self.neighbors = []
        # Check adjacent squares (up, down, left, right)
        if self.row < ROWS - 1 and not grid[self.row + 1][self.col].is_barrier(): # Down
            self.neighbors.append(grid[self.row + 1][self.col])
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # Up
            self.neighbors.append(grid[self.row - 1][self.col])
        if self.col < COLS - 1 and not grid[self.row][self.col + 1].is_barrier(): # Right
            self.neighbors.append(grid[self.row][self.col + 1])
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # Left
            self.neighbors.append(grid[self.row][self.col - 1])

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()

def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0
    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = h(start.get_pos(), end.get_pos())
    
    open_set_hash = {start}
    
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        current = open_set.get()[2]
        open_set_hash.remove(current)
        
        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True
        
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1
            
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        
        draw()
        
        if current != start:
            current.make_closed()
    
    return False

def make_grid(rows, cols):
    grid = []
    for i in range(rows):
        grid.append([])
        for j in range(cols):
            node = Node(i, j)
            grid[i].append(node)
    return grid

def draw_grid(win):
    for i in range(ROWS):
        pygame.draw.line(win, GREY, (0, i * GRID_SIZE), (WIDTH, i * GRID_SIZE))
        for j in range(COLS):
            pygame.draw.line(win, GREY, (j * GRID_SIZE, 0), (j * GRID_SIZE, WIDTH))

def draw(win, grid):
    win.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(win)
    draw_grid(win)
    pygame.display.update()

def get_clicked_pos(pos):
    x, y = pos
    row = x // GRID_SIZE
    col = y // GRID_SIZE
    return row, col

def handle_left_click(pos, grid, start, end):
    """Handle left mouse button click events"""
    row, col = get_clicked_pos(pos)
    node = grid[row][col]
    
    if not start and node != end:
        node.make_start()
        return node, end
    elif not end and node != start:
        node.make_end()
        return start, node
    elif node != end and node != start:
        node.make_barrier()
    
    return start, end

def handle_right_click(pos, grid, start, end):
    """Handle right mouse button click events"""
    row, col = get_clicked_pos(pos)
    node = grid[row][col]
    node.reset()
    
    if node == start:
        return None, end
    elif node == end:
        return start, None
    
    return start, end

def update_grid_neighbors(grid):
    """Update neighbors for all nodes in the grid"""
    for row in grid:
        for node in row:
            node.update_neighbors(grid)

def start_pathfinding(grid, start, end, draw_func):
    """Initialize and start the pathfinding algorithm"""
    if not (start and end):
        return
        
    update_grid_neighbors(grid)
    algorithm(draw_func, grid, start, end)

def main(win):
    """Main game loop with improved organization"""
    grid = make_grid(ROWS, COLS)
    start = None
    end = None
    
    running = True
    while running:
        draw(win, grid)
        
        for event in pygame.event.get():
            # Handle quit event
            if event.type == pygame.QUIT:
                running = False
                continue
                
            # Handle mouse input
            if pygame.mouse.get_pressed()[0]:  # Left click
                pos = pygame.mouse.get_pos()
                start, end = handle_left_click(pos, grid, start, end)
                
            elif pygame.mouse.get_pressed()[2]:  # Right click
                pos = pygame.mouse.get_pos()
                start, end = handle_right_click(pos, grid, start, end)
            
            # Handle keyboard input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_pathfinding(grid, start, end, lambda: draw(win, grid))
                    
                elif event.key == pygame.K_c:  # Add clear functionality
                    start = None
                    end = None
                    grid = make_grid(ROWS, COLS)
    
    pygame.quit()

main(WIN)
