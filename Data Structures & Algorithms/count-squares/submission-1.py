class CountSquares:

    def __init__(self):
        self.pointsCount = defaultdict(int)
        self.points = []

    # O(1)
    def add(self, point: List[int]) -> None:
        self.pointsCount[tuple(point)] += 1
        self.points.append(point)

    # O(n)
    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.points:
            # not square if w and h diff distance or same coord
            if abs(py - y) != abs(px - x) or x == px or y == py:
                continue
            # ways to create a perfect square
            # both of the points below need to exist
            res += self.pointsCount[(x, py)] * self.pointsCount[(px, y)]
        return res
