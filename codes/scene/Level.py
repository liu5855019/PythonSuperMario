from codes.scene import BaseScene
from codes.common import consts


class Level(BaseScene.BaseScene):
    def __init__(self):
        BaseScene.BaseScene.__init__(self)
        self.next = consts.strLevel1

    def update(self, surface, keys):
        pass

    def draw(self, surface):
        surface.fill(consts.colorWhite)

