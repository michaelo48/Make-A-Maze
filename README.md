# A* Pathfinding Algorithm Visualizer

A Python-based visualization tool for the A* pathfinding algorithm using Pygame. This application provides an interactive grid where users can place start points, end points, and barriers to visualize how the A* algorithm finds the shortest path.

## Features

- Interactive grid system
- Real-time visualization of the A* pathfinding algorithm
- Place start point, end point, and barriers
- Clear visualization
- Reset functionality
- Efficient pathfinding with Manhattan distance heuristic

## Prerequisites

Before running this application, make sure you have the following installed:
- Python 3.x
- Pygame

You can install Pygame using pip:
```bash
pip install pygame
```

## Project Structure

```
Make-A-Maze/
├── __init__.py
├── main.py                     # Main entry point
├── pathfinding_visualizer.py   # Core visualization logic
├── node.py                     # Node class definition
├── node_state.py              # Node state enums
└── config.py                  # Configuration settings
```

## Usage

1. Run the application:
```bash
python main.py
```

2. Controls:
   - Left Click: Place nodes in this order:
     1. First click places the start point (blue)
     2. Second click places the end point (grey)
     3. Subsequent clicks place barriers (black)
   - Right Click: Remove nodes
   - Spacebar: Start the pathfinding algorithm
   - 'C' key: Clear the grid

3. Visualization Colors:
   - White: Empty cells
   - Blue: Start point
   - Grey: End point
   - Black: Barriers
   - Green: Open set (nodes to be evaluated)
   - Red: Closed set (evaluated nodes)
   - Turquoise: Final path

## How It Works

The A* algorithm works by maintaining two sets of nodes:
1. Open Set: Nodes that need to be evaluated
2. Closed Set: Nodes that have been evaluated

The algorithm uses the Manhattan distance heuristic to estimate the distance between any node and the end point. It combines this with the known distance from the start to find the most promising path to explore.

Each node's priority is calculated using:
```
f_score = g_score + h_score
```
Where:
- g_score: Cost from start to current node
- h_score: Estimated cost from current node to end (Manhattan distance)

## Contributing

Feel free to fork this project and submit pull requests. You can also open issues for bugs or feature requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Based on the A* pathfinding algorithm
- Built using Pygame for visualization
- Inspired by various pathfinding visualizers and educational tools

## Future Improvements

- Add diagonal movement option
- Implement different heuristics
- Add maze generation algorithms
- Support for weighted paths
- Add animation speed control
- Save/load grid configurations
