from graphics import *

def main():
    width, height, colourList = userInputs()
    win = GraphWin("Patches", width, height)
    patchType, patchColour = drawPatches(win, width, height, colourList)
    patchSwap(win, width, height, patchType, patchColour)
    
def userInputs():
    width, height = getDimensions()
    colourList = getColours()
    return width, height, colourList

def getDimensions():
    validDimensions = [2, 3, 4, 5, 6, 7, 8]
    dimensions = []
    text = "width"
    while len(dimensions) < 2:
        if len(dimensions) == 1:
            text = "height"
        dimension = input("Please enter the " + text + ": ")
        if dimension.isdigit():
            if int(dimension) in validDimensions:
                dimensions.append(int(dimension))
            else:
                errorMessage()
        else:
            errorMessage()
    print()
    return dimensions[0] * 100, dimensions[1] * 100

def getColours():   
    print("Please make your colour choices. \
Available colours are red, green, blue, yellow, magenta, and cyan.")
    print()
    validColours = ["red", "green", "blue", "yellow", "magenta", "cyan"]
    colourList = []
    while len(colourList) < 4:
        colour = input("Please enter colour choice {0}: ".format(len(
            colourList)+1)).lower()
        if colour in validColours and colour not in colourList:
            colourList.append(colour)
        elif colour in validColours and colour in colourList:
            print("You have already selected this colour. Choose another.")
            print()
        else:
            errorMessage()
    return colourList

def drawPatches(win, width, height, colourList):  
    patchType = []
    patchColour = []
    drawColour = -1 
    for i in range(0, height, 100):
        for j in range(0, width, 100):           
            drawPatch = (i + j) % 200
            drawColour = (drawColour + 1) % 4
            if drawPatch == 0:
                circles(win, j, i, colourList[drawColour])
            else:
                zigzags(win, j, i, colourList[drawColour])               
            patchType.append(drawPatch)
            patchColour.append(colourList[drawColour])        
    return patchType, patchColour

def circles(win, x, y, colour):     
    radius = 5
    centreX = x + 50
    centreY = y + 95
    container(win, x, y)
    for j in range(10):
        circle = Circle(Point(centreX, centreY), radius)
        circle.setOutline(colour) 
        circle.draw(win)       
        radius = radius + 5
        centreY = centreY - 5

def zigzags(win, x, y, colour):
    container(win, x, y)
    for i in range(y + 10, y + 110, 20):
        for j in range(x + 10, x + 110, 10):
            drawDiagonals(win, j, i, colour)
    for k in range(y + 10, y + 110, 10):
        line = Line(Point(x, k), Point(x + 100, k))
        line.setFill(colour)
        line.draw(win)

def drawDiagonals(win, x, y, colour):
    diagonalOne = Line(Point(x - 10, y - 10), Point(x, y))
    diagonalTwo = Line(Point(x - 10, y + 10), Point(x, y))
    diagonalOne.setOutline(colour)
    diagonalTwo.setOutline(colour)
    diagonalOne.draw(win)
    diagonalTwo.draw(win)
    
def container(win, x, y):
    container = Rectangle(Point(x, y), Point(x + 100, y + 100))
    container.setFill("white")
    container.draw(win)

def patchSwap(win, width, height, patchType, patchColour):
    while True:
        x1, y1, index1, patchType1, patchColour1 = selectPatch(
            win, width, patchType, patchColour)
        x2, y2, index2, patchType2, patchColour2 = selectPatch(
            win, width, patchType, patchColour)
        drawPatchSwap(win, x1, y1, patchType2, patchColour2)
        drawPatchSwap(win, x2, y2, patchType1, patchColour1)
        patchType[index1] = patchType2
        patchType[index2] = patchType1
        patchColour[index1] = patchColour2
        patchColour[index2] = patchColour1

def selectPatch(win, width, patchType, patchColour):
    userClick = win.getMouse() 
    x = userClick.getX() // 100
    y = userClick.getY() // 100
    index = y * width//100 + x
    return x, y, index, patchType[index], patchColour[index]

def drawPatchSwap(win, x, y, patchType, patchColour):
    if patchType == 0:
        circles(win, x*100, y*100, patchColour)
    else:
        zigzags(win, x*100, y*100, patchColour)

def errorMessage():
    print("This is not a valid input. Try again.")
    print()
        
main()