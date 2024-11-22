#!/usr/bin/env python3
import argparse
import markdown
from pathlib import Path

snip_basedir = lambda p: Path(p).absolute().relative_to(Path('html').absolute())

def parse_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('markdown_file')

    arg_parser.add_argument(
        '-x',
        '--extension',
        action = 'append',
        default = []
    )

    arg_parser.add_argument(
        '-c',
        '--css',
        action = 'append',
        default = []
    )

    arg_parser.add_argument(
        '-j',
        '--js',
        action = 'append',
        default = []
    )

    return arg_parser.parse_args()

def main():
    args = parse_args()

    stylesheets = '\n'.join(
        f'<link rel="stylesheet" href="/{snip_basedir(c)}">'
        for c in args.css
    )

    scripts = '\n'.join(
        f'<script src="/{snip_basedir(j)}"></script>'
        for j in args.js
    )

    template = (
        '<head>\n'
        f'{stylesheets}\n'
        f'{scripts}\n'
        '</head>\n'
        '<body>\n'
        '<div class="content">\n'
        '{}\n'
        '</div>\n'
        '</body>'
    )

    with open(args.markdown_file) as m:
        content = markdown.markdown(m.read(), extensions = args.extension)

    print(template.format(content))

if __name__ == '__main__':
    main()
