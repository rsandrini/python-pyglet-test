import pyglet
from pyglet.gl import *
from pyglet.window import mouse, key


window = pyglet.window.Window(800, 600)
grid = False

def loading_grid(width=None, height=None):
    factor = 16
    x, y  = 0, 0
    if not width and not height:
        xMax = window.width
        yMax = window.height
    else:
        xMax = width
        yMax = height

    while x <= xMax:
        print 'X:%s' % x
        x += factor
        glBegin(GL_LINES)
        glVertex2i(x, 0)
        glVertex2i(x, window.height)
        glEnd()

    while y <= yMax:
        print 'Y:%s' % y
        y += factor
        glBegin(GL_LINES)
        glVertex2i(0, y)
        glVertex2i(window.width, y)
        glEnd()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.G:
        if grid:
            grid = False
        else:
            grid = True

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    if grid:
        loading_grid()

pyglet.app.run()


