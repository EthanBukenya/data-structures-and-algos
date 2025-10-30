class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

        print("graph routes : ", self.graph_dict)

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shortest_route(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_route(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path


if __name__ == '__main__':
    routes = [
        ("Kampala", "Nairobi"),
        ("Kampala", "Dodoma"),
        ("Nairobi", "Dar Es Salaam"),
        ("Kampala", "Dar Es Salaam")
    ]

    graph_routes = Graph(routes)
    start = "Kampala", end = "Dar Es Salaam"

    print(f"graph routes between {start} and {end} are : ",
          graph_routes.get_paths(start, end))

    print(f"shortest routes between {start} and {end} are : ",
          graph_routes.get_shortest_route(start, end))
