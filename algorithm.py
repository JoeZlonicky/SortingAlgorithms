import pygame
import random


class SortingAlgorithm:
    def __init__(self, title, data_size, graph_color):
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_icon(pygame.image.load("icon.png").convert_alpha())
        pygame.display.set_caption(title)
        self.graph = Graph(graph_color)
        self.data = [random.randrange(0, 100) for _ in range(data_size)]
        self.clock = pygame.time.Clock()

    def start(self):
        self.update_graph()
        self.apply_algorithm()
        self.loop()

    def update_graph(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        self.screen.fill((0, 0, 0))
        self.graph.draw(self.screen, self.data)
        pygame.display.flip()

    def loop(self):
        while True:
            self.update_graph()

    def apply_algorithm(self):
        pass

    def is_sorted(self):
        previous = 0
        for value in self.data:
            if value < previous:
                return False
            previous = value
        return True


class Graph:
    edge = 10
    separation = 6

    def __init__(self, color):
        self.color = color

    def draw(self, screen, data):
        n_of_bars = len(data)
        graph_width = screen.get_width() - self.edge * 2
        width_without_separation = self.separation * (n_of_bars - 1)
        bar_width = (graph_width - width_without_separation) / n_of_bars
        max_value = max(data)

        x = self.edge
        for i in range(n_of_bars):
            height = (data[i] / max_value) * (screen.get_height() - self.edge * 3)
            rect = pygame.Rect(int(x), 0, int(bar_width), height)
            rect.bottom = screen.get_height() - self.edge
            color_r = 55 + data[i] * 2
            color_b = 255 - data[i] * 2
            pygame.draw.rect(screen, (color_r, 0, color_b), rect)
            x += bar_width + self.separation
