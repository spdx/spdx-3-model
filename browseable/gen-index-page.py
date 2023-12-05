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


def generate_path_indexes(source_model_path, toplevel_path):
    for (dirpath, dirnames, filenames) in os.walk(toplevel_path):
        if os.path.exists(os.path.join(dirpath, 'index.md')):
            continue
        preamble = ''
        relative_dirpath = os.path.relpath(dirpath, toplevel_path)
        section_preamble_fn = \
            os.path.join(source_model_path, relative_dirpath,
                         f'{relative_dirpath}.md')
        if os.path.exists(section_preamble_fn):
            with open(section_preamble_fn) as section_preamble_file:
                preamble = section_preamble_file.read()
        with open(os.path.join(dirpath, 'index.md'), 'w') as index:
            if preamble:
                index.write(preamble)
            else:
                index.write(f'# {relative_dirpath}\n')
            index.write('\n')
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
    source_model_path = sys.argv[1]
    toplevel_path = sys.argv[2]
    for p in [source_model_path, toplevel_path]:
        if not os.path.isdir(p):
            raise RuntimeError('path not found: ' + p)
    generate_main_index(toplevel_path)
    generate_path_indexes(source_model_path, toplevel_path)


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as e:
        sys.stderr.write(str(e) + "\n")
        sys.exit(1)
