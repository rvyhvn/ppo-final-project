from tabulate import tabulate
import networkx as nx
import matplotlib.pyplot as plt


class Dijkstra:
    def __init__(self, graph):
        self.graph = graph
        self.distance = {}
        self.path = {}
        self.start = ""
        self.end = ""

    def initiate_distance(self, start, end):
        for node in self.graph:
            self.distance[node] = float("inf")
        self.distance[start] = 0
        self.start = start
        self.end = end

    def find_shortest_path(self, notVisited):
        shortest_node = None
        shortest_distance = float("inf")

        for node in notVisited:
            if self.distance[node] < shortest_distance:
                shortest_node = node
                shortest_distance = self.distance[node]

        return shortest_node

    def visualize_graph(self):
        G = nx.DiGraph()
        G.add_nodes_from(self.graph.keys())

        for node, neighbors in self.graph.items():
            for neighbor, weight in neighbors.items():
                G.add_edge(node, neighbor, weight=weight)

        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')

        nx.draw(G, pos, with_labels=True, node_size=500,
                node_color='skyblue', font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.title("Graph Visualization")
        plt.show()

    def route(self, start, end):
        self.initiate_distance(start, end)
        notVisited = [node for node in self.distance]
        shortestNode = self.find_shortest_path(notVisited)

        while notVisited:
            currentShortestNodeDistance = self.distance[shortestNode]

            if currentShortestNodeDistance == float("inf"):
                break

            for neighbor, weight in self.graph[shortestNode].items():
                distance_to_neighbor = currentShortestNodeDistance + weight
                if distance_to_neighbor < self.distance[neighbor]:
                    self.distance[neighbor] = distance_to_neighbor
                    self.path[neighbor] = shortestNode

            notVisited.remove(shortestNode)
            shortestNode = self.find_shortest_path(notVisited)

        if self.distance[self.end] < float("inf"):
            pathList = [self.end]
            i = 0
            while self.start not in pathList:
                pathList.append(self.path[pathList[i]])
                i += 1

            pathList.reverse()
            print("Shortest Path:", " -> ".join(pathList))

        self.visualize_graph()

    def display_result(self):
        # Prepare the headers for the table
        nodes = list(self.graph.keys())
        edges_table = [[""] + nodes]  # Header row

        # Fill the edges table with weights
        for node in nodes:
            row = [node]
            for neighbor in nodes:
                if neighbor in self.graph[node]:
                    row.append(self.graph[node][neighbor])
                else:
                    row.append("-")  # No edge between nodes
            edges_table.append(row)

        print("Edges with Weights:")
        print(tabulate(edges_table, headers="firstrow", tablefmt="grid"))
