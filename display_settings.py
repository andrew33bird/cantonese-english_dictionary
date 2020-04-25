from kivy.properties import ListProperty, NumericProperty

# screen size
divisor = 2
x = 720 / divisor
y = 1280 / divisor

screen_y = NumericProperty(y)
screen_x = NumericProperty(x)

# typical widget height
height = x / 8
widget_height = NumericProperty(height)

tab_x = x / 2
tab_width = NumericProperty(tab_x)