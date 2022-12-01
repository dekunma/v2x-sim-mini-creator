import os
import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "--base_dir",
    default="/scratch/dm4524/data/V2X-Sim-2",
    type=str,
    help="Path to V2X-Sim dataset"
)
args = parser.parse_args()
from_directory = os.path.join(args.base_dir, 'v1.0-mini')

other_meta_data_files = ['attribute', 'category', 'log', 'map', 'sensor', 'visibility']

for ii in other_meta_data_files:
    shutil.copy(os.path.join(from_directory, f'{ii}.json'), './v2.0-mini')