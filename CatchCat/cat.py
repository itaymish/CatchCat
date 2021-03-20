import turtle
import random
from character import *

class Cat(Character):
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

    def set_photo(self, photo):
        super().set_photo(photo)

    def random_position(self):
        self.random_x = random.randint(-474, 474)
        self.random_y = random.randint(-474, 474)

        self.character.setposition(self.random_x, self.random_y)