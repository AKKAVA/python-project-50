import gendiff.gendiff as gd

JSON_FILES = {
    'file_1': 'tests/fixtures/file_1.json',
    'file_2': 'tests/fixtures/file_2.json',
    'file_3': 'tests/fixtures/file_3.json',
    'file_4': 'tests/fixtures/file_4.json'}

JSON_RESULTS = {
    'result_1': 'tests/fixtures/results/json_result_1.txt',
    'result_2': 'tests/fixtures/results/json_result_2.txt',
    'result_3': 'tests/fixtures/results/json_result_3.txt'}


def test_json_diff_1():
    json_diff(JSON_FILES['file_1'], JSON_FILES['file_2'], JSON_RESULTS['result_1'])


def test_json_diff_2():
    json_diff(JSON_FILES['file_1'], JSON_FILES['file_3'], JSON_RESULTS['result_2'])


def test_json_diff_3():
    json_diff(JSON_FILES['file_1'], JSON_FILES['file_4'], JSON_RESULTS['result_3'])


def json_diff(file_1_path: str, file_2_path: str, result_path: str):
    with open(result_path, mode='r', encoding='utf-8') as file:
        correct_result = file.read()

    result = gd.gen_json_diff(file_1_path, file_2_path)
    assert result == correct_result
