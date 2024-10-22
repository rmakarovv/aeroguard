.PHONY: prereqs build test test_with_log

prereqs: requirements.txt
	pip install -r requirements.txt

build: scripts/preprocess.cpp
	g++ scripts/preprocess.cpp -o scripts/preprocess `pkg-config --cflags --libs opencv4`

test: tests
	python -m unittest -v

test_with_log: tests/test_preprocessing.py tests/test_processing.py tests/test_postprocessing.py
	python tests/test_preprocessing.py
	python tests/test_processing.py
	python tests/test_postprocessing.py