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
Title = Text('The Sparrow and The Penguin', 24,)
Line1 = Text('The two birds wanted to see who could fly higher.', 18,)
Line2 = Text('The sparrow flew first, high into the sky.', 18,)
Line3 = Text('The penguin then beat its wings and tried to follow the sparrow into the sky.', 18,)
Line4 = Text('However, the penguin could not fly, so it sunk into the ocean.', 18,)
Line5 = Text('The End', 24,)

###Quick key
# A = Animal
# AWout/SWout = Animal Wing outline/Sparrow Wing outline, the inner part of the wing used to add a second color
# AnoseT/SnoseT = Animal/Sparrow nose top, the top triangle of the double triangle nose
# AnoseB/SnoseB = Animal/Sparrow nose bottom, the bottom triangle of the double triangle nose
# AeyeO/SeyeO = Animal/Sparrow eye Outline, used to create the 2nd white circle around the eye
# AeyeI/SeyeI = Animal/Sparrow eye Inner, used to create the inner eye so the eye isnt just a white circle
# Acore/Score = Animal/Sparrow core, used to create the 2nd color on their stomach


###Req notes
# Rectangle = ocean and land mass #Note the oceans border is blue meeting border color req
# Polygon = Triangle beaks, etc - have varying thickness of wing vs body
# Path = Light rays from sun
# Circle = Sun - Is transparent
# Text = Text


###Penguin - orginally A was meant to be for a general animal body template, however, it became A and S for sparrow 

Abody = Circle(65)
Abody.setBorderWidth(4)
Abody.setFillColor('Black')
Abody.setDepth(depth*3)

Awing1 = Polygon(Point(-10, 60), Point(40, 0), Point(65, 45))
Awing1.setBorderWidth(4)
Awing1.setDepth(depth*5)
Awing1.setFillColor('White')
#Awing1.adjustReference(80,0) ## the thought was to adjust the ref so i can get more rotation from the tip of the wing

AWout1 = Polygon(Point(-10, 60), Point(40, 0), Point(45, 20))
AWout1.setDepth(depth*4)
#AWout1.adjustReference(80,0)
AWout1.setFillColor('Black')

Awing2 = Polygon(Point(-10, 60), Point(40, 0), Point(65, 45))
Awing2.setBorderWidth(4)
Awing2.setDepth(depth*5)
Awing2.setFillColor('White')
Awing2.flip()

AWout2 = Polygon(Point(-10, 60), Point(40, 0), Point(45, 20))
AWout2.setDepth(depth*4)
AWout2.setFillColor('Black')
AWout2.flip()

AnoseT = Polygon(Point(0,0), Point(-20,15), Point(20,15))
AnoseT.setFillColor('Orange')
AnoseB = Polygon(Point(-20,15), Point(20,15), Point(0,50))
AnoseB.setFillColor('Yellow')

AeyeO1 = Circle(10)
AeyeO1.setFillColor('White')
AeyeI1 = Circle(4)
AeyeI1.setFillColor('Black')

AeyeO2 = Circle(10)
AeyeO2.setFillColor('White')
AeyeI2 = Circle(4)
AeyeI2.setFillColor('Black')

Acore = Circle(30)
Acore.setDepth(depth)
Acore.setFillColor('White')

    #penguin body forming properly on layer to then be easily moved on canvas

Penguin.add(Abody)

Penguin.add(Awing1)
Awing1.move(-100,0)

Penguin.add(AWout1)
AWout1.move(-100,0)

Penguin.add(Awing2)
Awing2.move(115,0)

Penguin.add(AWout2)
AWout2.move(115,0)

Penguin.add(AnoseT)
Penguin.add(AnoseB)

Penguin.add(AeyeO1)
AeyeO1.move(-30,-30)

Penguin.add(AeyeI1)
AeyeI1.move(-30,-30)

Penguin.add(AeyeO2)
AeyeO2.move(30,-30)
           
Penguin.add(AeyeI2)
AeyeI2.move(30,-30)

Penguin.add(Acore)
Acore.move(0,40)


##
##
##



