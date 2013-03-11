import pyglet
from pyglet.gl import *

window = pyglet.window.Window()


@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINES)
    glVertex2i(0,  window.width)
    glEnd()


pyglet.app.run()
