import random
from algorithm import SortingAlgorithm


class BogoSort(SortingAlgorithm):
    def __init__(self):
        """ Visualize the bogo sort algorithm """
        super().__init__("Bogo", 7)

    def apply_algorithm(self):
        """ Randomize data until sorted """
        while not self.is_sorted():
            random.shuffle(self.data)
            self.update_graph()


if __name__ == "__main__":
    BogoSort()
