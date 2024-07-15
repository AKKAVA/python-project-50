#!/usr/bin/env python
from gendiff import arg_parser
from gendiff import gendiff


def main():
    args = arg_parser.arg_parser()
    diff = gendiff.generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
