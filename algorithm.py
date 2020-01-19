import pygame
import random


class SortingAlgorithm:
    """ Use as a base to visual different sorting algorithms, just call update_graph when needed """
    SCREEN_SIZE = (1280, 720)
    MIN_VALUE = 0
    MAX_VALUE = 2000
    BACKGROUND_COLOR = (0, 0, 0)

    def __init__(self, title, data_size):
        """ Start the algorithm on a randomly generated set of data """
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        pygame.display.set_icon(pygame.image.load("icon.png").convert_alpha())
        pygame.display.set_caption(title)
        self.data = [random.randrange(self.MIN_VALUE, self.MAX_VALUE + 1) for _ in range(data_size)]
        self.graph = Graph(self.data)
        self.clock = pygame.time.Clock()
        self.begin()
        
    def begin(self):
        """ Start the algorithm """
        self.update_graph()
        self.apply_algorithm()
        self.done()

    def update_graph(self):
        """ Update the graph display """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.pause()
        self.screen.fill(self.BACKGROUND_COLOR)
        self.graph.draw(self.screen)
        pygame.display.flip()

    def done(self):
        """ Once the algorithm is done, just loop infinitely """
        while True:
            self.update_graph()

    def apply_algorithm(self):
        """ Inherit with a sorting algorithm """
        pass

    def pause(self):
        """ Stop the simulation until space is pressed again """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return
            self.screen.fill(self.BACKGROUND_COLOR)
            self.graph.draw(self.screen)
            pygame.display.flip()
            

    def is_sorted(self):
        """ Test if the data is sorted by going linearly through the data until unsorted numbers are found """
        previous = 0  # Setting to 0 shouldn't be an issue aslong as MIN_VALUE is at least 0
        for value in self.data:
            if value < previous:
                return False
            previous = value
        return True


class Graph:
    """ Used to draw the data """
    EDGE = 10  # Distance from the edge of the screen the graph should be drawn
    SEPARATION = 2  # Distance between bars

    def __init__(self, data):
        """ Create a graph with the given data """
        self.data = data

    def draw(self, screen):
        """ Draw the data to the screen """
        n_of_bars = len(self.data)
        graph_width = screen.get_width() - self.EDGE * 2
        total_SEPARATION = self.SEPARATION * (n_of_bars - 1)
        bar_width = (graph_width - total_SEPARATION) / n_of_bars
        MAX_VALUE = max(self.data)  # Height of bars will be relative to the largest value

        x = self.EDGE
        for i in range(n_of_bars):
            # Create rect for bar
            height = (self.data[i] / MAX_VALUE) * (screen.get_height() - self.EDGE * 3)
            rect = pygame.Rect(int(x), 0, int(bar_width), height)
            rect.bottom = screen.get_height() - self.EDGE

            # Determine color based off value
            color_val = int(self.data[i] / MAX_VALUE * 100)
            color_r = 55 + color_val * 2
            color_b = 255 - color_val * 2
            pygame.draw.rect(screen, (color_r, 0, color_b), rect)
            x += bar_width + self.SEPARATION
