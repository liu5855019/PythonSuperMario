import  pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.setup_states()
        self.setup_timers()
        self.setup_velocities()
        self.load_images()

    def setup_states(self):
        self.face_right = True
        self.dead = False
        self.big = False

    def setup_velocities(self):
        ###
        # 设置速度相关
        ###
        self.velocity_x = 0
        self.velocity_y = 0

    def setup_timers(self):
        pass

    def load_images(self):
        pass

    def update(self, surface: pygame.Surface, keys):
        pass

    def draw(self, surface: pygame.Surface,):
        pass
