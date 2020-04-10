import argparse, json, csv, math
from datetime import datetime

parser = argparse.ArgumentParser(description='Convert Google\'s location data from JSON format to CSV')
parser.add_argument('input', type=str, help='path to input JSON file.')
parser.add_argument('output', type=str, help='path to output csv file.')

args = parser.parse_args()
file = open(args.input)
data = json.load(file)
locations = data['locations']
with open(args.output, 'w') as csvfile:
    fw = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    fw.writerow(['timestamp', 'latitude', 'longitude'])
    for l, location in enumerate(locations):
      timestamp = datetime.utcfromtimestamp(int(location['timestampMs']) / 1000)
      fw.writerow([timestamp, float(location['latitudeE7'])/math.pow(10, 7), float(location['longitudeE7'])/math.pow(10, 7)])

print("Conversion Done!")