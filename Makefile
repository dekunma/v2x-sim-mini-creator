scene = 1
base_dir = '/scratch/dm4524/data/V2X-Sim-2'

create:
	echo Creating mini dataset for scene $(scene)...
	python extract_meta_data_by_scene.py --scene=$(scene) --base_dir=$(base_dir)
	python extract_lidarseg_meta_data_by_scene.py --scene=$(scene) --base_dir=$(base_dir)
	python copy_other_meta_data.py --base_dir=$(base_dir)
	python copy_data_by_scene.py --scene=$(scene) --base_dir=$(base_dir)
	python copy_lidarseg_by_scene.py --scene=$(scene) --base_dir=$(base_dir)
	cp -r $(base_dir)/maps ./

clean:
	rm -rf ./v2.0-mini
	rm -rf ./sweeps
	rm -rf ./maps