from algorithm import SortingAlgorithm


class InsertionSort(SortingAlgorithm):
    def __init__(self):
        super().__init__("Insertion sort", 300, (255, 255, 0))

    def apply_algorithm(self):
        for i in range(1, len(self.data)):
            j = i
            value = self.data[i]
            while j > 0 and value < self.data[j - 1]:
                self.data[j] = self.data[j - 1]
                j -= 1
            self.data[j] = value
            self.update_graph()


if __name__ == "__main__":
    InsertionSort().start()
