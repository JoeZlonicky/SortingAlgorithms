from algorithm import SortingAlgorithm


class BubbleSort(SortingAlgorithm):
    def __init__(self):
        super().__init__("Bubble sort", 100, (0, 255, 255))

    def apply_algorithm(self):
        while not self.is_sorted():
            for x in range(len(self.data) - 1):
                if self.data[x] > self.data[x + 1]:
                    self.data[x], self.data[x+1] = self.data[x+1], self.data[x]
                    self.update_graph()


if __name__ == "__main__":
    BubbleSort().start()
