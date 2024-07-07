#!/usr/bin/env python
from gendiff import comparator as comparator
from gendiff import file_parser as file_parser
from gendiff.styles import formater as formater


def generate_diff(path_1: str, path_2: str, style: str = '') -> str:
    '''
    Get two paths to file
    end generete diff between them
    '''
    data_1, data_2 = file_parser.read_file(path_1), file_parser.read_file(path_2)
    style = formater.get_style(style)
    diff = comparator.compare_data(data_1, data_2)
    styled_diff = style(diff)
    striped_diff = styled_diff.rstrip('\n')

    return striped_diff
