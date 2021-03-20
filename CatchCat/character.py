import turtle

class Character(object):
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
        self.screen = screen
        self.color = color
        self.shape = shape
        self.shape_size = shape_size
        self.head_turn = head_turn
        self.speed = speed
        self.turn_angle_right = turn_angle_right
        self.turn_angle_left = turn_angle_left
        self.increase_speed_amount = increase_speed_amount
        self.decrease_speed_amount = decrease_speed_amount
        self.x_min_border = x_min_border
        self.x_max_border = x_max_border
        self.y_min_border = y_min_border
        self.y_max_border = y_max_border
        self.x_position = x_position
        self.y_position = y_position
        self.width = width
        self.hide_character = hide_character

        self.character = turtle.Turtle()
        self.character.penup()
        self.character.width(self.width)
        self.character.color(self.color)
        self.character.shapesize(self.shape_size)
        self.character.setheading(self.head_turn)
        self.character.speed(self.speed)

        if self.hide_character == True:
            self.character.hideturtle()
        elif self.hide_character == False:
            self.character.showturtle()
        else:
            print('Error: Unknown bolean at "hide_character"!')

        self.character.setposition(self.x_position, self.y_position)

    def move(self):
        self.character.forward(self.speed)

        if self.character.xcor() > self.x_max_border:
            self.character.setx(self.x_max_border)
        if self.character.xcor() < self.x_min_border:
            self.character.setx(self.x_min_border)
        if self.character.ycor() > self.y_max_border:
            self.character.sety(self.y_max_border)
        if self.character.ycor() < self.y_min_border:
            self.character.sety(self.y_min_border)

    def turn_left(self):
        self.character.left(self.turn_angle_right)

    def turn_right(self):
        self.character.right(self.turn_angle_left)

    def increase_speed(self):
        self.speed += self.increase_speed_amount
        print(self.speed)

    def decrease_speed(self):
        self.speed -= self.decrease_speed_amount
        print(self.speed)

    def go_to_mouse(self):
        self.screen.onclick(self.set_heading_mouse)

    def set_heading_mouse(self, x, y):
        self.character.setheading(self.character.towards(x, y))

    def stay(self):
        self.stay_at_place = True

        while self.stay_at_place:
            self.character.setposition(self.character.xcor(), self.character.ycor())

    def free_move(self):
        self.stay_at_place = False

    def set_photo(self, photo):
        self.photo = photo

        self.screen.register_shape(self.photo)
        self.character.shape(self.photo)