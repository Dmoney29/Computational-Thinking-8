import turtle #start
turtle.Screen() .bgcolor ("black")

t = turtle.Turtle()
t.speed(10)
t.goto(-100, -100)
# Color changing 
colors = ["pink","blue","white"]
for i in  range (1000):
    t.color (colors [i % 3] )   
    t.forward(100 + i)
    t.left (121)

turtle.exitonclick()#exit