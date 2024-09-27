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
    
########### Angela的解法:
# 設定size_of_gap的數值為所畫的圈數。
# 並將整個功能寫成def，將再把size_of_gap的數值傳進去。
def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        t.color(random_color())
        # This method is used to draw a circle with a given radius
        t.circle(100)
        # setheading(angle): Sets the orientation of the turtle to angle
        t.setheading(t.heading() +  size_of_gap)
        
# screen運行完之後，視窗關閉。
screen.exitonclick()



