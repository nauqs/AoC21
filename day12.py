from utils import get_input
from collections import defaultdict

paths = []

def part1(data):
    global paths
    for destination in graph['start']:
        get_path(graph, destination, ['start'].copy())
    return len(paths)

def get_path(graph, node, path):
    global paths
    if node == 'end':
        path.append(node)
        paths.append(path)
    elif not node.islower() or node not in path and node != 'start':
        path.append(node)
        for destination in graph[node]:
            get_path(graph, destination, path.copy())

def part2(data):
    global paths
    for destination in graph['start']:
        get_path_2(graph, destination, ['start'].copy(), False)
    paths_str = [",".join(path) for path in paths]
    return len(set(paths_str)) #remove repeated paths

def get_path_2(graph, node, path, repeated):
    global paths
    if node == 'end':
        path.append(node)
        paths.append(path)
    elif node != 'start':
        if not repeated or not node.islower() or node not in path:
            if node.islower() and node in path:
                repeated = True
            path.append(node)
            for destination in graph[node]:
                get_path_2(graph, destination, path.copy(), repeated)

if __name__ == "__main__":
    day = 12
    data = get_input(day)
    
    graph = defaultdict(list)
    for edge in data:
        origin, destination = edge.split('-')
        graph[origin].append(destination)
        graph[destination].append(origin)

    print(part1(graph.copy()))
    print(part2(graph.copy()))

