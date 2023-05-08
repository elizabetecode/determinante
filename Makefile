default: test

test:
	pytest

install:
	pip install -r requirements.txt

run:
	python determinant.py