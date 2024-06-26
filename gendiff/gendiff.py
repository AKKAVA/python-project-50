#!/usr/bin/env python
from . import comparator as comparator
from . import file_parser as file_parser
from . import arg_parser as arg_parser
from .styles import formater as formater


def main():
    args = arg_parser.arg_parser()
    style = args.format
    diff = generate_diff(args.first_file, args.second_file, style)
    print(diff)


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


if __name__ == '__main__':
    main()
