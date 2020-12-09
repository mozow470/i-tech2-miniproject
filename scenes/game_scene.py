import scene
from random import randint, random


class Ball(object):

    def __init__(self, game, x, y, radius=10):
        self.game = game
        self.radius = radius
        self.xy = [x, y]
        self.is_trick = random() <= 0.15 # 15%の確立

    def is_clicked(self, x, y):
        vec = self.xy[0] - x, self.xy[1] - y  # マウスの位置から、オブジェクトの中心座標に向いたベクトル
        vec_size = abs(vec[0]) + abs(vec[1])  # 単位を揃えたいので絶対値でベクトルの大きさを求める
        accurate: float = float(vec_size) / float(self.radius + 2)
        return accurate  # ハズレ度合い 0<=x<=1 .. 円の中をクリックした、 1<x .. 円の外

    def transition(self):
        self.radius = self.radius * 0.99  # 徐々にボールを小さくしてみる

        if self.radius <= 1:  # 直径が1以下になったら、当たり判定を初期化する。
            self.reset(x=randint(10, 190), y=randint(10, 190))
            if not self.is_trick:
                self.game.count_miss()  # ミスをカウント

    def reset(self, x, y):
        self.xy[0] = x
        self.xy[1] = y
        self.radius = randint(10, 20)
        self.is_trick = random() <= 0.15  # 15%の確立

    def get_color(self):
        return 9 if self.is_trick else 8


class GameScene(scene.Scene):

    def __init__(self, name):
        super().__init__(name)  # スーパークラス Omajinai
        self.ball_count = 4  # ボール（当たり判定の個数）
        self.limit_of_miss = 5  # ミス許容範囲
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
                accurate = ball.is_clicked(mouse_xy[0], mouse_xy[1])  # クリック精度を取得

                if accurate <= 1:  # ボールをクリックした
                    if ball.is_trick: # クリックしてはいけないトリックボールをクリックした。
                        self.point -= 50
                        if self.point < 0:
                            self.point = 0
                    else:
                        adj_acc = 1 - accurate  # 余事象
                        point = int(100 * adj_acc)  # point
                        self.point += point
                        self.accuracies.append(adj_acc)
                        self.accuracy = round(sum(self.accuracies) / len(self.accuracies) * 100.0, 1)  # 精度％を求める。
                        ball.reset(x=randint(10, 190), y=randint(10, 190))  # 個体情報をリセットする。

    def draw(self, pyxel):
        # pyxel.text(10, 10, "Point: {}".format(self.point), 0)
        pyxel.text(10, 20, "Miss: {}/{}".format(self.miss_count, self.limit_of_miss), 8)
        pyxel.text(10, 10, "Accuracy: {}%".format(self.accuracy), 0)
        for i in range(len(self.balls)):
            ball = self.balls[i]
            pyxel.circ(ball.xy[0], ball.xy[1], ball.radius, ball.get_color())

    def create_ball(self):
        return Ball(game=self, x=randint(10, 190), y=randint(10, 190), radius=randint(10, 30))

    def before_render(self, pyxel, parameters):
        self.point = 0  # reset point for next game.
        self.accuracy = 0
        self.miss_count = 0
        self.accuracies = []
        self.balls = [self.create_ball() for i in range(self.ball_count)]

    def count_miss(self):
        self.miss_count += 1
        if self.miss_count >= self.limit_of_miss:  # 10会ミスった
            self.app.scenes_manager.transition("result_scene", point=self.point, accuracy=self.accuracy)  # リザルト画面へ
