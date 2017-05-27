import turtle

# set up screen, sets up screen object
wn = turtle.Screen()
wn.bgcolor("red")
wn.title("turtle game with classes")
class Border(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
    # speed with () is a method and 0 means no speed no animate just draw
        self.speed(0)
        self.color('white')
        self.pensize(5)

    def draw_border(self):
        self.penup()
        self.goto(-300, -300)
        self.pendown()
        self.goto(-300, 300)
        self.goto(300, 300)
        self.goto(300, -300)
        self.goto(-300, -300)


class Player(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("turtle")
        self.color("white")
        self.speed = 1


# nice example of the use of a class as all the attributes for the players are here if there is more than one player
    # we have already set up the needed values
    def move(self):
        self.forward(self.speed)

    def turnleft(self):
        self.left(30)

    def turnright(self):
        self.right(30)

    def increasespeed(self):
        self.speed +=1

    def decreasespeed(self):
        self.speed -=1





# player is no the thing that self refers to
# player will get its attributes, ( features, traits, properties, characteristics from capital P  Player class
player = Player()
border = Border()
# player is an insance of the Player class

# draw the border
border.draw_border()

# set keyboard binding
turtle.listen()
turtle.onkey(player.turnleft, "Left")
turtle.onkey(player.turnright, "Right")
turtle.onkey(player.increasespeed, "Up")
turtle.onkey(player.decreasespeed, "Down")

# Main Loop
while True:

    player.move()
