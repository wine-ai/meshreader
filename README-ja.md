# メッシュデータ読み出しプログラム

メッシュデータ読み出しプログラムとは、メッシュデータ生成プログラムで生成したファイルをもちいて、 各メッシュ地物の属性を読み出すプログラムです。 本書は、本プログラムの仕様・使用方法などを記載するものである。

## 動作環境

- Python 3.8および下記のライブラリ
    - pandas v1.4.1
    - Pillow v8.0.0

## 環境構築

```sh
pip install -r requirements.txt
```

※なお、meshwriterで用いたDockerImageでも実行可能です。

## Meshdataクラス仕様

### __init__(self, meshdata_dir: str, meshcode: str)

Meshdataクラスのコンストラクタ

- meshdata_dir (str): フォルダ名がメッシュコードになっているフォルダ群の親フォルダ
- meshcode (str): 読み込み対象の3次メッシュコード


注：下記の時系列データの対象期間は1978-01-01 ~ 2016-12-31となる

### get_bbox() -> list

- メッシュの領域を1次元配列で得る

### get_precipitation(self) -> list

- 時系列日降水量データを1次元配列で得る

### get_daylight_hours(self) -> list:

- 時系列日照時間データを1次元配列で得る

### get_solar_radiation(self) -> list

- 時系列日積算日射量データを1次元配列で得る

### get_average_temperature(self) -> list

- 時系列日平均気温データを1次元配列で得る

### get_lowest_temperature(self) -> list

- 時系列日最低気温データを1次元配列で得る

### get_maximum_temperature(self) -> list

- 時系列日最高気温データを1次元配列で得る

### get_landuse(self) -> dict

- 当該メッシュ土地利用面積データを辞書で得る

### get_elevation(self) -> list

- 当該メッシュ標高値分布を2次元のlistで得る

### get_slope(self) -> list

- 当該メッシュ傾斜角分布を2次元のlistで得る

### get_direction(self) -> list

- 当該メッシュ傾斜方向分布を2次元のlistで得る

### get_geology(self) -> list

- 当該メッシュ地質ピクセル値分布を2次元のlistで得る

## 使用例

下記に加え、`__main__.py`内、`main()`でも実装例を確認することができます。

```python
def main():
    meshdata = Meshdata(os.path.join("meshdata", "54381188"))
    
    # bbox(list)
    bbox = meshdata.get_bbox()
    print(bbox)
    
    # 時系列日降水量(list)
    precipitation = meshdata.get_precipitation()
    print(precipitation)
    
    # 時系列日照時間(list)
    daylight_hours = meshdata.get_daylight_hours()
    print(daylight_hours)
    
    # 時系列日積算日射量(list)
    solar_radiation = meshdata.get_solar_radiation()
    print(solar_radiation)
    
    # 時系列日平均気温(list)
    average_temperature = meshdata.get_average_temperature()
    print(average_temperature)
    
    # 時系列日最低気温データ(list)
    lowest_temperature = meshdata.get_lowest_temperature()
    print(lowest_temperature)
    
    # 時系列日最高気温データ(list)
    maximum_temperature = meshdata.get_maximum_temperature()
    print(maximum_temperature)
    
    # 土地利用面積(dict)
    landuse = meshdata.get_landuse()
    print(landuse)
    
    # 標高分布(list)
    elevation = meshdata.get_elevation()
    print(elevation)
    
    # 傾斜分布(list)
    slope = meshdata.get_slope()
    print(slope)
    
    # 傾斜方位分布(list)
    direction = meshdata.get_direction()
    print(direction)
    
    # 地質ピクセル値分布(list)
    geology = meshdata.get_geology()
    print(geology)
    
```

## 実行方法

- 本プログラムはPythonのクラスなので、Pythonプログラムから呼び出されることを想定していますが、下記コマンドでも動作を確認することができます。

```shell
cd meshreader
python __main__.py
```
