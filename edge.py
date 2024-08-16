class Edge:
    def __init__(self, v1, v2):
        if not isinstance(v1, int) or not isinstance(v2, int):
            raise TypeError("given vertices must be integers")
        if v1 < 1 or v2 < 1:
            raise ValueError("given vertices must be integers of 1 or more")

        self.unordered = {v1, v2}
        if v1 > v2:
            v1, v2 = v2, v1
        self.ordered = (v1, v2)

    def __iter__(self):
        for v in self.ordered:
            yield v

    def __eq__(self, other):
        if not isinstance(other, Edge):
            raise TypeError("given argument must be of type Edge")
        return self.unordered == other.unordered

    def __repr__(self):
        return str(self.unordered)

    def __contains__(self, v):
        return v in self.unordered

    def __hash__(self):
        return hash(self.ordered)

    def get_endpoint(self):
        """Returns a vertex incident with the edge."""
        return self.ordered[0]

    def get_adjacent(self, v):
        """Returns the other vertex incident with the edge."""
        if v not in self:
            raise ValueError(f"edge {self} does not contain vertex {v}")
        if self.ordered[0] == v:
            return self.ordered[1]
        return self.ordered[0]
