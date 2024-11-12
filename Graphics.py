import pygame
from pygame.draw_py import draw_line

pygame.init()


size = pygame.display.get_desktop_sizes()[0]
WIDTH = size[0]
HEIGHT = size[1]

BACKGROUND_COLOR = (255, 255, 255, 255)

screen = pygame.display.set_mode(size, pygame.FULLSCREEN | pygame.SCALED)


class Graphics:
    def __init__(self):
        self.running = False
        self.clock = pygame.time.Clock()

    def start(self):
        self.running = True
        self.loop()

    def loop(self):
        while self.running:
            self.control()
            screen.fill(BACKGROUND_COLOR)
            self.update()
            self.draw()
            self.clock.tick()

    def control(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                self.stop()
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    self.stop()

    def stop(self):
        self.running = False

    def update(self):
        pass

    def draw(self):
        pygame.draw.circle(screen, (255, 0, 0, 255), (WIDTH // 2, HEIGHT // 2), 50)
        pygame.display.flip()
