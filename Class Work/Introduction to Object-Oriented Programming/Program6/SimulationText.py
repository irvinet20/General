from Ball import Ball

def getFloat(prompt):
    while True:
        try:
            return float(input(prompt))
        except TypeError:
            print("Invalid float")

print("This script provides a text-only interface for testing a ball.")
x = getFloat('Initial x: ')
y = getFloat('Initial y: ')
vx = getFloat('Initial vx: ')
vy = getFloat('Initial vy: ')
g = getFloat('Gravity: ')

class _SimpleWorld:
    def getGravity(self):
        return g
    def getStar(self):
        return None

earth = _SimpleWorld()
b = Ball(x,y,vx,vy)
for time in range(1,11):
    b.advance(earth)
    print('After step %2d the ball is at (%5.2f, %5.2f)' % (time, b.getPositionX(), b.getPositionY()))
