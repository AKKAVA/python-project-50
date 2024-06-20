import gendiff.gendiff as gd

JSON_FILES = {
    'file_1': 'tests/fixtures/json_files/file_1.json',
    'file_2': 'tests/fixtures/json_files/file_2.json',
    'file_3': 'tests/fixtures/json_files/file_3.json',
    'file_4': 'tests/fixtures/json_files/file_4.json'}


YAML_FILES = {
    'file_1': 'tests/fixtures/yaml_files/file_1.yaml',
    'file_2': 'tests/fixtures/yaml_files/file_2.yaml',
    'file_3': 'tests/fixtures/yaml_files/file_3.yml',
    'file_4': 'tests/fixtures/yaml_files/file_4.yaml'}


RESULTS = {
    'result_1': 'tests/fixtures/results/json_result_1.txt',
    'result_2': 'tests/fixtures/results/json_result_2.txt',
    'result_3': 'tests/fixtures/results/json_result_3.txt'}


def gen_diff(file_1_path: str, file_2_path: str, result_path: str):
    with open(result_path, mode='r', encoding='utf-8') as file:
        correct_result = file.read()

    result = gd.generate_diff(file_1_path, file_2_path)
    assert result == correct_result


# json tests

def test_json_diff_1():
    gen_diff(JSON_FILES['file_1'], JSON_FILES['file_2'], RESULTS['result_1'])


def test_json_diff_2():
    gen_diff(JSON_FILES['file_1'], JSON_FILES['file_3'], RESULTS['result_2'])


def test_json_diff_3():
    gen_diff(JSON_FILES['file_1'], JSON_FILES['file_4'], RESULTS['result_3'])


# yaml tests

def test_yaml_diff_1():
    gen_diff(YAML_FILES['file_1'], YAML_FILES['file_2'], RESULTS['result_1'])


def test_yaml_diff_2():
    gen_diff(YAML_FILES['file_1'], YAML_FILES['file_3'], RESULTS['result_2'])


def test_yaml_diff_3():
    gen_diff(YAML_FILES['file_1'], YAML_FILES['file_4'], RESULTS['result_3'])
