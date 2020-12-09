import os
import pathlib
import datetime

STORE_FILE_NAME = "store.log"


def get_store_path():
    return pathlib.Path(os.getcwd()).resolve()


def make_store_files():
    logs_folder = get_store_path()
    try:
        store_file = logs_folder.joinpath(STORE_FILE_NAME)
        if not store_file.exists():
            store_file.touch()
            print("** ストアファイルを作成しました: {}".format(store_file))
    except OSError as excp:
        print("** ストアファイルの作成に失敗しました。プレイデータは保存されません. {}".format(excp))


class Store(object):

    def __init__(self, app):
        self.app = app
        self.records = []

    """
       Storeファイルを読み込む
    """
    def import_from_store(self):
        try:
            store_file = get_store_path().joinpath(STORE_FILE_NAME)
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
    def push_to_store(self, point, accuracy):
        now_unix = datetime.datetime.now().timestamp()
        try:
            store_file = get_store_path().joinpath(STORE_FILE_NAME)
            with store_file.open(mode="a", encoding="utf-8") as file:
                file.writelines("{} {} {}\n".format(now_unix, point, accuracy))
                file.close()
            self.records.append([now_unix, point, accuracy])
        except OSError as excp:
            print("** ストアファイルの書き込みに失敗しました。プレイデータは保存されません. {}".format(excp))