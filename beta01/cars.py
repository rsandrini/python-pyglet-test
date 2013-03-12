import pyglet
from pyglet.gl import *

window = pyglet.window.Window(800, 600)


def loading_grid(width=None, height=None):
    grid = []
    x, y  = 0, 0 
    if not width and not height:
        xMax = window.width
        yMax = window.height
    else:
        xMax = width
        yMax = height

    while x <= xMax:
      	grid.append({x, 0, x, xMax})
        x += 8
    
    while y <= yMax:
        grid.append({y, 0, y, yMax})
        y += 8
    return grid


def draw_grid():
    grid = loading_grid()
    print grid
    '''
    try:
        for i in grid:
            print i
            txMin = i.pop()
            txMax = i.pop()
            tyMin = i.pop()
            tyMax = i.pop()
	    
	    if tX and tY:
                glBegin(GL_LINES)
                glVertex2i(txMin, txMax)        
		glVertex2i(tyMin, txMax)
                glEnd() 
    except KeyError:

        print 'KeyError'
        pass
    '''

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_grid()

pyglet.app.run()


