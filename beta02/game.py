from pyglet import clock, window
from pyglet.gl import *
from hero import *

fps = pyglet.clock.ClockDisplay()

class Game:
    grid = False
    heroes = []
    dt = None
    window = None

    def __init__(self, window):
        self.grid = False
        self.heroes.append(Hero())
	self.window = window

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

    def castle(self):
        pass

    def update(self, dt):
        self.dt = dt
        for i in self.heroes:
            i.update(dt)

    def draw(self, dt):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity() # Reset The View
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        fps.draw()

        for i in self.heroes:
            i.draw()

        if self.grid:
            self.show_grid(self.window.width, self.window.height)

        ## CASTLE
        glBegin(GL_TRIANGLES)
        glVertex2i(370, 270)
        glVertex2i(430, 370)
        glVertex2i(430, 270)
        glEnd()

        ##CAVES
        #glBegin(GL_

        ## ENEMYS


