from typing import List, Any, Tuple

import scene
from random import randint, random


class Preset(object):

    def __init__(self, name="Easy", ball_count=4, limit_of_miss=5, rate_of_trick=0.1):
        self.name = name  # Preset name
        self.ball_count = ball_count  # ボール（当たり判定の個数）
        self.limit_of_miss = limit_of_miss  # ミス許容範囲
        self.rate_of_trick = rate_of_trick  # トリックボール率


class Ball(object):

    is_trick: bool
    radius: float
    xy: Tuple[int, int]

    def __init__(self, game, x, y, radius=10):
        self.game = game
        self.reset(x, y)

    def get_accuracy(self, x, y):
        vec = self.xy[0] - x, self.xy[1] - y  # マウスの位置から、オブジェクトの中心座標に向いたベクトル
        vec_size = abs(vec[0]) + abs(vec[1])  # 単位を揃えたいので絶対値でベクトルの大きさを求める
        accurate: float = float(vec_size) / float(self.radius + 2)
        return accurate  # ハズレ度合い 0<=x<=1 .. 円の中をクリックした、 1<x .. 円の外

    def transition(self):
        self.radius = self.radius * 0.99  # 徐々にボールを小さくしてみる

        if self.radius <= 1:  # 直径が1以下になったら、当たり判定を初期化する。
            if not self.is_trick:
                self.game.count_miss()  # ミスをカウント
                self.game.pyi.play(0, 1)
            self.reset(x=randint(10, 190), y=randint(10, 190))

    def reset(self, x, y):
        self.xy = x, y
        self.radius = float(randint(10, 20))
        self.is_trick = random() <= self.game.rate_of_trick  # 15%の確立

    def get_color(self):
        return 9 if self.is_trick else 8


class GameScene(scene.Scene):

    balls: List[Ball]
    miss_count: int
    accuracy: float
    accuracies: List[Any]
    point: int
    preset_name: str
    rate_of_trick: float
    limit_of_miss: int
    ball_count: int

    def __init__(self, name):
        super().__init__(name)  # スーパークラス Omajinai
        self.reset(Preset())  # Load default preset

    def reset(self, preset: Preset):
        # プリセットからパラメータを読み込む（副作用防止のため、値を渡すだけ。）
        self.ball_count = preset.ball_count
        self.limit_of_miss = preset.limit_of_miss
        self.rate_of_trick = preset.rate_of_trick
        self.preset_name = preset.name

        # 処理用
        self.point = 0
        self.accuracies = []
        self.accuracy = 0.0
        self.miss_count = 0
        self.balls = [self.create_ball() for i in range(self.ball_count)]

    def update(self, pyxel):
        if pyxel.btn(pyxel.KEY_Q):
            self.app.scenes_manager.transition("main_scene")

        mouse_xy = pyxel.mouse_x, pyxel.mouse_y
        is_clicked = pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON)

        for i in range(len(self.balls)):
            ball = self.balls[i]
            ball.transition()  # 小さくなっていく

            if is_clicked:
                accurate = ball.get_accuracy(mouse_xy[0], mouse_xy[1])  # クリック精度を取得

                if accurate <= 1:  # ボールをクリックした
                    if ball.is_trick:  # クリックしてはいけないトリックボールをクリックした。
                        self.point -= 50
                        if self.point < 0:
                            self.point = 0
                        pyxel.play(0, 1)

                    else:
                        adj_acc = 1 - accurate  # 余事象
                        point = int(100 * adj_acc)  # point
                        self.point += point
                        self.accuracies.append(adj_acc)
                        self.accuracy = round(sum(self.accuracies) / len(self.accuracies) * 100.0, 1)  # 精度％を求める。
                        ball.reset(x=randint(10, 190), y=randint(10, 190))  # 個体情報をリセットする。
                        pyxel.play(0, 0)
                continue

    def draw(self, pyxel):
        # pyxel.text(10, 10, "Point: {}".format(self.point), 0)
        pyxel.text(10, 20, "Miss: {}/{}".format(self.miss_count, self.limit_of_miss), 8)
        pyxel.text(10, 10, "Accuracy: {}%".format(self.accuracy), 0)
        for i in range(len(self.balls)):
            ball = self.balls[i]
            pyxel.circ(ball.xy[0], ball.xy[1], ball.radius, ball.get_color())

    def create_ball(self):
        return Ball(game=self, x=randint(10, 190), y=randint(10, 190), radius=randint(10, 30))

    def before_render(self, pyxel, parameters, before):
        preset = parameters["preset"]
        self.reset(preset=preset)  # load preset
        print("[Game] Game Mode:", preset.name)

    def count_miss(self):
        self.miss_count += 1
        if self.miss_count >= self.limit_of_miss:  # 10会ミスった
            self.app.scenes_manager.transition("result_scene", point=self.point, accuracy=self.accuracy,
                                               preset_name=self.preset_name)  # リザルト画面へ
