scene = 1

create:
	echo Creating mini dataset for scene $(scene)...
	python extract_meta_data_by_scene.py --scene=$(scene)
	python extract_lidarseg_meta_data_by_scene.py --scene=$(scene)
	python copy_other_meta_data.py
	python copy_data_by_scene.py --scene=$(scene)
	cp -r ../V2X-Sim-2/maps ./

clean:
	rm -rf ./v2.0-mini
	rm -rf ./sweeps
	rm -rf ./maps