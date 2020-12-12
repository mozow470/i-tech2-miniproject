import os
import pathlib
import datetime

STORE_FILE_NAME = "store.log"  # Default name for store system

"""
   Workinディレクトリを取得する
"""


def get_store_path():
    return pathlib.Path(os.getcwd()).resolve()


"""
   Logファイルを作成する。
"""


def make_store_files(default=STORE_FILE_NAME):
    logs_folder = get_store_path()
    try:
        store_file = logs_folder.joinpath(default)
        if not store_file.exists():
            store_file.touch()
            print("** ストアファイルを作成しました: {}".format(store_file))
    except OSError as excp:
        print("** ストアファイルの作成に失敗しました。プレイデータは保存されません. {}".format(excp))


class Store(object):

    def __init__(self, app, default=STORE_FILE_NAME):
        self.app = app
        self.file_path = default
        self.records = []

    """
       Storeファイルを読み込む
    """

    def import_from_store(self):
        try:
            store_file = get_store_path().joinpath(self.file_path)
            with store_file.open(mode="r", encoding="utf-8") as file:
                records = file.readlines()
                for i in range(len(records)):
                    record = records[i].split(" ")
                    self.records.append(record)
                file.close()
        except OSError as excp:
            print("** ストアファイルの読み込みに失敗しました。プレイデータは保存されません. {}".format(excp))

    """
       Storeに追加、および書き込み
       @param point 結果のポイント
       @param accuracy 結果の精度
    """

    def push_to_store(self, *values):
        now_unix = datetime.datetime.now().timestamp()
        now_unix = str(now_unix)  # convert to string
        mapped_values = map(str, values)  # joinを使うから
        try:
            store_file = get_store_path().joinpath(self.file_path)
            with store_file.open(mode="a", encoding="utf-8") as file:
                file.writelines("{} {}\n".format(now_unix, " ".join(mapped_values)))  # one record per one line
                file.close()
            print([now_unix, *values])
            self.records.append([now_unix, *values])
        except OSError as excp:
            print("** ストアファイルの書き込みに失敗しました。プレイデータは保存されません. {}".format(excp))
