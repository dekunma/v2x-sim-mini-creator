import os
import shutil
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

base_dir = os.path.join(args.base_dir, 'sweeps')

for sweep in os.listdir(base_dir):
    from_dir = os.path.join(base_dir, sweep)
    to_dir = f'./sweeps/{sweep}'
    os.makedirs(to_dir, exist_ok=True)
    for file in os.listdir(from_dir):
        if file.startswith(f'scene_{current_scene}_'):
            shutil.copy(os.path.join(from_dir, file), to_dir)