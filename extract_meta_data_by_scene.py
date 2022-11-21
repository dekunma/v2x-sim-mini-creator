import json
import os
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
from_directory = '../V2X-Sim-2/v1.0-mini'

class V2XMetaData:
    def __init__(self, name) -> None:
        self.name = name
        self.data = []
        self.ids = set()
        self.file = json.load(open(os.path.join(from_directory, f'{name}.json')))

file_names = ['scene', 'sample', 'sample_annotation', 'instance', 'sample_data', 'ego_pose', 'calibrated_sensor']
meta_data_list = {name : V2XMetaData(name) for name in file_names}

scene_token = ''
# get current scene by id
for s in meta_data_list['scene'].file:
    if s['name'] == f'scene_{current_scene}':
        meta_data_list['scene'].data.append(s)
        scene_token = s['token']

if scene_token == '':
    raise Exception(f'No scene {current_scene} found in scene.json')

for s in meta_data_list['sample'].file:
    if s['scene_token'] == scene_token:
        meta_data_list['sample'].data.append(s)
        meta_data_list['sample'].ids.add(s['token'])

# get all sample annotations
for ann in meta_data_list['sample_annotation'].file:
    if ann['sample_token'] in meta_data_list['sample'].ids:
        meta_data_list['instance'].ids.add(ann['instance_token'])
        meta_data_list['sample_annotation'].data.append(ann)

# get all sample data
for sd in meta_data_list['sample_data'].file:
    if sd['sample_token'] in meta_data_list['sample'].ids:
        meta_data_list['ego_pose'].ids.add(sd['ego_pose_token'])
        meta_data_list['calibrated_sensor'].ids.add(sd['calibrated_sensor_token'])
        meta_data_list['sample_data'].data.append(sd)

def add_all_by_ids(name):
    for f in meta_data_list[name].file:
        if f['token'] in meta_data_list[name].ids:
            meta_data_list[name].data.append(f)

for ii in ['ego_pose', 'calibrated_sensor', 'instance']:
    add_all_by_ids(ii)

output_dir = 'v2.0-mini'
os.makedirs(output_dir, exist_ok=True)

def dump_json_file(name):
    with open(os.path.join(output_dir, f'{name}.json'), 'w') as f:
        json.dump(meta_data_list[name].data, f, indent=4)

for ii in file_names:
    dump_json_file(ii)