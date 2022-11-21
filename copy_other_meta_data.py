import os
import shutil

other_meta_data_files = ['attribute', 'category', 'log', 'map', 'sensor', 'visibility']

for ii in other_meta_data_files:
    shutil.copy(os.path.join('../V2X-Sim-2/v1.0-mini', f'{ii}.json'), './v2.0-mini')