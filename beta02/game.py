import pyglet
from pyglet.gl import *
from hero import *

class Game:
    grid = False
    heroes = []

    def __init__(self):
        self.grid = False
        self.heroes.append(Hero())

    def show_grid(self, xMax, yMax):
        factor = 16
        x, y  = 0, 0

        while x <= xMax:
            x += factor
            glBegin(GL_LINES)
            glVertex2i(x, 0)
            glVertex2i(x, yMax)
            glEnd()

        while y <= yMax:
            y += factor
            glBegin(GL_LINES)
            glVertex2i(0, y)
            glVertex2i(xMax, y)
            glEnd()

    def update(self):
        print 'updating'
        for x in heroes:
            x.update()

    def draw(self):
        for x in self.heroes:
            x.draw()
