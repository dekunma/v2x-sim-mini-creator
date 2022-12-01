import os
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-s",
    "--scene",
    default=1,
    type=int,
)
parser.add_argument(
    "--base_dir",
    default="/scratch/dm4524/data/V2X-Sim-2",
    type=str,
    help="Path to V2X-Sim dataset"
)
args = parser.parse_args()

current_scene = args.scene

from_dir = os.path.join(args.base_dir, 'v1.0-mini', 'lidarseg.json')

lidarseg_file = json.load(open(from_dir))
lidarseg = []

for ii in lidarseg_file:
    if f'scene_{current_scene}_' in ii['filename']:
        lidarseg.append(ii)

with open(f'./v2.0-mini/lidarseg.json', 'w') as f:
        json.dump(lidarseg, f, indent=4)