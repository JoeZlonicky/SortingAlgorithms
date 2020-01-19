from algorithm import SortingAlgorithm


class SelectionSort(SortingAlgorithm):
    def __init__(self):
        """ Visualize the selection sort algorithm """
        super().__init__("Selection sort", 100)

    def apply_algorithm(self):
        """ Swap values into order """
        for i in range(len(self.data)):
            smallest = i
            for j in range(i, len(self.data)):
                if self.data[j] < self.data[smallest]:
                    smallest = j
            if smallest != i:
                self.data[smallest], self.data[i] = self.data[i], self.data[smallest]
                self.update_graph()
            self.clock.tick(15)  # Limit FPS so it doesn't finish too fast


if __name__ == "__main__":
    SelectionSort()
