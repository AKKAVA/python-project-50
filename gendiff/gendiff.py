import argparse
import json


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    parser.add_argument('-f', '--format',
                        help='set format of output')
    args = parser.parse_args()
    diff = gendiff(args.first_file, args.second_file)
    print(diff)


def gendiff(path_1: str, path_2: str):
    json_diff = gen_json_diff(path_1, path_2)
    return json_diff


def gen_json_diff(path_1: str, path_2: str):
    '''
    Get two paths to json file
    and generete diff between them\n\n

    "+" - absent in first file\n
    "-" - absent in second file\n
    "no simbol" - present in both files
    '''
    result = '{\n'
    file_1, file_2 = parse_json(path_1), parse_json(path_2)
    keys_1, keys_2 = list(file_1.keys()), list(file_2.keys())

    for key in sorted(keys_1):
        if key not in keys_2:
            result += form_json_str(key, file_1, simbol='-')
        elif file_1[key] != file_2[key]:
            result += form_json_str(key, file_1, simbol='-')
            result += form_json_str(key, file_2, simbol='+')
            keys_2.pop(keys_2.index(key))
        else:
            result += form_json_str(key, file_1)
            keys_2.pop(keys_2.index(key))
    if keys_2:
        for key in sorted(keys_2):
            result += form_json_str(key, file_2, simbol='+')
    result += '}'
    return result


def parse_json(path: str) -> dict:
    with open(path, mode='r', encoding='utf-8') as file:
        return json.load(file)


def form_json_str(key, vals, simbol=' '):
    val = json.dumps(vals[key]).strip('"')
    return f'  {simbol} {key}: {val}\n'


if __name__ == '__main__':
    main()
