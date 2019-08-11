import numpy as np
import pygame
import time

class _turtle():

    def __init__(self):
        pygame.init()
        res_x, res_y = 1000, 1000
        pygame.display.set_caption("Turtle")
        self.display = pygame.display.set_mode((res_x, res_y))
        self.display.fill((255,255,255))
        pygame.display.update()
        self.x = res_x/2
        self.y = res_y/2
        self.theta = 0
        self.draw = False
        self.width = 1
        self.lines = []
        time.sleep(0.5)

    def move(self, dist, width = 1):
        x1 = self.x + dist*np.cos(self.theta)
        y1 = self.y + dist*np.sin(self.theta)
        if (self.draw):
            self.lines.append({'start_x':self.x, 'start_y':self.y, 'end_x':x1, 'end_y':y1, 'width':self.width})
        self.x = x1
        self.y = y1
        self.refresh()
    
    def turn(self, angle):
        self.theta = (self.theta+angle)%(2*np.pi)
        self.refresh()

    def refresh(self):
        self.display.fill((255,255,255))
        for line in self.lines:
            pygame.draw.line(pygame.display.get_surface(), [0,0,0], [line['start_x'], line['start_y']], [line['end_x'], line['end_y']], 2*line['width'])
        self.draw_self()
        pygame.display.update()

    def draw_self(self):
        angle = np.pi*6/8
        size = 10
        width = 3
        r = [self.x + size*np.cos(self.theta+angle), self.y + size*np.sin(self.theta+angle)]
        l = [self.x + size*np.cos(self.theta-angle), self.y + size*np.sin(self.theta-angle)]
        pygame.draw.line(pygame.display.get_surface(), [255,0,0], [self.x, self.y], [l[0], l[1]], width)
        pygame.draw.line(pygame.display.get_surface(), [255,0,0], [self.x, self.y], [r[0], r[1]], width)
