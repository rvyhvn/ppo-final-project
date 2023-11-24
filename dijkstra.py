from tabulate import tabulate

class Dijkstra:
    def __init__(self, graph):
        self.graph = graph
        self.distance = {}
        self.path = {}
        self.start = ""
        self.end = ""

    def initiate_distance(self, start, end):
        for node in self.graph:
            self.distance[node] = float('inf')
        self.distance[start] = 0
        self.start = start
        self.end = end

    def find_shortest_path(self, notVisited):
        shortest_node = None
        shortest_distance = float('inf')

        for node in notVisited:
            if self.distance[node] < shortest_distance:
                shortest_node = node
                shortest_distance = self.distance[node]

        return shortest_node

    def route(self, start, end):
        self.initiate_distance(start, end)
        notVisited = [node for node in self.distance]
        shortestNode = self.find_shortest_path(notVisited)

        while notVisited:
            currentShortestNodeDistance = self.distance[shortestNode]

            if currentShortestNodeDistance == float('inf'):
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
            print(" -> ".join(pathList))

    def display_result(self):
        distances_table = [["Node", "Shortest Distance from Start"]]
        for node, dist in self.distance.items():
            distances_table.append([node, dist])

        path_table = [["Node", "Predecessor Node"]]
        for node, pred in self.path.items():
            path_table.append([node, pred])

        print("Shortest Distances:")
        print(tabulate(distances_table, headers="firstrow", tablefmt="grid"))
        print("\nShortest Path:")
        print(tabulate(path_table, headers="firstrow", tablefmt="grid"))


