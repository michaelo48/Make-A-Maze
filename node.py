from typing import List, Tuple
import pygame
from node_state import NodeState
from config import Colors

class Node:
    """A node in the pathfinding grid"""
    def __init__(self, row: int, col: int, size: int):
        self.row = row
        self.col = col
        self.x = row * size
        self.y = col * size
        self.size = size
        self.state = NodeState.EMPTY
        self.neighbors: List['Node'] = []
        
    @property
    def position(self) -> Tuple[int, int]:
        """Get the grid position of the node"""
        return self.row, self.col
    
    def draw(self, window: pygame.Surface) -> None:
        """Draw the node on the window"""
        color = self._get_color_for_state()
        pygame.draw.rect(window, color, (self.x, self.y, self.size, self.size))
    
    def _get_color_for_state(self) -> Tuple[int, int, int]:
        """Map node states to colors"""
        state_colors = {
            NodeState.EMPTY: Colors.WHITE,
            NodeState.BARRIER: Colors.BLACK,
            NodeState.START: Colors.BLUE,
            NodeState.END: Colors.GREY,
            NodeState.PATH: Colors.TURQUOISE,
            NodeState.OPEN: Colors.GREEN,
            NodeState.CLOSED: Colors.RED
        }
        return state_colors[self.state]
    
    def update_neighbors(self, grid: List[List['Node']]) -> None:
        """Update valid neighbors for pathfinding"""
        self.neighbors.clear()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left
        
        for dx, dy in directions:
            new_row, new_col = self.row + dx, self.col + dy
            if self._is_valid_neighbor(new_row, new_col, grid):
                self.neighbors.append(grid[new_row][new_col])
    
    def _is_valid_neighbor(self, row: int, col: int, grid: List[List['Node']]) -> bool:
        """Check if a potential neighbor position is valid"""
        return (0 <= row < len(grid) and 
                0 <= col < len(grid[0]) and 
                grid[row][col].state != NodeState.BARRIER)