import turtle
from character import *

class Borders(Character):
    def __init__(self, 
                 screen,
                 color, 
                 shape, 
                 shape_size, 
                 head_turn, 
                 speed, 
                 turn_angle_right, 
                 turn_angle_left, 
                 increase_speed_amount, 
                 decrease_speed_amount, 
                 x_min_border, 
                 x_max_border, 
                 y_min_border, 
                 y_max_border,
                 x_position, 
                 y_position, 
                 width,
                 hide_character):
        super().__init__(screen,
                         color, 
                         shape, 
                         shape_size, 
                         head_turn, 
                         speed, 
                         turn_angle_right, 
                         turn_angle_left, 
                         increase_speed_amount, 
                         decrease_speed_amount, 
                         x_min_border, 
                         x_max_border, 
                         y_min_border, 
                         y_max_border,
                         x_position, 
                         y_position, 
                         width,
                         hide_character)

    def draw_borders(self):
        self.character.setposition(self.x_min_border, self.y_min_border)
        self.character.pendown()
        self.character.speed(0)

        for self.side in range(4):
            self.character.forward(self.x_max_border * 2)
            self.character.right(90)

        self.character.penup()
        self.character.speed(self.speed)

        if self.hide_character == True:
            self.character.hideturtle()
        elif self.hide_character == False:
            self.character.showturtle()
        else:
            print('Error: Unknown bolean at "hide_character", "Character"')

        self.character.setposition(self.x_position, self.y_position)