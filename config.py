from dataclasses import dataclass
from typing import Tuple

@dataclass
class Colors:
    """Color constants for visualization"""
    WHITE: Tuple[int, int, int] = (255, 255, 255)
    BLACK: Tuple[int, int, int] = (0, 0, 0)
    RED: Tuple[int, int, int] = (255, 0, 0)
    GREEN: Tuple[int, int, int] = (0, 255, 0)
    BLUE: Tuple[int, int, int] = (0, 0, 255)
    GREY: Tuple[int, int, int] = (128, 128, 128)
    TURQUOISE: Tuple[int, int, int] = (64, 224, 208)

# Window configuration
WINDOW_SIZE = 800
GRID_ROWS = 40