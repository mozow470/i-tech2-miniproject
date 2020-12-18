import math


class LinearGraph:

    def __init__(self, data_x, data_y, label_x, label_y, zoom=1.0, graph_size=[100, 100]):
        self.data_x, self.data_y = data_x, data_y
        self.zoom = zoom
        self.graph_size_x, self.graph_size_y = graph_size[0], graph_size[1]
        self.visual_data = []
        self.data_label = []
        self.label_x, self.label_y = label_x, label_y

    """
                描写に必要な変数を調整する
                @param zoom 拡大率
    """
    def calculate(self, zoom=1.0):
        if not len(self.data_x) == len(self.data_y):  # データの個数が一致しない
            raise BaseException("Cannot calculate for zip")

        self.zoom = zoom
        data_size = len(self.data_x)
        data_range_len = int(data_size * self.zoom)

        if data_range_len <= 0:  # 指数化しようがない
            self.visual_data = []
            self.data_label = []
            return

        # Divide 0を考慮する
        def get_max(data):
            result = max(data)
            return result if result > 0 else 1

        ad_data_x = self.data_x[0:data_range_len]
        ad_data_y = self.data_y[0:data_range_len]

        ad_label_x = self.label_x[0:data_range_len]
        ad_label_y = self.label_y[0:data_range_len]

        # グラフの描写サイズに合わせて指数化する
        data_x_max, data_y_max = get_max(ad_data_x), get_max(ad_data_y)
        index_data_x = [i / data_x_max * self.graph_size_x for i in ad_data_x]
        index_data_y = [i / data_y_max * self.graph_size_y for i in ad_data_y]

        # 束ねる
        self.visual_data = list(zip(index_data_x, index_data_y))
        self.data_label = list(zip(ad_label_x, ad_label_y))

    """
            Pyxelに描写する
            @param pyxel_app Pyxelオブジェクト
            @param x 描写するX座標
            @param y 描写するY座標
    """
    def render(self, pyxel_app, x, y, title="Title"):

        data_size = len(self.visual_data)

        # タイトルを表示
        pyxel_app.text(x, y - self.graph_size_y - 10, title, 0)

        # x,y軸を引く
        pyxel_app.line(x, y, x + self.graph_size_x, y, 0)
        pyxel_app.line(x, y, x, y - self.graph_size_y, 0)

        # ラベル感覚を調整する
        interval = self.graph_size_x / data_size if data_size > 0 else 99999.0
        interval_exp = 1

        max_label_y = 0

        while interval <= 15.0:  # ラベルの感覚が最低15px以上になるように
            interval_exp += 1
            interval = self.graph_size_x / (data_size / interval_exp)

        for k in range(data_size):
            v_data = self.visual_data[k]
            label_y = float(self.data_label[k][1])
            # x軸に点をつける。
            pyxel_app.circ(x + v_data[0], y, 1, 0)
            pyxel_app.circ(x + v_data[0], y - v_data[1], 1, 6)

            # ラベルを付ける。
            if k % interval_exp == 0:
                pyxel_app.text(x + v_data[0] - 4, y + 10, str(round(self.data_label[k][0], 2)), 2)
                # pyxel_app.text(x-20, y-v_data[1], str(round(self.data_label[k][1], 2)) ,2)

            if max_label_y < label_y:
                max_label_y = label_y

            # グラフの変化率を描く。
            if k < len(self.visual_data) - 1:
                v_data_next = self.visual_data[k + 1]
                pyxel_app.line(x + v_data[0], y - v_data[1], x + v_data_next[0], y - v_data_next[1], 6)

        pyxel_app.text(x-18, y - self.graph_size_y, str(int(max_label_y)), 2)
