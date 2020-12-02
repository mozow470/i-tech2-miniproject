import pyxel
from scene import Scenes
from scenes.test_scene import TestScene


class App:

    def __init__(self):
        self.pyi = pyxel
        self.scenes_manager = Scenes(app=self)
        register_scenes = [TestScene(name="test_scene")]

        for i in range(len(register_scenes)):
            self.scenes_manager.register_scene(register_scenes[i])  # シーンを登録
        self.scenes_manager.set_transition("test_scene")  # 初期のシーンを設定

        pyxel.init(200, 200)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.scenes_manager.focused_scene().update(pyxel=pyxel)

    def draw(self):
        focused_scene = self.scenes_manager.focused_scene()  # get object

        pyxel.cls(focused_scene.background)
        focused_scene.draw(pyxel=pyxel)


App()
