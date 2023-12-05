#!/usr/bin/env python3

import sys
import os
import re


def generate_main_index(toplevel_path):
    template_path = os.path.join(toplevel_path, 'index.md.in')
    with open(os.path.join(toplevel_path, 'index.md'), 'w') as index:
        with open(template_path) as template:
            index.write(template.read())
        for item in os.listdir(toplevel_path):
            abs_item = os.path.join(toplevel_path, item)
            if os.path.isdir(abs_item):
                index.write(f'* [{item}]({item})\n')
    os.remove(template_path)


def generate_path_indexes(toplevel_path):
    os.chdir(toplevel_path)
    for (dirpath, dirnames, filenames) in os.walk('.'):
        relative_dirpath = os.path.relpath(dirpath)
        if os.path.exists(os.path.join(dirpath, 'index.md')):
            continue
        with open(os.path.join(dirpath, 'index.md'), 'w') as index:
            index.write(f'# {relative_dirpath}\n\n')
            if len(dirnames) > 0:
                for item in dirnames:
                    index.write(f'* [{item}]({item})\n')
            else:
                for item in filenames:
                    mo = re.search(r'(.*)\.md', item)
                    if mo is not None:
                        base_item = mo.group(1)
                        index.write(f'* [{base_item}]({base_item})\n')


def main():
    toplevel_path = sys.argv[1]
    if not os.path.isdir(toplevel_path):
        raise RuntimeError('path not found: ' + toplevel_path)
    generate_main_index(toplevel_path)
    generate_path_indexes(toplevel_path)


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as e:
        sys.stderr.write(str(e) + "\n")
        sys.exit(1)
