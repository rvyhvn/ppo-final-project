# Import library yang diperlukan
from tabulate import tabulate
import networkx as nx
import matplotlib.pyplot as plt

# Definisikan kelas Dijkstra
class Dijkstra:
    def __init__(self, graph):
        # Inisialisasi atribut kelas
        self.graph = graph
        self.distance = {}
        self.path = {}
        self.start = ""
        self.end = ""

    def initiate_distance(self, start, end):
        # Inisialisasi jarak awal ke setiap node
        for node in self.graph:
            self.distance[node] = float("inf")
        self.distance[start] = 0
        self.start = start
        self.end = end

    def find_shortest_path(self, notVisited):
        # Temukan node dengan jarak terpendek
        shortest_node = None
        shortest_distance = float("inf")

        for node in notVisited:
            if self.distance[node] < shortest_distance:
                shortest_node = node
                shortest_distance = self.distance[node]

        return shortest_node

    def visualize_graph(self):
        # Buat objek graph menggunakan NetworkX
        G = nx.DiGraph()
        G.add_nodes_from(self.graph.keys())

        # Tambahkan edge dengan bobot ke objek graph
        for node, neighbors in self.graph.items():
            for neighbor, weight in neighbors.items():
                G.add_edge(node, neighbor, weight=weight)

        # Tentukan posisi masing-masing node
        custom_positions = {
            'V1': (0, 0),
            'V2': (1, 1),
            'V3': (1, 0),
            'V4': (1, -1),
            'V5': (3, 1),
            'V6': (3, 0),
            'V7': (3, -1),
            'V8': (4, 0),
        }

        pos = custom_positions  
        labels = nx.get_edge_attributes(G, 'weight')

        # Tentukan warna masing-masing node
        node_colors = ['#d3d3d3', '#ffffe0', '#90ee90', '#9370db', '#d3d3d3', '#d3d3d3', '#ffffe0', '#FFB6C1']
        
        # Tentukan ukuran node
        node_sizes = [1500 for _ in G.nodes()]  

        # Tentukan warna tepi (edge color) node
        node_edge_colors = ['black' for _ in G.nodes()]

        # Tentukan warna edge
        edge_colors = ['black' for _ in G.edges()]

        # Jika terdapat jalur terpendek, tandai edge dengan warna merah
        if self.distance[self.end] < float("inf"):
            pathList = [self.end]
            i = 0
            while self.start not in pathList:
                pathList.append(self.path[pathList[i]])
                i += 1

            pathList.reverse()

            for i in range(len(pathList) - 1):
                if G.has_edge(pathList[i], pathList[i+1]):
                    edge_colors[list(G.edges()).index((pathList[i], pathList[i+1]))] = 'red'

        # Visualisasi graph menggunakan Matplotlib
        nx.draw(G, pos, with_labels=True, node_size=node_sizes, edge_color=edge_colors,
                node_color=node_colors, edgecolors=node_edge_colors, linewidths=2.0)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.title("Graph Visualization")
        plt.show()

    def route(self, start, end):
        # Menambahkan print nilai titik awal dan titik akhir
        print("Starting Point:", start)
        print("End Point:", end)
        
        # Inisialisasi jarak dan path
        self.initiate_distance(start, end)
        notVisited = [node for node in self.distance]
        shortestNode = self.find_shortest_path(notVisited)

        # Dapatkan lintasan terpendek
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

        # Jika terdapat jalur terpendek, print lintasan dan visualisasikan graph
        if self.distance[self.end] < float("inf"):
            pathList = [self.end]
            i = 0
            while self.start not in pathList:
                pathList.append(self.path[pathList[i]])
                i += 1

            pathList.reverse()
            print("Shortest Path:", " -> ".join(pathList))

        self.visualize_graph()

    def route_all_nodes(self, start):
        # Menambahkan print nilai titik awal
        print("\nStarting Point:", start)
        
        # Inisialisasi jarak dan path
        self.initiate_distance(start, "")
        notVisited = [node for node in self.distance]
        shortestNode = self.find_shortest_path(notVisited)

        # Dapatkan lintasan terpendek ke semua node
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

        # Print lintasan terpendek ke semua node
        for node in self.distance:
            if self.distance[node] < float("inf"):
                pathList = [node]
                i = 0
                while start not in pathList:
                    pathList.append(self.path[pathList[i]])
                    i += 1
                pathList.reverse()
                print(f"Shortest Path to {node}:", " -> ".join(pathList))

    def display_result(self):
        # Persiapkan header untuk tabel
        nodes = list(self.graph.keys())
        edges_table = [[""] + nodes]  # Baris header

        # Isi tabel dengan bobot edge
        for node in nodes:
            row = [node]
            for neighbor in nodes:
                if neighbor in self.graph[node]:
                    row.append(self.graph[node][neighbor])
                else:
                    row.append("-")  # Tidak ada edge antar node
            edges_table.append(row)

        # Print tabel
        print("Edges with Weights:")
        print(tabulate(edges_table, headers="firstrow", tablefmt="grid"))

print("Dijkstra_Kelompok 4 & 7_PPO B")

# Definisikan node v dan jaraknya
graph = {
    'V1': {'V2': 4, 'V3': 6, 'V4': 2},
    'V2': {'V3': 3, 'V5': 3},
    'V3': {'V6': 2, 'V7': 1},
    'V4': {'V3': 2, 'V7': 5},
    'V5': {'V6': 2, 'V8': 3},
    'V6': {'V8': 3},
    'V7': {'V8': 3},
    'V8': {},
}

# Buat objek dari kelas Dijkstra
dijkstra = Dijkstra(graph)

# Tentukan titik awal dan titik akhir untuk pencarian lintasan terpendek
start_point = 'V1'
end_point = 'V8'

# Cari lintasan terpendek dari titik awal ke titik akhir
dijkstra.route(start_point, end_point)

# Mencari lintasan terpendek dari 'V1' ke semua node lainnya
dijkstra.route_all_nodes(start_point)