#Sparrow



Sbody = Circle(65)
Sbody.setBorderWidth(4)
Sbody.setFillColor('Brown')
Sbody.setDepth(depth*3)

Swing1 = Polygon(Point(-10, 60), Point(40, 0), Point(65, 45))
Swing1.setBorderWidth(4)
Swing1.setDepth(depth*5)
Swing1.setFillColor('White')


SWout1 = Polygon(Point(-10, 60), Point(40, 0), Point(45, 20))
SWout1.setDepth(depth*4)
SWout1.setFillColor('RosyBrown')

Swing2 = Polygon(Point(-10, 60), Point(40, 0), Point(65, 45))
Swing2.setBorderWidth(4)
Swing2.setDepth(depth*5)
Swing2.setFillColor('White')
Swing2.flip()

SWout2 = Polygon(Point(-10, 60), Point(40, 0), Point(45, 20))
SWout2.setDepth(depth*4)
SWout2.setFillColor('ROsyBrown')
SWout2.flip()

SnoseT = Polygon(Point(0,0), Point(-20,15), Point(20,15))
SnoseT.setFillColor('Orange')
SnoseB = Polygon(Point(-20,15), Point(20,15), Point(0,50))
SnoseB.setFillColor('Yellow')

SeyeO1 = Circle(10)
SeyeO1.setFillColor('White')
SeyeI1 = Circle(4)
SeyeI1.setFillColor('Black')

SeyeO2 = Circle(10)
SeyeO2.setFillColor('White')
SeyeI2 = Circle(4)
SeyeI2.setFillColor('Black')

Score = Circle(30)
Score.setDepth(depth)
Score.setFillColor('Tan')

    #Sparrow body forming properly on layer to then be easily moved on canvas

Sparrow.add(Sbody)

Sparrow.add(Swing1)
Swing1.move(-100,0)

Sparrow.add(SWout1)
SWout1.move(-100,0)

Sparrow.add(Swing2)
Swing2.move(115,0)

Sparrow.add(SWout2)
SWout2.move(115,0)

Sparrow.add(SnoseT)
Sparrow.add(SnoseB)

Sparrow.add(SeyeO1)
SeyeO1.move(-30,-30)

Sparrow.add(SeyeI1)
SeyeI1.move(-30,-30)

Sparrow.add(SeyeO2)
SeyeO2.move(30,-30)
           
Sparrow.add(SeyeI2)
SeyeI2.move(30,-30)

Sparrow.add(Score)
Score.move(0,40)

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

Sparrow.move(300,465)
Sparrow.scale(.7)
Arctic.add(Sparrow)

Penguin.move(100,465)
Penguin.scale(.7)
Arctic.add(Penguin)

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
    Swing1.rotate(10) #Rotations are for a slight wing animation
    SWout1.rotate(10)
    Swing2.rotate(-10)
    SWout2.rotate(-10)
    Sparrow.move(25,-15)
    sleep(.5)
    Swing1.rotate(-10)
    SWout1.rotate(-10)
    Swing2.rotate(10)
    SWout2.rotate(10)
    Sparrow.move(25,-15)
    sleep(.5)

    
Line3.move(400, 165)
Arctic.add(Line3)

for i in range(11):
    Awing1.rotate(10)
    AWout1.rotate(10)
    Awing2.rotate(-10)
    AWout2.rotate(-10)
    Penguin.move(25,0)
    sleep(.5)
    Awing1.rotate(-10)
    AWout1.rotate(-10)
    Awing2.rotate(10)
    AWout2.rotate(10)
    Penguin.move(25,0)
    sleep(.5)

Line4.move(400, 190)
Arctic.add(Line4)

for i in range(10):
    Awing1.rotate(10)
    AWout1.rotate(10)
    Awing2.rotate(-10)
    AWout2.rotate(-10)
    Penguin.move(0,10)
    sleep(.5)
    Awing1.rotate(-10)
    AWout1.rotate(-10)
    Awing2.rotate(10)
    AWout2.rotate(10)
    Penguin.move(0,10)
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

           















