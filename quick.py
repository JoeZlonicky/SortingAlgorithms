from algorithm import SortingAlgorithm


class QuickSort(SortingAlgorithm):
    def __init__(self):
        super().__init__("Quick sort", 300, (255, 0, 0))

    def apply_algorithm(self):
        self.quick_sort(0, len(self.data) - 1)

    def quick_sort(self, low, high):
        if low < high:
            part = self.partition(low, high)
            self.quick_sort(low, part - 1)
            self.quick_sort(part + 1, high)

    def partition(self, low, high):
        pivot = self.data[high]
        i = low - 1
        for j in range(low, high):
            if self.data[j] <= pivot:
                i += 1
                self.data[i], self.data[j] = self.data[j], self.data[i]
                self.update_graph()
        self.data[i + 1], self.data[high] = self.data[high], self.data[i + 1]
        self.update_graph()
        return i + 1


if __name__ == "__main__":
    QuickSort().start()
