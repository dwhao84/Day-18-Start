
from turtle import Turtle, Screen
import random
timmy_the_turtle = Turtle()

timmy_the_turtle.shape("circle")
timmy_the_turtle.color("red")

# 1. Draw a square.
# for i in range(4):
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.right(90)

# # 2. Import Modules
# import heroes
# print(heroes.gen())

# 3. Draw a Dashed Line in Turtle.
# for _ in range(50):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()  # 筆畫下去
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()    # 筆拿起來

# 4. Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon.
# 五角形的角度為72度
# 正方形的角度為90度

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed"]

# 寫法1:
def draw_shape(number_side):
    angle = 360 / number_side
    for _ in range(number_side):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)
        
for shape_side in range(3,11):
    draw_shape(shape_side) # 畫出3~10的多邊形
    timmy_the_turtle.color(random.choice(colours)) # 用random的方法，在turtle.color畫出不同顏色的圓。

# 寫法2:
# 另一個較為直觀的寫法。
for _ in range(3):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(360/3)

for i in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(360/4)

for i in range(5):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(360/5)
    
for i in range(6):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(360/6)

for i in range(7):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(360/7)

for i in range(8):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(360/8)

for i in range(9):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(360/9)
    
for i in range(10):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(360/10)


# Call Screen()
screen = Screen()
screen.exitonclick()