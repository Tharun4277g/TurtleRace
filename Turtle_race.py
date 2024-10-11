import random
from turtle import Turtle,Screen
WIDTH,HEIGHT=400,400
color_list=["red","green","aquamarine1","black","blue","brown","orange","pink","yellow"]
def no_of_turtles():
    count=0
    while True:
        count = int(input("How Many Turtles do you want to race(2-10)"))
        if 2<=count<=10:
            return count
        else:
            print("Turtles are not within the range....!")
turtles=no_of_turtles()
print(turtles)
s1=Screen()
s1.setup(400,400)#width,height
x_spacing=WIDTH//(turtles+1)
turtle_list=[]
for i in range(1,turtles+1):
    new_turtle=Turtle()
    new_turtle.shape("turtle")
    new_turtle.left(90)#Rotate 90 degrees
    new_turtle.color([color_list[i-1]])
    new_turtle.penup()
    new_turtle.goto(-WIDTH//2 +(i*x_spacing),-HEIGHT//2+10)
    turtle_list.append(new_turtle)
def race():
    is_race_on=True
    while is_race_on:
        for t in turtle_list:
            distance=random.randrange(1,20)
            t.forward(distance)
            x,y=t.pos()
            if y>=((HEIGHT/2)-20):
                print(f"The Winner is {t.pencolor()} Turtle!")
                is_race_on=False
race()
s1.exitonclick()
