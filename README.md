Google provides all your data through their Takeout platform. The location data is by default in json format, however most analysis and visualization tools(like Uber's Kepler.gl) online accept a csv file.

***
# Convert Google's location data from JSON format to CSV

positional arguments:
  input       path to input JSON file.
  output      path to output csv file.

optional arguments:
  -h, --help  show this help message and exit
***
# Usage
  ```python3 formatconvertor.py <input> <output> ```
