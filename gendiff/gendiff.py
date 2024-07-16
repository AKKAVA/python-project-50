#!/usr/bin/env python
from gendiff import comparator
from gendiff import file_parser
from gendiff.styles import formater


def generate_diff(path_1: str, path_2: str, style_name: str = '') -> str:
    '''
    Get two paths to file
    end generete diff between them
    '''
    data_1, data_2 = file_parser.read_file(path_1), file_parser.read_file(path_2)
    diff = comparator.compare_data(data_1, data_2)
    return formater.style(style_name, diff)
