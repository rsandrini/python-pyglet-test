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

    if symbol == key.R:
        print 'iniciando carro'
        game.loading_car()

    if symbol == key.UP:
        game.car.position.x += 1

@window.event
def update():
    game.update()


@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    if game.grid:
        game.loading_grid(window.width, window.height)
    game.draw()

game = Game()
pyglet.app.run()


