from kivy.properties import (ListProperty, NumericProperty, StringProperty)

# screen size
divisor = 2
x = 720 / divisor
y = 1280 / divisor

screen_y = NumericProperty(y)
screen_x = NumericProperty(x)

# typical widget height
height = x / 8
widget_height = NumericProperty(height)
small_height = height / 2
small_widget_height = NumericProperty(small_height)
# tab width
tab_x = x / 2
tab_width = NumericProperty(tab_x)
# scroll list height
scroll_height = height / 2
scroll_row_height = NumericProperty(scroll_height)
# advanced filters width
width = x * 2 / 5
adv_filt_width = NumericProperty(width)

# font sizes
font_header_normal = NumericProperty(24)
font_normal = NumericProperty(18)

# colors by type
# tab colors
color_tab_down = ListProperty([0xee/255, 0xe8/255, 0xd5/255, 1])
color_tab_normal = ListProperty([0x83/255, 0x94/255, 0x96/255, 1])
color_tab_text_down = ListProperty([0x83/255, 0x94/255, 0x96/255, 1])
color_tab_text_normal = ListProperty([0xee/255, 0xe8/255, 0xd5/255, 1])
# text box colors
textbox_color_bckgnd = ListProperty([0xfd/255, 0xf6/255, 0xe3/255, 1])
textbox_color_text = ListProperty([0, 0x2b/255, 0x36/255, 1])
#scroll list colors
color_row_1 = ListProperty([0, 0x2b/255, 0x36/255, 1])
color_row_2 = ListProperty([0x07/255, 0x36/255, 0x42/255, 1])
# global colors
color_background = ListProperty([0, 0x2b/255, 0x36/255, 1])
color_text = ListProperty([0xfd/255, 0xf6/255, 0xe3/255, 1])

# button images
settings_btn_normal = StringProperty('images/settings_normal.png')
settings_btn_down = StringProperty('images/settings_down.png')
search_btn_normal = StringProperty('images/search_normal.png')
search_btn_down = StringProperty('images/search_down.png')
adv_filter_colapse = StringProperty('images/adv_filter_colapse.png')
adv_filter_expand = StringProperty('images/adv_filter_expand.png')