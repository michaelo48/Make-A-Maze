import pygame
from typing import Tuple, List, Dict, Set, Optional
from queue import PriorityQueue
from node import Node
from node_state import NodeState
from config import Colors

class PathfindingVisualizer:
    """Main class for the pathfinding visualization"""
    def __init__(self, width: int, rows: int):
        self.width = width
        self.rows = rows
        self.cell_size = width // rows
        self.window = pygame.display.set_mode((width, width))
        pygame.display.set_caption("A* Pathfinding Visualizer")
        self.grid = self._make_grid()
        self.start_node: Optional[Node] = None
        self.end_node: Optional[Node] = None

    def _make_grid(self) -> List[List[Node]]:
        """Create the initial grid of nodes"""
        return [[Node(i, j, self.cell_size) for j in range(self.rows)] 
                for i in range(self.rows)]

    def _draw_grid_lines(self) -> None:
        """Draw the grid lines"""
        for i in range(self.rows):
            pygame.draw.line(self.window, Colors.GREY, 
                           (0, i * self.cell_size), 
                           (self.width, i * self.cell_size))
            pygame.draw.line(self.window, Colors.GREY, 
                           (i * self.cell_size, 0), 
                           (i * self.cell_size, self.width))

    def draw(self) -> None:
        """Draw the complete grid"""
        self.window.fill(Colors.WHITE)
        for row in self.grid:
            for node in row:
                node.draw(self.window)
        self._draw_grid_lines()
        pygame.display.update()

    def _get_clicked_position(self, pos: Tuple[int, int]) -> Tuple[int, int]:
        """Convert mouse position to grid coordinates"""
        x, y = pos
        row = x // self.cell_size
        col = y // self.cell_size
        return row, col

    def handle_mouse_click(self, pos: Tuple[int, int], is_left_click: bool) -> None:
        """Handle mouse input for grid manipulation"""
        row, col = self._get_clicked_position(pos)
        node = self.grid[row][col]

        if is_left_click:
            if not self.start_node and node != self.end_node:
                node.state = NodeState.START
                self.start_node = node
            elif not self.end_node and node != self.start_node:
                node.state = NodeState.END
                self.end_node = node
            elif node not in (self.start_node, self.end_node):
                node.state = NodeState.BARRIER
        else:  # Right click
            if node == self.start_node:
                self.start_node = None
            elif node == self.end_node:
                self.end_node = None
            node.state = NodeState.EMPTY

    def reset_grid(self) -> None:
        """Reset the grid to initial state"""
        self.grid = self._make_grid()
        self.start_node = None
        self.end_node = None

    @staticmethod
    def _manhattan_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
        """Calculate Manhattan distance between two points"""
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)

    def _reconstruct_path(self, came_from: Dict[Node, Node], current: Node) -> None:
        """Reconstruct and visualize the found path"""
        while current in came_from:
            current = came_from[current]
            if current not in (self.start_node, self.end_node):
                current.state = NodeState.PATH
            self.draw()

    def clear_search_data(self) -> None:
        """Clear previous search visualization data but keep barriers and start/end nodes"""
        for row in self.grid:
            for node in row:
                if node.state in {NodeState.OPEN, NodeState.CLOSED, NodeState.PATH}:
                    node.state = NodeState.EMPTY

    def start_algorithm(self) -> bool:
        """Initialize and run the A* pathfinding algorithm"""
        if not (self.start_node and self.end_node):
            return False

        # Clear previous search data
        self.clear_search_data()
        
        # Update neighbors before starting
        for row in self.grid:
            for node in row:
                node.update_neighbors(self.grid)

        return self._a_star_algorithm()

    def _a_star_algorithm(self) -> bool:
        """A* pathfinding algorithm implementation"""
        count = 0
        open_set = PriorityQueue()
        open_set.put((0, count, self.start_node))
        came_from: Dict[Node, Node] = {}
        
        g_score = {node: float('inf') for row in self.grid for node in row}
        g_score[self.start_node] = 0
        
        f_score = {node: float('inf') for row in self.grid for node in row}
        f_score[self.start_node] = self._manhattan_distance(
            self.start_node.position, self.end_node.position)

        open_set_hash = {self.start_node}

        while not open_set.empty():
            current = open_set.get()[2]
            open_set_hash.remove(current)

            if current == self.end_node:
                self._reconstruct_path(came_from, self.end_node)
                return True

            for neighbor in current.neighbors:
                temp_g_score = g_score[current] + 1

                if temp_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor] = temp_g_score + self._manhattan_distance(
                        neighbor.position, self.end_node.position)
                    
                    if neighbor not in open_set_hash:
                        count += 1
                        open_set.put((f_score[neighbor], count, neighbor))
                        open_set_hash.add(neighbor)
                        if neighbor != self.end_node:
                            neighbor.state = NodeState.OPEN

            self.draw()

            if current != self.start_node:
                current.state = NodeState.CLOSED

        return False

__all__ = ['PathfindingVisualizer']

if __name__ != '__main__':
    PathfindingVisualizer = PathfindingVisualizer