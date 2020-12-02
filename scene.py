class Scene(object):

    def __init__(self, name, background=7):
        self.app = None  # set_app で設定する。
        self.pyi = None
        self.name = name
        self.background = background

    def set_app(self, app):
        self.app = app
        self.pyi = app.pyi  # pyxel instance for coding in methods.

    """
        pyxel更新メソッド
        @param pyi pyxelインスタンス。selfからも参照できるが、わざわざself.書くのもめんどくさいので渡してあげる。
        """

    def update(self, pyxel):
        pass

    """
        pyxel描写メソッド
        @param pyi pyxelインスタンス。selfからも参照できるが、わざわざself.書くのもめんどくさいので渡してあげる。
        """

    def draw(self, pyxel):
        pyxel.text(10, 10, "Hello world: Pyxel Scene Freamwork!", 0)


class Scenes(object):

    def __init__(self, app):
        self.app = app
        self.scenes = []
        self.focused_scene = Scene(name="**_temp_scene")  # default
        self.focused_scene.set_app(app)

    """
    新規シーンを作成し、そのインスタンスを返す。
    @param name 新規作成のシーン名
    """

    def register_scene(self, scene):
        scene.set_app(self.app)  # App instanceの登録
        self.scenes.append(scene)  # シーン一覧に登録する。
        return scene

    """
    メインシーンを切り替える
    @param name 新規作成のシーン名
    """

    def set_transition(self, name):
        for i in range(len(self.scenes)):
            scence = self.scenes[i]
            if scence.name == name:  # 名前が一致したら、それをメインシーンに設定する。
                self.focused_scene = scence

    """
    現在のメインシーンを返す。
    """

    def focused_scene(self):
        return self.focused_scene  # とりあえず、マインシーンを返す
