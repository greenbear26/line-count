#!/usr/bin/env python3
import os
import sys


def get_lines(directory, file_ending_list):
    line_count = 0
    file_count = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if any(filename.endswith(file_ending) for file_ending in file_ending_list):
                file_count += 1
                with open(os.path.join(dirpath, filename)) as f:
                    lines = len(f.readlines())
                    line_count += lines

    return (line_count, file_count)


def get_args():
    # first value is the name of script, so we ignore it
    args = sys.argv[1:]

    if len(args) != 2:
        print("Usage: line_count.py <directory> <file-extensions> ")
        print("Example: line_count.py /home/user/ .java")
        sys.exit(1)

    if not os.path.isdir(args[0]):
        print(f'The directory "{args[0]}" does not exist.')
        sys.exit(1)

    file_ending_list = args[1].split(",")
    return (args[0], file_ending_list)


def main():
    directory_path, file_ending_list = get_args()

    line_count, file_count = get_lines(directory_path, file_ending_list)
    print("Lines: " + str(line_count))
    print("Files: " + str(file_count))


if __name__ == "__main__":
    main()
