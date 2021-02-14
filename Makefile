.PHONY:clean
clean:
	rm -rf dist;
	rm -rf build;
	rm -rf *.egg-info;
	find . -name *.pyc -delete
	find . -name *__pycache__* -delete

.PHONY:build
build:
	python setup.py sdist --formats=tar

.PHONY:install
install: clean build
	pip install --upgrade --force-reinstall dist/*

.PHONY:test
test: clean
	python setup.py test
