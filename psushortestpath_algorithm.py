import csv
import heapq
import time
from math import sin, cos, sqrt, atan2, radians

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # Radius of earth in miles
    R = 3958.8

    # Convert to radians
    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)

    # Differences
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    # Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

class Graph:
    def __init__(self, nodes_file, links_file):
        self.nodes = {}
        self.graph = {}
        self.load_nodes(nodes_file)
        self.load_links(links_file)

    def load_nodes(self, nodes_file):
        with open(nodes_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                node_id = int(row['node_id'])
                lat = float(row['y_coord'])
                lon = float(row['x_coord'])
                self.nodes[node_id] = (lat, lon)
                self.graph[node_id] = []

    def load_links(self, links_file):
        with open(links_file, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                from_node = int(row['from_node_id'])
                to_node = int(row['to_node_id'])
                length = float(row['length'])
                self.graph[from_node].append((to_node, length))

def a_star_search(graph, start, goal):
    """
    A* search algorithm
    """
    frontier = []
    heapq.heappush(frontier, (0, start))  # (f_score, node)
    came_from = {}
    g_score = {node: float('inf') for node in graph.nodes}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph.nodes}
    f_score[start] = haversine_distance(*graph.nodes[start], *graph.nodes[goal])

    while frontier:
        current_f, current = heapq.heappop(frontier)

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, g_score[goal]

        for neighbor, cost in graph.graph[current]:
            tentative_g = g_score[current] + cost
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + haversine_distance(*graph.nodes[neighbor], *graph.nodes[goal])
                heapq.heappush(frontier, (f_score[neighbor], neighbor))

    return None, float('inf')  # No path found

def find_shortest_path(start=1, goal=2):
    """
    Main function to find shortest path
    """
    graph = Graph('Nodes.csv', 'Links.csv')

    if start not in graph.nodes or goal not in graph.nodes:
        return None, None, None

    start_time = time.time()
    path, cost = a_star_search(graph, start, goal)
    end_time = time.time()

    running_time = end_time - start_time

    return path, cost, running_time

if __name__ == "__main__":
    # Default: Node 1 to Node 2
    path, cost, running_time = find_shortest_path()
    if path:
        print(f"Shortest Path: {path}")
        print(f"Total Cost: {cost:.2f} miles")
        print(f"Running Time: {running_time:.4f} seconds")
    else:
        print("No path found")