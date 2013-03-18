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

@window.event
def update():
    game.update()


@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    if game.grid:
        game.show_grid(window.width, window.height)
    game.draw()

game = Game()
pyglet.app.run()


