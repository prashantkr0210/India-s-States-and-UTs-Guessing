# Use this code to get the coordinates of certain locations on picture inserted
import turtle

screen = turtle.Screen()
screen.screensize(700, 900)
screen.title("Indian States Game")

# Loading image to the screen
image = "india_map.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop() 
