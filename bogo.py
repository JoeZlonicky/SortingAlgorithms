import random
from algorithm import SortingAlgorithm


class BogoSort(SortingAlgorithm):
    """ Visualize the bogo sort algorithm """
    
    def __init__(self):
        super().__init__("Bogo", 7)

    def apply_algorithm(self):
        """ Randomize data until sorted """
        while not self.is_sorted():
            random.shuffle(self.data)
            self.update_graph()


if __name__ == "__main__":
    BogoSort()
