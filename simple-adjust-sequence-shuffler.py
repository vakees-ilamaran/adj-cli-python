#!/usr/bin/env python3

"""
Description:
    adjust-sequence-shuffler
Abstract: 
    This is a simpler version of the shuffler which uses random module
Author: 
    vakees.ilamaran@gmail.com
"""

import random


def parsing_args():
    """
    We get the command line arguments and parse it to use it !!
    :return: returns the parse object
    """

    parser = argparse.ArgumentParser(
        prog='adjust-sequence-shuffler',
        epilog='Enjoy the CLI Adjust Team!')

    parser.add_argument(
        '--limit',
        metavar='limit',
        type=int,
        default=10,
        required=False,
        help='The limit for the shuffling of numbers to be generated')

    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s V1.0.0')

    return parser.parse_args()


def main():
    try:
        # Parsing if there are any command line arguments given.
        args = parsing_args()
        numbers_to_shuffle = list(range(1, args.limit + 1))
        random.shuffle(numbers_to_shuffle)
        print(*numbers_to_shuffle, sep=' ')

    except Exception as e:
        print("There is some issue with the main function")
        print("Please contact the GitHub Contributor for troubleshooting")
        sys.exit(e)


if __name__ == "__main__":
    main()
