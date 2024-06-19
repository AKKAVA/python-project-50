install:
	poetry install

test:
	poetry run pytest
	poetry run flake8

demo:
	poetry run gendiff "tests/file_1.json" "tests/file_2.json"

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl --break-system-packages

package-uninstall:
	python3 -m pip uninstall hexlet-code --break-system-packages

record:
	asciinema rec --overwrite cast/gendiff.cast