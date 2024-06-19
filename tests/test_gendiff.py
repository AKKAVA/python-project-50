import gendiff.gendiff as gd


def test_json_diff():
    correct_result = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    result = gd.gen_json_diff('tests/file_1.json', 'tests/file_2.json')
    assert result == correct_result
