import pyglet
from pyglet.gl import *
from pyglet.window import mouse, key
from game import *

window = pyglet.window.Window(800, 600)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.G:
        if game.grid:
            print 'Grid desativada'
            game.grid = False
        else:
            print 'Grid ativada'
            game.grid = True

def update(dt):
    game.update(dt)
    game.draw(dt)


# schedule the update function, 60 times per second
pyglet.clock.schedule_interval(update, 1.0/60.0)

game = Game(window)
pyglet.app.run()


