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


if __name__ == '__main__':
    routes = [
        ("Kampala", "Nairobi"),
        ("Kampala", "Dar Es Salaam"),
        ("Entebbe", "Soroti")
    ]

    graph_routes = Graph(routes)
