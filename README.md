# A* Pathfinding Visualizer

A Python-based visualization tool that demonstrates the A* pathfinding algorithm using Pygame. This interactive application allows users to create obstacles, set start and end points, and watch the algorithm find the shortest path in real-time.

## Features

- Interactive grid-based visualization
- Real-time pathfinding demonstration
- Custom obstacle placement
- Color-coded visualization of:
  - Start point (Blue)
  - End point (Grey)
  - Obstacles (Black)
  - Explored nodes (Red)
  - Frontier nodes (Green)
  - Final path (Turquoise)

## Requirements

- Python 3.x
- Pygame library

## Installation

1. Ensure Python 3.x is installed on your system
2. Install Pygame using pip:
```bash
pip install pygame
```

## Usage

1. Run the program:
```bash
python pathfinding_visualizer.py
```

2. Using the visualizer:
   - Left-click to:
     1. Place the start point (first click)
     2. Place the end point (second click)
     3. Create obstacles (subsequent clicks)
   - Right-click to erase any point
   - Press SPACE to start the pathfinding algorithm once start and end points are placed

## How It Works

The visualizer implements the A* pathfinding algorithm, which:
1. Uses a heuristic function (Manhattan distance) to estimate the distance to the goal
2. Explores nodes based on both the current path cost and estimated remaining distance
3. Guarantees the shortest path when found
4. Visualizes the exploration process in real-time

## Color Guide

- White: Unexplored nodes
- Blue: Start point
- Grey: End point
- Black: Obstacles/Walls
- Green: Nodes in the open set (frontier)
- Red: Explored nodes
- Turquoise: Final path

## Controls

- Left Mouse Button: Place points/obstacles
- Right Mouse Button: Erase points/obstacles
- Spacebar: Start algorithm
- Close Window: Exit program

## Technical Details

- Grid Size: 40x40
- Window Size: 800x800 pixels
- Uses Priority Queue for efficient node selection
- Implements Manhattan distance heuristic
- Supports four-directional movement (up, down, left, right)

## Notes

- The algorithm will only start when both start and end points are placed
- Obstacles can be placed before or after placing start/end points
- The visualization can be reset by closing and reopening the program
