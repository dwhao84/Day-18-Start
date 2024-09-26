import random
from turtle import Turtle, Screen

screen = Screen()
screen.colormode(255)

t = Turtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########
for i in range(36):
    t.pencolor(random_color()) # 產生隨機顏色
    t.pensize(1)              # 設定筆寬
    t.circle(100)              # 畫圓
    t.shape("circle")
    t.left(10)
    t.speed("fast")
    
screen.exitonclick() # screen運行完之後，視窗關閉。



