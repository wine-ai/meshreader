# Grid Square Environmental Data Readout Program

The Grid Square Environmental Data Readout Program is a software that reads the attributes of each Grid Square feature using files generated by the Grid Square data generation program. This document contains specifications and instructions for using this program.

## Operating Environment

- Python 3.8 and the following libraries:
    - pandas v1.4.1
    - Pillow v8.0.0

## Environment Setup

```sh
pip install -r requirements.txt
```

※ It is also possible to run it using the Docker Image used in meshwriter.

## Meshdata Class Specification

### __init__(self, meshdata_dir: str, meshcode: str)

Constructor of the Meshdata class

- meshdata_dir (str): Parent folder of a group of folders named after Grid Square codes
- meshcode (str): Target 3rd level Grid Square code to be read

Note: The target period for the following time-series data is from January 1978 to December 2016.

### get_bbox() -> list

- Obtain the bounding box of the Grid Square as a one-dimensional array.

### get_precipitation(self) -> list

- Obtain time-series daily precipitation data as a one-dimensional array.

### get_daylight_hours(self) -> list:

- Obtain time-series daily sunlight duration data as a one-dimensional array.

### get_solar_radiation(self) -> list

- Obtain time-series daily accumulated solar radiation data as a one-dimensional array.

### get_average_temperature(self) -> list

- Obtain time-series daily average temperature data as a one-dimensional array.

### get_lowest_temperature(self) -> list

- Obtain time-series daily lowest temperature data as a one-dimensional array.

### get_maximum_temperature(self) -> list

- Obtain time-series daily highest temperature data as a one-dimensional array.

### get_landuse(self) -> dict

- Obtain land use area data of the Grid Square as a dictionary.

### get_elevation(self) -> list

- Obtain elevation distribution of the Grid Square as a two-dimensional list.

### get_slope(self) -> list

- Obtain slope angle distribution of the Grid Square as a two-dimensional list.

### get_direction(self) -> list

- Obtain slope direction distribution of the Grid Square as a two-dimensional list.

### get_geology(self) -> list

- Obtain geological pixel value distribution of the Grid Square as a two-dimensional list.

## Usage Example

In addition to the following, examples of implementation can also be found in `main()` within `__main__.py`.

```python
def main():
    meshdata = Meshdata(os.path.join("meshdata", "54381188"))
    
    # bbox (list)
    bbox = meshdata.get_bbox()
    print(bbox)
    
    # Time-series daily precipitation (list)
    precipitation = meshdata.get_precipitation()
    print(precipitation)
    
    # Time-series daily sunlight duration (list)
    daylight_hours = meshdata.get_daylight_hours()
    print(daylight_hours)
    
    # Time-series daily accumulated solar radiation (list)
    solar_radiation = meshdata.get_solar_radiation()
    print(solar_radiation)
    
    # Time-series daily average temperature (list)
    average_temperature = meshdata.get_average_temperature()
    print(average_temperature)
    
    # Time-series daily lowest temperature (list)
    lowest_temperature = meshdata.get_lowest_temperature()
    print(lowest_temperature)
    
    # Time-series daily highest temperature (list)
    maximum_temperature = meshdata.get_maximum_temperature()
    print(maximum_temperature)
    
    # Land use area (dict)
    landuse = meshdata.get_landuse()
    print(landuse)
    
    # Elevation distribution (list)
    elevation = meshdata.get_elevation()
    print(elevation)
    
    # Slope distribution (list)
    slope = meshdata.get_slope()
    print(slope)
    
    # Slope orientation distribution (list)
    direction = meshdata.get_direction()
    print(direction)
    
    # Geological pixel value distribution (list)
    geology = meshdata.get_geology()
    print(geology)
    
```

## Execution Method

- This program is a Python class, so it is intended to be called from a Python program, but its operation can also be confirmed with the following command:

```shell
cd meshreader
python __main__.py
```


