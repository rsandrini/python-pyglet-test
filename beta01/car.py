import pyglet
from vector import *
from pyglet.gl import *

states = ['STOP', 'RUN']

class Car:

    position = vector2(0,0)
    state = states[0] 


    def __init__(self):
        self.position.x = 100
        self.position.y = 100

    def run(self):
        if self.state == 'STOP':
            self.state = states[1]
            print 'Carro iniciado'
        else:
            self.state = states[0]
            print 'Carro desligado'

    def reset(self, x=None, y=None):
        if x and y:
            self.position.x, self.position.y = x, y
        else:
            self.position.x, self.position.y = 100, 100

    def update(self):
        if self.state == states[1]:
            print 'X:%s Y:%s' % self.position.x, self.position.y

    def draw(self):
        # Draw some stuff
        glBegin(GL_TRIANGLES)
        x = self.position.x
        y = self.position.y
        glVertex2i(x, y)
        glVertex2i(x-10 , y-10)
        glVertex2i(x+10, x+10)
        glEnd()
