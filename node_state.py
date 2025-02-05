from enum import Enum, auto

class NodeState(Enum):
    """Enum for different states a node can be in"""
    EMPTY = auto()
    BARRIER = auto()
    START = auto()
    END = auto()
    PATH = auto()
    OPEN = auto()
    CLOSED = auto()