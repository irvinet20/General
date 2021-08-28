## start up
from cs1graphics import *
from time import sleep
Arctic = Canvas(800,600)
Penguin = Layer()
Sparrow = Layer()
Tree = Layer()
Sun = Layer()
depth = 100


###Story
Title = Text('The Sparrows and The Penguins', 24,)
Line1 = Text('The two birds species wanted to see who could fly higher.', 18,)
Line2 = Text('The sparrows flew first, high into the sky.', 18,)
Line3 = Text('The penguins then beat their wings and tried to follow the sparrows into the sky.', 18,)
Line4 = Text('However, the penguins could not fly, so it sunk into the ocean.', 18,)
Line5 = Text('The End', 24,)



class Bird(Layer):
    """ The Class is used to make birds from a bird template"""
    """ Birds Begnin at 0, 0 and slightly large for a 800,600 scene"""
    def __init__(self, BodyColor, WingColorTop, WingColorBot, ChestColor, BeakTopColor, BeakBotColor):
        """All in one creation, Body Color, Wing Color in two parts, Chest Color, and Beak Color in two parts are all parameters"""
        super().__init__()
        
        self._BodyColor = BodyColor
        self._WingColorTop = WingColorTop
        self._WingColorBot = WingColorBot
        self._ChestColor = ChestColor
        self._BeakTopColor = BeakTopColor
        self._BeakBotColor = BeakBotColor
        depth = 100

        Body = Circle(65)
        Body.setBorderWidth(4)
        Body.setFillColor(self._BodyColor)
        Body.setDepth(depth*3)

        LeftWingTop = Polygon(Point(-10, 60), Point(40, 0), Point(65, 40))
        LeftWingTop.setBorderWidth(4)
        LeftWingTop.setDepth(depth*5)
        LeftWingTop.setFillColor(self._WingColorBot)

        LeftWingBot = Polygon(Point(-10, 60), Point(40, 0), Point(45, 20))
        LeftWingBot.setDepth(depth*4)
        LeftWingBot.setFillColor(self._WingColorTop)

        RightWingTop = Polygon(Point(-10, 60), Point(40, 0), Point(65, 40))
        RightWingTop.setBorderWidth(4)
        RightWingTop.setDepth(depth*5)
        RightWingTop.setFillColor(self._WingColorBot)
        RightWingTop.flip()
        

        RightWingBot = Polygon(Point(-10, 60), Point(40, 0), Point(45, 20))
        RightWingBot.setDepth(depth*4)
        RightWingBot.setFillColor(self._WingColorTop)
        RightWingBot.flip()

        BeakTop = Polygon(Point(0,0), Point(-20,15), Point(20,15))
        BeakTop.setFillColor(self._BeakTopColor)
        BeakBot = Polygon(Point(-20,15), Point(20,15), Point(0,50))
        BeakBot.setFillColor(self._BeakBotColor)

        LeftOutterEye = Circle(10)
        LeftOutterEye.setFillColor('White')
        LeftInnerEye = Circle(4)
        LeftInnerEye.setFillColor('Black')

        RightOutterEye = Circle(10)
        RightOutterEye.setFillColor('White')
        RightInnerEye = Circle(4)
        RightInnerEye.setFillColor('Black')

        Chest = Circle(30)
        Chest.setDepth(depth)
        Chest.setFillColor(self._ChestColor)

        self.add(Body)

        LeftWingTop.move(-100,0)
        self.add(LeftWingTop)

        LeftWingBot.move(-100,0)
        self.add(LeftWingBot)

        RightWingTop.move(115,0)
        self.add(RightWingTop)

        RightWingBot.move(115,0)
        self.add(RightWingBot)

        self.add(BeakTop)
        self.add(BeakBot)

        LeftOutterEye.move(-30, -30)
        self.add(LeftOutterEye)

        LeftInnerEye.move(-30, -30)
        self.add(LeftInnerEye)

        RightOutterEye.move(30, -30)
        self.add(RightOutterEye)

        RightInnerEye.move(30, -30)
        self.add(RightInnerEye)

        Chest.move(0,40)
        self.add(Chest)


