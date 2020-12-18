class Scene(object):

    def __init__(self, name, background=7):
        self.app = None  # set_app で設定する。
        self.pyi = None
        self.name = name
        self.background = background

    """
            アプリインスタンスを登録する
            @param app 登録するアプリインスタンス
            """
    def set_app(self, app):
        self.app = app
        self.pyi = app.pyi  # pyxel instance for coding in methods.
        self.on_registered(self.pyi)

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
        pyxel.text(10, 10, "Hello world: Pyxel Scene Framework!", 0)

    """
           このコンポーネントにトランジションする前に呼ばれる関数. before_transitionよりも前に呼び出されます。
           @param pyi pyxelインスタンス。selfからも参照できるが、わざわざself.書くのもめんどくさいので渡してあげる。
           """

    def before_render(self, pyxel, parameters, before):
        pass

    """
               他コンポーネントにトランジションする前に呼ばれる関数
               @param pyi pyxelインスタンス。selfからも参照できるが、わざわざself.書くのもめんどくさいので渡してあげる。
               """

    def before_transition(self, pyxel):
        pass

    """
        シーンオブジェクトに登録後、呼び出されるメソッド。サウンド等を定義する。
        @param pyi pyxelインスタンス。selfからも参照できるが、わざわざself.書くのもめんどくさいので渡してあげる。
                  """

    def on_registered(self, pyxel):
        pass


class Scenes(object):

    def __init__(self, app):
        self.app = app
        self.scenes = []
        self.focused_scene = Scene(name="_init_hello_world_scene")  # default
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

    def transition(self, name, **parameters):
        prev_scene = self.focused_scene
        for i in range(len(self.scenes)):
            scene = self.scenes[i]
            if scene.name == name and prev_scene.name != name:  # 名前が一致したら、それをメインシーンに設定する。
                prev_scene.before_transition(self.app.pyi)  # イベントを呼び出す。
                scene.before_render(self.app.pyi, parameters=parameters, before=prev_scene.name)
                self.focused_scene = scene
