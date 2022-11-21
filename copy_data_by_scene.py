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
args = parser.parse_args()
current_scene = args.scene

for sweep in os.listdir('../V2X-Sim-2/sweeps'):
    from_dir = f'../V2X-Sim-2/sweeps/{sweep}'
    to_dir = f'./sweeps/{sweep}'
    os.makedirs(to_dir, exist_ok=True)
    for file in os.listdir(from_dir):
        if file.startswith(f'scene_{current_scene}_'):
            shutil.copy(os.path.join(from_dir, file), to_dir)