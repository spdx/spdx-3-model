#!/usr/bin/env python3

import sys
import os
import re


def find_sections(path):
    return [x for x in os.listdir(path)
            if os.path.isdir(os.path.join(path, x))]


def generate_main_index(source_model_path, toplevel_path, sections):
    template_path = os.path.join(toplevel_path, 'index.md.in')
    with open(os.path.join(toplevel_path, 'index.md'), 'w') as index:
        with open(template_path) as template:
            index.write(template.read())
        for item in sections:
            index.write(f'* [{item}]({item})\n')
    os.remove(template_path)


def generate_path_indexes(source_model_path, toplevel_path, sections):
    for section in sections:
        toplevel_section_path = os.path.join(toplevel_path, section)
        source_section_path = os.path.join(source_model_path, section)
        if not os.path.exists(toplevel_section_path):
            os.mkdir(toplevel_section_path)
        for (dirpath, dirnames, filenames) in os.walk(toplevel_section_path):
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
                    index.write('\n## Model Info\n\n')
                else:
                    index.write(f'# {relative_dirpath}\n\n')
                if len(dirnames) > 0:
                    for item in dirnames:
                        index.write(f'* [{item}]({item})\n')
                elif len(filenames) > 0:
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
    sections = find_sections(source_model_path)
    generate_main_index(source_model_path, toplevel_path, sections)
    generate_path_indexes(source_model_path, toplevel_path, sections)


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as e:
        sys.stderr.write(str(e) + "\n")
        sys.exit(1)
