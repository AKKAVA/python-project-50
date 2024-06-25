install:
	poetry install

test:
	poetry run pytest -vv

test-coverage:
	poetry run pytest --cov --cov-report xml

lint:
	poetry run flake8

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl --break-system-packages

package-uninstall:
	python3 -m pip uninstall hexlet-code --break-system-packages

record:
	asciinema rec --overwrite cast/gendiff.cast

upload:
	asciinema upload cast/gendiff.cast
