import os

import numpy as np
import pandas as pd
from PIL import Image


class Meshdata:
    """
    メッシュデータ読み出しクラス
    """

    def __init__(self, meshdata_dir: str, meshcode: str):
        """
        インスタンス化の時にmeshwriterで書き出されたメッシュデータのディレクトリを指定する

        Args:
            meshdata_dir (str): フォルダ名がメッシュコードになっているフォルダ群の親フォルダ
            meshcode (str): 3次メッシュコード
        """
        self.meshdata_dir = meshdata_dir
        self.meshcode = meshcode
        self.read_pickle = pd.read_pickle(os.path.join(
            meshdata_dir, meshcode, "meshdata.pickle"))

        self.hex_json_dir = os.path.join(meshdata_dir, "geology_hex.json")

    def get_bbox(self) -> list:
        bbox = [
            self.read_pickle["minx"],
            self.read_pickle["miny"],
            self.read_pickle["maxx"],
            self.read_pickle["maxy"],
        ]
        return bbox

    def get_precipitation(self) -> list:
        """
        時系列日降水量データを1次元配列で得る
        対象期間: 1978-01-01 ~ 2016-12-31

        Returns:
            list: list of int
        """
        precipitation = self.read_pickle["日降水量"]

        return precipitation

    def get_daylight_hours(self) -> list:
        """
        時系列日照時間データを1次元配列で得る
        対象期間: 1978-01-01 ~ 2016-12-31

        Returns:
            list: list of int
        """
        daylight_hours = self.read_pickle['日照時間']
        return daylight_hours

    def get_solar_radiation(self) -> list:
        """
        時系列日積算日射量データを1次元配列で得る
        対象期間: 1978-01-01 ~ 2016-12-31

        Returns:
            list: list of int
        """
        solar_radiation = self.read_pickle['日積算日射量']
        return solar_radiation

    def get_average_temperature(self) -> list:
        """
        時系列日平均気温データを1次元配列で得る
        対象期間: 1978-01-01 ~ 2016-12-31

        Returns:
            list: list of float
        """
        average_temperature = self.read_pickle['日平均気温']
        return average_temperature

    def get_lowest_temperature(self) -> list:
        """
        時系列日最低気温データを1次元配列で得る
        対象期間: 1978-01-01 ~ 2016-12-31

        Returns:
            list: list of float
        """
        lowest_temperature = self.read_pickle['日最低気温']
        return lowest_temperature

    def get_maximum_temperature(self) -> list:
        """
        時系列日最高気温データを1次元配列で得る
        対象期間: 1978-01-01 ~ 2016-12-31

        Returns:
            list: list of float
        """
        maximum_temperature = self.read_pickle['日最高気温']
        return maximum_temperature

    def get_landuse(self) -> dict:
        """
        土地利用面積データを得る
        Returns:
            dict: {
                "田": int,
                "他農用地": int,
                "森林": int,
                "荒地": int,
                "建物用地": int,
                "道路": int,
                "鉄道": int,
                "他用地": int,
                "河川湖沼": int,
                "海浜": int,
                "海水域": int,
                "ゴルフ場": int,
            }
        """
        landuse = {
            "田": self.read_pickle["田"],
            "他農用地": self.read_pickle["他農用地"],
            "森林": self.read_pickle["森林"],
            "荒地": self.read_pickle["荒地"],
            "建物用地": self.read_pickle["建物用地"],
            "道路": self.read_pickle["道路"],
            "鉄道": self.read_pickle["鉄道"],
            "他用地": self.read_pickle["他用地"],
            "河川湖沼": self.read_pickle["河川湖沼"],
            "海浜": self.read_pickle["海浜"],
            "海水域": self.read_pickle["海水域"],
            "ゴルフ場": self.read_pickle["ゴルフ場"],
        }
        return landuse

    def get_elevation(self) -> list:
        """
        当該メッシュの標高値分布を2次元のlistで得る
        """
        with Image.open(os.path.join(self.meshdata_dir, self.meshcode, "dem.png")) as im:
            elevation_list = self.decode_datapng(im)
        return elevation_list

    def get_slope(self) -> list:
        """
        当該メッシュの傾斜角分布を2次元のlistで得る
        """
        with Image.open(os.path.join(self.meshdata_dir, self.meshcode, "slope.png")) as im:
            slope_list = self.decode_datapng(im)
        return slope_list

    def get_direction(self) -> list:
        """
        当該メッシュの傾斜方向分布を2次元のlistで得る
        """
        with Image.open(os.path.join(self.meshdata_dir, self.meshcode, "direction.png")) as im:
            direction_list = self.decode_datapng(im)
        return direction_list

    def decode_datapng(self, im) -> list:
        """
        産総研データPNGを実数値にデコードする

        Args:
            im (PIL.Image): PNG画像のPIL.Imageインスタンス

        Returns:
            _type_: RGB値を実数値にデコードした2次元のnumpy.array
        """
        rgb_array = np.array(im, np.float64)
        mask_null = (rgb_array[:, :, 0] == 128) * \
                    (rgb_array[:, :, 1] == 0) * (rgb_array[:, :, 2] == 0)
        mask_over = (rgb_array[:, :, 0] >= 128) * \
                    (rgb_array[:, :, 1] >= 0) * (rgb_array[:, :, 2] >= 1)

        value_array = (rgb_array[:, :, 0] * 256 * 256 +
                       rgb_array[:, :, 1] * 256 + rgb_array[:, :, 2]) * 0.01
        value_array[mask_null] = None
        value_array[mask_over] -= 2 ** 24

        return value_array.tolist()

    def hex_to_detial(self) -> dict:
        """hexと対応する地質情報を読み込んで辞書を作成する"""
        return dict(pd.read_json(self.hex_json_dir).values.tolist())

    def read_geologypng_to_hexdf(self) -> pd.DataFrame:
        """
        当該メッシュの地質分布（rgb）をpd.dataframe(hex)で得る
        """

        with Image.open(os.path.join(self.meshdata_dir, self.meshcode, "geology.png")) as im:
            rgb_2d = np.array(im, dtype=np.uint8)

        geology_list = []
        for row in rgb_2d:
            geology_list.append(list(map(self.rgb2hex, row)))

        geology_df = pd.DataFrame(geology_list)

        return geology_df

    def rgb2hex(self, rgb) -> str:
        """
        リスト[R,G,B]のデータ量を減らすためにhex(文字列)に変換
        """
        return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

    def get_geology(self) -> list:
        """
        当該メッシュの地質情報分布を2次元のlistで得る
        """
        png_to_hex = self.read_geologypng_to_hexdf()
        geology = png_to_hex.replace(self.hex_to_detial()).values.tolist()

        return geology


def main():
    meshdata = Meshdata("sampledata", "54382129")

    geology = meshdata.get_geology()
    precipitation = meshdata.get_precipitation()
    direction = meshdata.get_direction()
    radiation = meshdata.get_solar_radiation()

    print(geology[10][20], precipitation[10], direction[10][20], radiation[10])


if __name__ == "__main__":
    main()
