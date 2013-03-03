import pyglet
from pyglet.gl import *

window = pyglet.window.Window()
label = pyglet.text.Label('Hello World',
                            font_name='Times New Roman',
                            font_size=36,
                            x=window.width//2, y=window.height//2,
                            anchor_x='center', anchor_y='center')

@window.event
def on_draw():
    window.clear()
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)
    glVertex2i(50, 50)
    glVertex2i(75, 100)
    glVertex2i(100, 150)
    glVertex2i(200, 200)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2i(50, 50)
    glVertex2i(75, 100)
    glVertex2i(200, 200)
    glEnd()

pyglet.app.run()
