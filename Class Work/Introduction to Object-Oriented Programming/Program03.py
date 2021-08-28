from cs1graphics import *

GridSize = int(input('Enter pixels per grid cell: '))
Board = Canvas(15*GridSize, 13*GridSize, 'brown')

for Spaces in range(0,2): #generally used for two board creation
    Space = Rectangle(6*GridSize,11*GridSize,Point(4*GridSize,6.5*GridSize))
    Space.setFillColor('Tan')
    Space.setBorderWidth(.075*GridSize)
    Half_Plane = Layer()
    Half_Plane.add(Space)
    
    for trit in range(0,2): #used to create top and bottom set of triangles
        for tri in range(0,6): #6 triangles in a row on one board
            Triangle = Polygon(Point(1*GridSize+GridSize*tri,1*GridSize+trit*11*GridSize), Point(2*GridSize+GridSize*tri,1*GridSize+trit*11*GridSize), Point(1.5*GridSize+GridSize*tri,6*GridSize+trit*1*GridSize))
            if (tri % 2) == 0:
                Triangle.setFillColor((255-255*trit,0,255*trit)) #trit used to alternate colors as vaule of 1 and 0
                Half_Plane.add(Triangle)
            if (tri % 2) != 0:
                Triangle.setFillColor((255*trit,0,255-255*trit))
                Half_Plane.add(Triangle)
                
    for circ in range(0,2): #same general structure as with triangles
        for cir in range(0,8):
            if cir < 2:
                Dot = Circle(.5*GridSize,Point(1.5*GridSize+GridSize*1*Spaces, 1.5*GridSize+cir*GridSize+GridSize*9*circ))
                Dot.setFillColor((255-255*circ,255-255*circ,255-255*circ))
                Dot.setBorderWidth(.005*GridSize)
                Half_Plane.add(Dot)
            if cir > 2:
                Dot = Circle(.5*GridSize,Point(6.5*GridSize, 1.5*GridSize+(cir-3)*GridSize+GridSize*6*circ))
                Dot.setFillColor((0+255*circ,0+255*circ,0+255*circ))
                Dot.setBorderWidth(.005*GridSize)
                Half_Plane.add(Dot)
                
    for n in range(0,12): #number setup
        if n <= 5:
            num = Text(str(abs(Spaces*25-(n+1))), GridSize*.5, Point(1.5*GridSize,12.5*GridSize-GridSize*12*Spaces))
            num.move(n*GridSize,0)
            Board.add(num)
        if n > 5:
            num = Text(str(abs(Spaces*25-(n+1))), GridSize*.5, Point(2.5*GridSize,12.5*GridSize-GridSize*12*Spaces))
            num.move(n*GridSize,0)
            Board.add(num)
                
    if Spaces == 0: #I was having issues with the fliping because i didnt know how to control it by round like rotate but this seemed to fix it
        Board.add(Half_Plane)
    if Spaces == 1:
        Half_Plane.adjustReference(4*GridSize*Spaces,6.5*GridSize*Spaces)
        Half_Plane.rotate(90*Spaces)
        Half_Plane.flip()
        Half_Plane.rotate(-90*Spaces)
        Half_Plane.move(7*GridSize*Spaces,0)
        Board.add(Half_Plane)

##Lazy Clean Up        
Mid = Path(Point(7.5*GridSize,0),Point(7.5*GridSize,13*GridSize))
Mid.setBorderWidth(.15*GridSize)
Board.add(Mid)

Dot = Circle(.5*GridSize, Point(9.5*GridSize, 3.5*GridSize))
Dot.setFillColor((0,0,0))
Board.add(Dot)

Dot = Circle(.5*GridSize, Point(9.5*GridSize, 9.5*GridSize))
Dot.setFillColor((255,255,255))
Board.add(Dot)



