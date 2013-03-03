import pyglet
from pyglet.window import mouse, key
from pyglet.gl import *

window = pyglet.window.Window()


@window.event
def on_draw():
    window.clear()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print 'The key "A" was pressed'
    elif symbol == key.LEFT:
        print 'The key "LEFT" was pressed'
    elif symbol == key.ENTER:
        print 'The Key "ENTER" was pressed'

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print 'The left mouse button was pressed'


pyglet.app.run()
