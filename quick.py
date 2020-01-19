from algorithm import SortingAlgorithm


class QuickSort(SortingAlgorithm):
    def __init__(self):
        """ Visualize the quick sort algorithm """
        super().__init__("Quick sort", 100)

    def apply_algorithm(self):
        """ Begin the recursive calls to quick_sort """
        self.quick_sort(0, len(self.data) - 1)

    def quick_sort(self, low, high):
        """ Partition the segment into two and sort them seperately """
        if low < high:
            part = self.partition(low, high)
            self.quick_sort(low, part - 1)
            self.quick_sort(part + 1, high)
            self.clock.tick(15)  # Limit FPS so it doesn't finish too fast

    def partition(self, low, high):
        """ Sort the values so the pivot has all lower values to the left and all higher values to the right """
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
    QuickSort()
