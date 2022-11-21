import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-s",
    "--scene",
    default=1,
    type=int,
)
args = parser.parse_args()

current_scene = args.scene
lidarseg_file = json.load(open('../V2X-Sim-2/v1.0-mini/lidarseg.json'))
lidarseg = []

for ii in lidarseg_file:
    if f'scene_{current_scene}_' in ii['filename']:
        lidarseg.append(ii)

with open(f'./v2.0-mini/lidarseg.json', 'w') as f:
        json.dump(lidarseg, f, indent=4)