##Animal Creations        
Penguin1 = Bird('Black', 'Black', 'White', 'White', 'Orange', 'Yellow')
Penguin2 = Bird('DarkGrey', 'DarkGrey', 'white', 'White', 'Yellow', 'Orange')

Sparrow1 = Bird('Brown', 'RosyBrown', 'White', 'Tan', 'Orange', 'Yellow')
Sparrow2 = Bird('Brown', 'RosyBrown', 'White', 'Tan', 'Yellow', 'Orange')
        


#Tree
Trunk = Rectangle(50, 225)
Trunk.setFillColor('blanchedalmond')
Bush = Circle(50)
Bush.setFillColor('Green')
Bush.move(0,-115)

Tree.add(Trunk)
Tree.add(Bush)
Tree.setDepth(depth*10)

#sun
Suncore = Circle(100)
Suncore.setBorderWidth(5)
Ray1 = Path(Point(-200, 0), Point(0,0))
Ray1.setBorderColor('Yellow')
Ray1.setDepth(depth*10) # just to get rays behind border of sun and show sun transparency
Ray2 = Path(Point(-200, 100), Point(0,0))
Ray2.setBorderColor('Yellow')
Ray2.setDepth(depth*10)
Ray3 = Path(Point(-200, 200), Point(0,0))
Ray3.setBorderColor('Yellow')
Ray3.setDepth(depth*10)

Sun.add(Suncore)
Sun.add(Ray1)
Sun.add(Ray2)
Sun.add(Ray3)

#Icecap

icecap = Rectangle(550,150)
icecap.setFillColor('grey')

#Sea

sea = Rectangle(300, 75)
sea.setFillColor('Blue')
sea.setBorderColor('blue')

##Scene Start

Sparrow1.move(300,465)
Sparrow1.scale(.5)
Arctic.add(Sparrow1)

Penguin1.move(50,465)
Penguin1.scale(.5)
Arctic.add(Penguin1)

Sparrow2.move(425,465)
Sparrow2.scale(.5)
Arctic.add(Sparrow2)

Penguin2.move(175,465)
Penguin2.scale(.5)
Arctic.add(Penguin2)

icecap.move(250,600)
Arctic.add(icecap)

sea.move(675,600)
Arctic.add(sea)

Tree.move(425,450)
Arctic.add(Tree)

Sun.move(800,0)
Arctic.add(Sun)

Title.move(400,75)
Arctic.add(Title)

##Scene Animation
Line1.move(400, 115)
Arctic.add(Line1)

Line2.move(400, 140)
Arctic.add(Line2)
for i in range(12): #Following for loops used for time and to control flow of events
    Sparrow1.move(25,-15)
    Sparrow2.move(25,-15)
    sleep(.5)
    Sparrow1.move(25,-15)
    Sparrow2.move(25,-15)
    sleep(.5)

    
Line3.move(400, 165)
Arctic.add(Line3)

for i in range(11):
    sleep(.5)
    Penguin1.move(50,0)
    Penguin2.move(50,0)
    sleep(.5)

Line4.move(400, 190)
Arctic.add(Line4)

for i in range(10):
    Penguin1.move(0,10)
    Penguin2.move(0,10)
    sleep(.5)
    Penguin1.move(0,10)
    Penguin2.move(0,10)
    sleep(.5)

Line5.move(400, 230)
Arctic.add(Line5)




        ##Reference - template i was using to figure out body layout, then scaled for the layer as if 400,400 was origin - just easier for me visually
#Arctic.add(Abody)
#Abody.move(400, 400)
#Arctic.add(Awing1)
#Awing1.move(300,400)
#Arctic.add(AWout1)
#AWout1.move(300,400)
#Arctic.add(Awing2)
#Awing2.move(515, 400)
#Arctic.add(AWout2)
#AWout2.move(515,400)
#Arctic.add(AnoseT)
#AnoseT.move(400,400)
#Arctic.add(AnoseB)
#AnoseB.move(400,400)
#Arctic.add(AeyeO1)
#AeyeO1.move(370,370)
#Arctic.add(AeyeI1)
#AeyeI1.move(370,370)
#Arctic.add(AeyeO2)
#AeyeO2.move(430,370)
#Arctic.add(AeyeI2)
#AeyeI2.move(430,370)
#Arctic.add(Acore)
#Acore.move(400,440)

           















