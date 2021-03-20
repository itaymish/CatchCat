import turtle
import time
from character import *
from borders import *
from text import *
from cat import *

class Game(object):
    def __init__(self, screen):
        self.screen = screen

        self.clicks = 0
        self.time_limit = 5
        self.start_time = time.time()
        self.count_clicks = True

        self.cat = Cat(screen=self.screen,
                       color='blue',
                       shape='classic',
                       shape_size=5,
                       head_turn=90,
                       speed=3,
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
                       hide_character=False)

        self.cat.set_photo('media/cat.gif')

        self.clicks_text = Text(screen=self.screen,
                                color='black',
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
                                y_position=400,
                                width=3,
                                hide_character=True)

        self.game_over_text = Text(screen=self.screen,
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
                                   hide_character=True)

        self.clicks_text.write_text(f'Clicks: {self.clicks}', 'center', 'Arial', 32, 'normal')

        self.cat.character.onclick(self.clicked)

        self.border = Borders(screen=self.screen,
                              color='black',
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
                              width=5,
                              hide_character=True)

        self.border.draw_borders()

        self.screen.listen()
        self.screen.onkeypress(self.reset, 'r')
        self.screen.onkeypress(self.reset, 'R')
        
        while True:
            self.elapsed_time = time.time() - self.start_time
            print(self.time_limit - int(self.elapsed_time))
            if self.elapsed_time > self.time_limit:
                if self.count_clicks == True:
                    self.game_over_text.write_text('Game over! Press R to restart', 'center', 'Arial', 32, 'normal')

                self.count_clicks = False
                
            turtle.update()

        turtle.done()
        
    def clicked(self, x, y):
        if self.count_clicks:
            self.clicks += 1

            self.clicks_text.clear_text()
            self.clicks_text.write_text(f'Clicks: {self.clicks}', 'center', 'Arial', 32, 'normal')

            self.cat.random_position()
        else:
            pass

    def reset_timer(self):
        self.start_time = time.time()
        #self.start_time = time.time() - self.elapsed_time

    def reset(self):
        self.reset_timer()

        self.game_over_text.clear_text()

        self.clicks = 0
        self.clicks_text.clear_text()
        self.clicks_text.write_text(f'Clicks: {self.clicks}', 'center', 'Arial', 32, 'normal')

        self.count_clicks = True