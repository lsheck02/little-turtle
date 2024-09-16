import turtle as ttl
draw = ttl.Turtle()

#Height 250
#Width 475

start_x = -237
start_y = 125
stripe_height = 250/13

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


draw_stripes()


wn = ttl.Screen()
wn.mainloop()
