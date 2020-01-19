from algorithm import SortingAlgorithm


class InsertionSort(SortingAlgorithm):
    def __init__(self):
        """ Visualize the insertion sort algorithm """
        super().__init__("Insertion sort", 100)

    def apply_algorithm(self):
        """ Insert values into sorted orders """
        for i in range(1, len(self.data)):
            j = i
            value = self.data[i]
            while j > 0 and value < self.data[j - 1]:
                self.data[j] = self.data[j - 1]
                j -= 1
            self.data[j] = value
            self.update_graph()
            self.clock.tick(15)  # Limit FPS so it doesn't finish too fast


if __name__ == "__main__":
    InsertionSort()
