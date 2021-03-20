import turtle
from game import *
from text import *

window = turtle.Screen()
#window.bgcolor('lightgreen')
window.bgpic('media/background.gif')
window.title('CatchCat')
window.screensize(500, 500)
window.cv._rootwindow.resizable(False, False)
turtle.tracer(False)

'''start_text = Text(screen=window,
                  color='violet',
                  shape='classic',
                  shape_size=3,
                  head_turn=90,
                  speed=0,
                  turn_angle_right=5,
                  turn_angle_left=5,
                  increase_speed_amount=1,
                  decrease_speed_amount=1,
                  x_min_border=-500,
                  x_max_border=500,
                  y_min_border=-500,
                  y_max_border=500,
                  x_position=0,
                  y_position=0,
                  width=3,
                  hide_character=True)'''

if __name__ == '__main__':
    try:
        Game(screen=window)
    except:
        pass

    #Game(screen=window)