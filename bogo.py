import random
from algorithm import SortingAlgorithm


class BogoSort(SortingAlgorithm):
    def __init__(self):
        super().__init__("Bogo", 10, (0, 255, 0))

    def apply_algorithm(self):
        while not self.is_sorted():
            random.shuffle(self.data)
            self.update_graph()


if __name__ == "__main__":
    BogoSort().start()
