# Autonomous Vehicle Shortest Path Finder

This project implements an A* algorithm for finding the shortest and most efficient path in autonomous vehicles using geographical data. It employs the f(n) = g(n) + h(n) formula, where h(n) is the heuristic based on Haversine distance.

## Features

- **A* Algorithm Implementation**: Efficient pathfinding with admissible heuristic
- **Geographical Distance Calculation**: Uses Haversine formula for accurate distance computation
- **Interactive Web Interface**: Clean, Apple-style Streamlit application
- **Customizable Start/Goal Nodes**: Select any nodes from the dataset
- **Performance Metrics**: Displays path, total cost, and algorithm running time

## Data Files

- `Nodes.csv`: Contains node information (ID, latitude, longitude)
- `Links.csv`: Contains link information (from/to nodes, length in miles)

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command Line
Run the Python script directly:
```bash
python PSUShortestPath_Algorithm.py
```

### Web Application
Launch the Streamlit app:
```bash
streamlit run PSUShortestPath_App.py
```

Then open your browser to the provided URL.

## Algorithm Details

- **Heuristic (h(n))**: Straight-line distance using Haversine formula
- **Cost (g(n))**: Cumulative link lengths in miles
- **Total Cost (f(n))**: g(n) + h(n)

## Academic Purpose

This software is developed for academic purposes and demonstrates pathfinding concepts. It is not intended for direct integration into vehicle ADAS systems.

## Dependencies

- Python 3.7+
- Streamlit

## License

Academic use only.