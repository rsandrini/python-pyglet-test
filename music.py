import pyglet
from pyglet.gl import *

music = pyglet.resource.media('music.mp3')
music.play()

pyglet.app.run()
