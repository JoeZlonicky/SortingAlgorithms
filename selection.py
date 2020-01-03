from algorithm import SortingAlgorithm


class SelectionSort(SortingAlgorithm):
    def __init__(self):
        super().__init__("Selection sort", 100, (255, 150, 20))

    def apply_algorithm(self):
        for i in range(len(self.data)):
            smallest = i
            for j in range(i, len(self.data)):
                if self.data[j] < self.data[smallest]:
                    smallest = j
            if smallest != i:
                self.data[smallest], self.data[i] = self.data[i], self.data[smallest]
                self.update_graph()
                self.clock.tick(15)


if __name__ == "__main__":
    SelectionSort().start()
