import pyxel

from scene import Scenes
from scenes.test_scene import TestScene
from scenes.main_scene import MainScene
from scenes.game_scene import GameScene
from scenes.statistics_scene import StatisticsScene
from scenes.countdown_scene import CountdownScene
from scenes.result_scene import ResultScene

from store import make_store_files, Store


class App:

    def __init__(self):
        self.pyi = pyxel
        self.store = Store(app=self);
        self.scenes_manager = Scenes(app=self)

        make_store_files()  # make an store file if not exit in working folder.
        self.store.import_from_store()

        register_scenes = [
            TestScene(name="test_scene"),  # シーンを登録
            MainScene(name="main_scene"),
            GameScene(name="game_scene"),
            StatisticsScene(name="statistics_scene"),
            CountdownScene(name="countdown_scene"),
            ResultScene(name="result_scene")

        ]
        for i in range(len(register_scenes)):
            self.scenes_manager.register_scene(register_scenes[i])  # シーンを登録

        self.scenes_manager.transition("main_scene")  # 初期のシーンを設定
        # self.scenes_manager.transition("game_scene")  # 初期のシーンを設定(Dev)

        pyxel.init(200, 200)
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.scenes_manager.focused_scene.update(pyxel=pyxel)

    def draw(self):
        focused_scene = self.scenes_manager.focused_scene  # get object

        pyxel.cls(focused_scene.background)
        focused_scene.draw(pyxel=pyxel)


App()
