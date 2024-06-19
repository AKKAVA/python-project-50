install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run coverage

lint:
	poetry run flake8

demo:
	poetry run gendiff "file_1.json" "file_2.json"

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl --break-system-packages

package-uninstall:
	python3 -m pip uninstall hexlet-code --break-system-packages

record:
	asciinema rec --overwrite cast/gendiff.cast