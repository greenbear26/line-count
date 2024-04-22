#!/usr/bin/env python3
import os

def get_lines(directory):
    count = 0;
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.java'):
                with open(os.path.join(dirpath, filename)) as f:
                    lines = len(f.readlines())
                    count += lines

    return count

print("Lines: ")
print(get_lines("."))
