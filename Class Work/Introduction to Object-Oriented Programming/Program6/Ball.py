from math import sqrt
class Ball:

    def __init__(self, initialPosX=0, initialPosY=0, initialVelX=0, initialVelY=0):
        self._posX = initialPosX
        self._posY = initialPosY
        self._velX = initialVelX
        self._velY = initialVelY
    def getPositionX(self):
        return self._posX
    def getPositionY(self):
        return self._posY
    def getVelocityX(self):
        return self._velX
    def getVelocityY(self):
        return self._velY
    def advance(self, world):
        star = world.getStar()
        if star:
            SPX = star.getPositionX()
            SPY = star.getPositionY()
            SPM = star.getMass()
            DX = self._posX-SPX
            DY = self._posY-SPY
            if DX == 0:
                MagX = 0
            if DY ==0:
                MagY = 0
            else:
                MagX = SPM / DX**2
                MagY = SPM / DY**2

            self._velY = self._velY + MagY
            self._velX = self._velX + MagX
            self._posX = self._posX + self._velX
            self._posY = self._posY + self._velY
        else:
            self._posX = self._posX + self._velX
            self._posY = self._posY + self._velY
            g = world.getGravity()
            self._velY = self._velY + g






##    def advance(self, world):
##        self._posX = self._posX + self._velX
##        self._posY = self._posY + self._velY
##        g = world.getGravity()
##        self._velY = self._velY + g
    
