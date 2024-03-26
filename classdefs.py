class Vertex:
    def __init__(self) -> None:
        self.coord = [0,0]
        self.agents = list()
        self.neighbours = list()
    def __lt__(self, other):
        return self.coord[0] < other.coord[0]
        