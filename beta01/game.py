import pyglet
from pyglet.gl import *
from car import *

class Game:
    grid = False
    car = None

    def __init__(self):
        self.grid = False
        self.car = Car()
       
    def loading_grid(self, xMax, yMax):
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

    def loading_car(self):
        self.car.reset()
	self.car.run()    
    
    def update(self):
        print 'updating'
        self.car.update()

    def draw(self):
        self.car.draw()
