import pytest
import gendiff.gendiff as gd


JSON_FILES = {
    'file_1': 'tests/fixtures/json_files/file_1.json',
    'file_2': 'tests/fixtures/json_files/file_2.json',
    'file_3': 'tests/fixtures/json_files/file_3.json',
    'file_4': 'tests/fixtures/json_files/file_4.json',
    'file_5': 'tests/fixtures/json_files/file_5.json',
    'file_6': 'tests/fixtures/json_files/file_6.json'}


YAML_FILES = {
    'file_1': 'tests/fixtures/yaml_files/file_1.yaml',
    'file_2': 'tests/fixtures/yaml_files/file_2.yaml',
    'file_3': 'tests/fixtures/yaml_files/file_3.yml',
    'file_4': 'tests/fixtures/yaml_files/file_4.yaml',
    'file_5': 'tests/fixtures/yaml_files/file_5.yaml',
    'file_6': 'tests/fixtures/yaml_files/file_6.yaml',
    'file_7': 'tests/fixtures/yaml_files/file_7.yml',
    'file_8': 'tests/fixtures/yaml_files/file_8.yml'}


RESULTS = {
    'result_1': 'tests/fixtures/results/result_1.txt',
    'result_2': 'tests/fixtures/results/result_2.txt',
    'result_3': 'tests/fixtures/results/result_3.txt',
    'result_4': 'tests/fixtures/results/result_4.txt',
    'result_5': 'tests/fixtures/results/result_5.txt',
    'result_6': 'tests/fixtures/results/result_6.txt'}


TEST_CASES = [
    (JSON_FILES['file_1'], JSON_FILES['file_2'], RESULTS['result_1'], 'stylish'),
    (JSON_FILES['file_1'], JSON_FILES['file_3'], RESULTS['result_2'], 'stylish'),
    (JSON_FILES['file_1'], JSON_FILES['file_4'], RESULTS['result_3'], 'stylish'),
    (JSON_FILES['file_5'], JSON_FILES['file_6'], RESULTS['result_4'], 'stylish'),
    (YAML_FILES['file_1'], YAML_FILES['file_2'], RESULTS['result_1'], 'stylish'),
    (YAML_FILES['file_1'], YAML_FILES['file_3'], RESULTS['result_2'], 'stylish'),
    (YAML_FILES['file_1'], YAML_FILES['file_4'], RESULTS['result_3'], 'stylish'),
    (YAML_FILES['file_5'], YAML_FILES['file_6'], RESULTS['result_4'], 'stylish'),
    (JSON_FILES['file_5'], JSON_FILES['file_6'], RESULTS['result_5'], 'plain'),
    (YAML_FILES['file_7'], YAML_FILES['file_8'], RESULTS['result_6'], 'stylish'),
]


@pytest.mark.parametrize('file_1_path, file_2_path, result_path, style', TEST_CASES)
def test_diff(file_1_path: str, file_2_path: str, result_path: str, style):
    with open(result_path, mode='r', encoding='utf-8') as file:
        correct_result = file.read()

    result = gd.generate_diff(file_1_path, file_2_path, style)

    assert result == correct_result
