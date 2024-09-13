import turtle as ttl

draw = ttl.Turtle()

color = input("What color would you like the circle to be? ")
radius = input("What would you like the radius of the circle to be? ")


draw.penup()
draw.pencolor(color)
draw.goto(0, 0 - int(radius))
draw.pendown()
draw.circle(int(radius))

wn = ttl.Screen()
wn.mainloop()