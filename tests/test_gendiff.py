import gendiff.gendiff as gd

JSON_FILES = {
    'file_1': 'tests/fixtures/json_files/file_1.json',
    'file_2': 'tests/fixtures/json_files/file_2.json',
    'file_3': 'tests/fixtures/json_files/file_3.json',
    'file_4': 'tests/fixtures/json_files/file_4.json'}


YALM_FILES = {
    'file_1': 'tests/fixtures/yalm_files/file_1.yalm',
    'file_2': 'tests/fixtures/yalm_files/file_2.yalm',
    'file_3': 'tests/fixtures/yalm_files/file_3.yalm',
    'file_4': 'tests/fixtures/yalm_files/file_4.yalm'}


RESULTS = {
    'result_1': 'tests/fixtures/results/json_result_1.txt',
    'result_2': 'tests/fixtures/results/json_result_2.txt',
    'result_3': 'tests/fixtures/results/json_result_3.txt'}


# json tests

def test_json_diff_1():
    json_diff(JSON_FILES['file_1'], JSON_FILES['file_2'], RESULTS['result_1'])


def test_json_diff_2():
    json_diff(JSON_FILES['file_1'], JSON_FILES['file_3'], RESULTS['result_2'])


def test_json_diff_3():
    json_diff(JSON_FILES['file_1'], JSON_FILES['file_4'], RESULTS['result_3'])


def json_diff(file_1_path: str, file_2_path: str, result_path: str):
    with open(result_path, mode='r', encoding='utf-8') as file:
        correct_result = file.read()

    result = gd.gen_json_diff(file_1_path, file_2_path)
    assert result == correct_result


# yalm tests

# def test_yalm_diff_1():
#     yalm_diff(YALM_FILES['file_1'], YALM_FILES['file_2'], RESULTS['result_1'])


# def test_json_diff_2():
#     yalm_diff(YALM_FILES['file_1'], YALM_FILES['file_3'], RESULTS['result_2'])


# def test_json_diff_3():
#     yalm_diff(YALM_FILES['file_1'], YALM_FILES['file_4'], RESULTS['result_3'])


# def yalm_diff(file_1_path: str, file_2_path: str, result_path: str):
#     with open(result_path, mode='r', encoding='utf-8') as file:
#         correct_result = file.read()

#     result = gd.gen_yalm_diff(file_1_path, file_2_path)
#     assert result == correct_result
