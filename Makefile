.PHONY:clean
clean:
	rm -rf dist;
	rm -rf build;
	rm -rf *.egg-info;
	find . -name *.pyc -delete

.PHONY:build
build:
	python ./container_gen/container_generator.py -f ./pynohtml/containers.py;
	cat ./container_gen/spe_containers.py >> ./pynohtml/containers.py;
	python setup.py sdist --formats=tar

.PHONY:install
install: clean build
	pip install --upgrade --force-reinstall dist/*
