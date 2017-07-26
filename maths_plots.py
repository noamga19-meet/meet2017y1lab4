import turtle

X=0
while X<300:
    y=X**2/300
    turtle.goto(X,y)
    X=X+100

turtle.mainloop()
