from turtle import Turtle
START_POSITION=[(0,0),(-20,0),(-40,0)]
DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:
    def __init__(self):
        self.segment=[]
        self.createsnake()
        self.head=self.segment[0]

    def createsnake(self):
        for position in START_POSITION:
           self.add_segment(position)

    def add_segment(self,position):
        tim = Turtle("square")
        tim.penup()
        tim.color("black")
        tim.goto(position)
        self.segment.append(tim)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.createsnake()
        self.head = self.segment[0]

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for seg_num in range(len(self.segment)-1, 0, -1):
            x = self.segment[seg_num - 1].xcor()
            y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(x, y)
        self.head.forward(DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

