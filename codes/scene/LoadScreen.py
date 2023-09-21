from codes.scene import BaseScene
from codes.common import consts


class LoadScreen(BaseScene.BaseScene):

    def __init__(self):
        BaseScene.BaseScene.__init__(self)
        self.next = consts.strLoadScreen

    def update(self, surface, keys):
        pass

    def draw(self, surface):
        surface.fill(consts.colorBlue)

