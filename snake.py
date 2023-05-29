from random import randrange
import os

def draw_a_map(fruit,secret_fruit,empty):
    for row in range(10):
        for column in range(10):
            if(column,row) in fruit:
                print("o ", end="") 
            elif(column,row) in secret_fruit:
                print("? ", end="") 
            elif (column, row) not in empty:
                print(". ", end="")                    
            else:
                print("X ", end="")
        print(end="\n")

def move(snake, fruit, secret_fruit, direction):

    if direction == "v":
        a,b=snake[-1]
        element=a+1,b

    elif direction=="z":
        a,b=snake[-1]
        element = a-1,b
            
    elif direction == "s":
        a,b=snake[-1]
        element=a,b-1
    
    elif direction == "j":
        a,b=snake[-1]
        element = a,b+1
    else:
        raise ValueError("Invalid direction.")
    
    for number in element:
        if number<0 or number>10:
            raise ValueError("Game over.")
    
    if element==fruit[-1]:
        del fruit[0]
        snake.append(element)
        fruit_xy=randrange(0,11),randrange(0,11)
        fruit.append(fruit_xy)
    
    elif len(secret_fruit)>0 and element==secret_fruit[0]:
        del secret_fruit[0]
        snake.append(element)

    elif element not in snake:
        snake.append(element)
        del snake[0]
    else:
        raise ValueError()
    
    return True

snake_coordinates= [(0,0)]
fruit_coordinates=[(1,1)]
secret_fruit_coordinates=[]
count=1
draw_a_map(fruit_coordinates, secret_fruit_coordinates, snake_coordinates) 

while True:
    direction= input("Zadaj stranu pohybu.")
    try:
        os.system('cls')
        move(snake_coordinates,fruit_coordinates,secret_fruit_coordinates, direction)
        draw_a_map(fruit_coordinates, secret_fruit_coordinates, snake_coordinates) 
        count=count+1       

        if count%30==0:
            secret_fruit_xy=randrange(0,11),randrange(0,11)
            secret_fruit_coordinates.append(secret_fruit_xy)
                        
    except ValueError:
        print("Game over.")
        break

