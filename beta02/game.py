from pyglet import clock, font, image, window
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

    def update(self, dt):
        self.dt = dt
        for i in self.heroes:
            i.update(dt)

    def draw(self, dt):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity() # Reset The View

	for i in self.heroes:
	    i.draw()

        if self.grid:
            self.show_grid(self.window.width, self.window.height)
  
        # Draw a square (quadrilateral)
        glBegin(GL_QUADS)                   # Start drawing a 4 sided polygon
        glVertex3f(-1.0, 1.0, 0.0)          # Top Left
        glVertex3f(1.0, 1.0, 0.0)           # Top Right
        glVertex3f(1.0, -1.0, 0.0)          # Bottom Right
        glVertex3f(-1.0, -1.0, 0.0)         # Bottom Left
        glEnd() 

        fps.draw()
