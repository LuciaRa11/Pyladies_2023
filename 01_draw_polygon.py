from turtle import forward, left, right, exitonclick, penup, pendown

def draw_polygon(side_count):
    side_lenght=200/side_count

    for side in range(side_count):
        forward(side_lenght)
        left(180-(180*(1-2/side_count)))

def move(distance):
    penup()
    forward(distance)
    pendown()

def get_valid_polygon_sides():
    sides=int(input("Enter the number of sides for the polygon from 3 to 30. "))
    while sides<3 or sides>30:
        sides=int(input("Enter the number of sides for the polygon from 3 to 30. "))
    return sides
    
polygon_sides= get_valid_polygon_sides()

for side_count in range(polygon_sides,polygon_sides + 4):   
    draw_polygon(side_count)
    move(75)

exitonclick()
