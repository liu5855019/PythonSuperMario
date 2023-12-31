screen_w = 800
screen_h = 600

game_fps = 60
game_fps_update_interval = 500
game_gravity = 1.0

bg_scale = 2.680
player_scale = 2.9


path_graphics = '../../resources/graphics'
path_mario = '../../resources/data/player/mario.json'
path_level1 = '../../resources/data/maps/level_1.json'

str_mario = 'mario'
str_mario_bros = 'mario_bros'
str_title_screen = 'title_screen'
str_item_objects = 'item_objects'
str_level = 'level'
str_level1 = 'level_1'
str_main_menu = 'main_menu'
str_load_screen = 'load_screen'
str_image_frames = 'image_frames'
str_right_small_normal = "right_small_normal"
str_right_big_normal = "right_big_normal"
str_right_big_fire = "right_big_fire"



font_name = 'FixedSys.ttf'
font_size = 40


color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_red = (255, 0, 0)
color_green = (0, 255, 0)
color_blue = (0, 0, 255)



if __name__ == '__main__':
    print(screen_w, screen_h)
