import pygame
from pathfinding_visualizer import PathfindingVisualizer
from config import WINDOW_SIZE, GRID_ROWS

def main():
    pygame.init()  # Add this line
    visualizer = PathfindingVisualizer(WINDOW_SIZE, GRID_ROWS)
    running = True

    while running:
        visualizer.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                continue

            # Handle mouse input
            if pygame.mouse.get_pressed()[0]:  # Left click
                visualizer.handle_mouse_click(pygame.mouse.get_pos(), True)
            elif pygame.mouse.get_pressed()[2]:  # Right click
                visualizer.handle_mouse_click(pygame.mouse.get_pos(), False)

            # Handle keyboard input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    visualizer.start_algorithm()
                elif event.key == pygame.K_c:
                    visualizer.reset_grid()

    pygame.quit()

if __name__ == "__main__":
    main()