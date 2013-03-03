import pyglet
from pyglet.gl import *

window = pyglet.window.Window()
image = pyglet.resource.image('keila.jpg')

@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)

pyglet.app.run()
