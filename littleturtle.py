import turtle as ttl
draw = ttl.Turtle()

#Height 250
#Width 475

start_x = -237
start_y = 125
stripe_height = 250/13

gapbetweenstars = stripe_height+6

draw.speed(100)
draw.penup()


def rectangle_stripe(x, y, color):
    draw.goto(x, y)
    draw.pendown()
    draw.color(color)
    draw.begin_fill()
    draw.forward(475)
    draw.right(90)
    draw.forward(stripe_height)
    draw.right(90)
    draw.forward(475)
    draw.right(90)
    draw.forward(stripe_height)
    draw.right(90)
    draw.end_fill()
    draw.penup()

def drawstar(x, y, color, length):
    draw.goto(x,y)
    draw.setheading(0)
    draw.pendown()
    draw.begin_fill()
    draw.color(color)
    draw.forward(length)
    draw.right(144)
    draw.forward(length)
    draw.right(144)
    draw.forward(length)
    draw.right(144)
    draw.forward(length)
    draw.right(144)
    draw.forward(length)
    draw.right(144)
    draw.forward(length)
    draw.right(144)
    draw.end_fill()
    draw.penup()
    

def draw_stripes():
    rectangle_stripe(-237, 125, "red")
    rectangle_stripe(-237, 125-stripe_height*2, "red")
    rectangle_stripe(-237, 125-stripe_height*4, "red")
    rectangle_stripe(-237, 125-stripe_height*6, "red")
    rectangle_stripe(-237, 125-stripe_height*8, "red")
    rectangle_stripe(-237, 125-stripe_height*10, "red")
    rectangle_stripe(-237, 125-stripe_height*12, "red")

    rectangle_stripe(-237, 125-stripe_height, "white")
    rectangle_stripe(-237, 125-stripe_height*3, "white")
    rectangle_stripe(-237, 125-stripe_height*5, "white")
    rectangle_stripe(-237, 125-stripe_height*7, "white")
    rectangle_stripe(-237, 125-stripe_height*9, "white")
    rectangle_stripe(-237, 125-stripe_height*11, "white")

def drawblue(x, y, color):
    square_height = (7/13) * 250
    square_width = (0.76) * 250
    draw.goto(x, y)
    draw.pendown()
    draw.color(color)
    draw.begin_fill()
    draw.forward(square_width)
    draw.right(90)
    draw.forward(square_height)
    draw.right(90)
    draw.forward(square_width)
    draw.right(90)
    draw.forward(square_height)
    draw.right(90)
    draw.end_fill()
    draw.penup()

def drawstars():
    drawstar(-222, 112, "white", 10)
    drawstar(-222+30, 112, "white", 10)
    drawstar(-222+60, 112, "white", 10)
    drawstar(-222+90, 112, "white", 10)
    drawstar(-222+120, 112, "white", 10)
    drawstar(-222+150, 112, "white", 10)

    drawstar(-222, 112-gapbetweenstars, "white", 10)
    drawstar(-222+30, 112-gapbetweenstars, "white", 10)
    drawstar(-222+60, 112-gapbetweenstars, "white", 10)
    drawstar(-222+90, 112-gapbetweenstars, "white", 10)
    drawstar(-222+120, 112-gapbetweenstars, "white", 10)
    drawstar(-222+150, 112-gapbetweenstars, "white", 10)

    drawstar(-222, 112-gapbetweenstars*2, "white", 10)
    drawstar(-222+30, 112-gapbetweenstars*2, "white", 10)
    drawstar(-222+60, 112-gapbetweenstars*2, "white", 10)
    drawstar(-222+90, 112-gapbetweenstars*2, "white", 10)
    drawstar(-222+120, 112-gapbetweenstars*2, "white", 10)
    drawstar(-222+150, 112-gapbetweenstars*2, "white", 10)

    drawstar(-222, 112-gapbetweenstars*3, "white", 10)
    drawstar(-222+30, 112-gapbetweenstars*3, "white", 10)
    drawstar(-222+60, 112-gapbetweenstars*3, "white", 10)
    drawstar(-222+90, 112-gapbetweenstars*3, "white", 10)
    drawstar(-222+120, 112-gapbetweenstars*3, "white", 10)
    drawstar(-222+150, 112-gapbetweenstars*3, "white", 10)

    drawstar(-222, 112-gapbetweenstars*4, "white", 10)
    drawstar(-222+30, 112-gapbetweenstars*4, "white", 10)
    drawstar(-222+60, 112-gapbetweenstars*4, "white", 10)
    drawstar(-222+90, 112-gapbetweenstars*4, "white", 10)
    drawstar(-222+120, 112-gapbetweenstars*4, "white", 10)
    drawstar(-222+150, 112-gapbetweenstars*4, "white", 10)

    drawstar(-206, 100, "white", 10)
    drawstar(-206+30, 100, "white", 10)
    drawstar(-206+60, 100, "white", 10)
    drawstar(-206+90, 100, "white", 10)
    drawstar(-206+120, 100, "white", 10)

    drawstar(-206, 100-gapbetweenstars, "white", 10)
    drawstar(-206+30, 100-gapbetweenstars, "white", 10)
    drawstar(-206+60, 100-gapbetweenstars, "white", 10)
    drawstar(-206+90, 100-gapbetweenstars, "white", 10)
    drawstar(-206+120, 100-gapbetweenstars, "white", 10)

    drawstar(-206, 100-gapbetweenstars*2, "white", 10)
    drawstar(-206+30, 100-gapbetweenstars*2, "white", 10)
    drawstar(-206+60, 100-gapbetweenstars*2, "white", 10)
    drawstar(-206+90, 100-gapbetweenstars*2, "white", 10)
    drawstar(-206+120, 100-gapbetweenstars*2, "white", 10)

    drawstar(-206, 100-gapbetweenstars*3, "white", 10)
    drawstar(-206+30, 100-gapbetweenstars*3, "white", 10)
    drawstar(-206+60, 100-gapbetweenstars*3, "white", 10)
    drawstar(-206+90, 100-gapbetweenstars*3, "white", 10)
    drawstar(-206+120, 100-gapbetweenstars*3, "white", 10)

def border():
    draw.goto(start_x, start_y)
    draw.pendown()
    draw.setheading(0)
    draw.color("black")
    draw.forward(475)
    draw.right(90)
    draw.forward(250)
    draw.right(90)
    draw.forward(475)
    draw.right(90)
    draw.forward(250)
    draw.penup()
    
draw_stripes()
drawblue(-237, 125, "navy")
drawstars()
border()
draw.goto(200, 200)

wn = ttl.Screen()
wn.mainloop()
