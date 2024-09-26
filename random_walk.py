from turtle import Turtle, Screen
import random

# Explaination for random walk.
# https://en.wikipedia.org/wiki/Random_walk

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270, 360]

# 套用Turtle的物件。
turtle = Turtle()

# 將turtle定義成圓形。
turtle.shape("circle")

def random_color ():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    print(r,g,b)
    random_colors = (r, g, b)
    return random_colors

# Call Screen()
screen = Screen()
screen.colormode(255)

# 開始亂走
for _ in range(200):
    turtle.color(random_color())
    turtle.forward(30)
    turtle.setheading(random.choice(directions))
    turtle.pensize(10)
    
# After click the screen will remove.
screen.exitonclick()


