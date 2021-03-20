import turtle
from character import *

class Text(Character):
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

    def write_text(self, text, align, font, size, mode):
        self.text = text
        self.align = align
        self.font = font
        self.size = size
        self.mode = mode

        self.character.hideturtle()
        self.character.write(self.text, align=self.align, font=(self.font, self.size, self.mode))

        if self.hide_character == True:
            self.character.hideturtle()
        elif self.hide_character == False:
            self.character.showturtle()
        else:
            print('Error: Unknown bolean at "hide_character"!')

    def clear_text(self):
        self.character.clear()