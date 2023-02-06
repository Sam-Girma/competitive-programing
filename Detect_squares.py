class DetectSquares:

    def __init__(self):
        self.point_counts = defaultdict(lambda: defaultdict(int))

    def add_point(self, xy: List[int]):
        x, y = xy
        self.point_counts[x][y] += 1

    def count_squares(self, xy: List[int]):
        count = 0
        x, y = xy
        for y_val, num in self.point_counts[x].items():
            edge_len = abs(y - y_val)
            if edge_len > 0:
                count += num * self.point_counts[x - edge_len][y_val] * self.point_counts[x - edge_len][y]
                count += num * self.point_counts[x + edge_len][y_val] * self.point_counts[x + edge_len][y]

        return count
