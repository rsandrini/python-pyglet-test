import random
import pyglet
from vector import *
from pyglet.gl import *

states = ['BORNING', 'STOP', 'HUNTING', 'ATTACKING', 'FLEEING', 'DEAD']

class Hero:

    position = vector2(0,0)
    state = states[0]
    timeout = 10
    hp = 0
    enemys = []
    destination = vector2(0,0)
    num_attacks = 0

    def __init__(self):
        self.position.x = 100
        self.position.y = 100
        self.state = 'BORNING'
        self.hp = 10
        self.num_attacks = 1

    def reset_position(self, x=None, y=None):
        if x and y:
            self.position.x, self.position.y = x, y
        else:
            self.position.x, self.position.y = 100, 100

    def update(self):
        print 'State: %s' % state
        if self.state is 'BORNING':
            if self.timeout <= 0:
                self.state = states[1]
            else:
                self.timeout -= timeout

        if self.state is 'STOP':
            if self.hp > 3:
                self.state = states[2]
            else:
                self.hp += 0.1
                self.state = states[4]
                self.destination = vector(100, 100)

        if self.state is 'FLEEING':
            if self.position is self.destination\
                and self.hp > 3:
                self.state = states[1]
            else:
                #caminhar
                pass

        if self.state is 'ATTACKING':
            if self.hp < 3:
                self.state = states[4]
            else:
                for x in enemys:
                    attacks = 0
                    if x.state != 'DEAD' and x.is_attackable:
                        if attacks < self.num_attacks:
                            #self.attack(x)
                            attacks += 1

        if self.state is 'HUNTING':
            #andar aleatorio
            pass

    def attack(self, enemy):
        at = random.randint(0, 10)
        return at

    def defense(self, enemy):
        df = random.randint(0, 10)
        return df

    def draw(self):
        # Draw some stuff
        glBegin(GL_TRIANGLES)
        x = self.position.x
        y = self.position.y
        glVertex2i(x, y)
        glVertex2i(x-10 , y-10)
        glVertex2i(x+10, x+10)
        glEnd()
