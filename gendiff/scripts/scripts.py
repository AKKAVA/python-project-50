from gendiff import arg_parser as arg_parser
from gendiff import gendiff as gendiff


def main():
    args = arg_parser.arg_parser()
    style = args.format
    diff = gendiff.generate_diff(args.first_file, args.second_file, style)
    print(diff)


if __name__ == '__main__':
    main()
