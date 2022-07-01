#!/usr/bin/env python3
#coding: utf-8

# IMPORTS
import argparse, magic, sys, os, pandas
from rich.console import Console
from rich.table import Table

### MAIN
if __name__ == "__main__":

    # CLI
    parser = argparse.ArgumentParser(
        description='An XLS reader for your shell, because I had a use for it.',
        epilog='From @_erk3_ with love')
    parser.add_argument('-f', '--file', type=str, required=True, help='your XLS file, what else?')
    args = parser.parse_args()

    # File checks
    if not os.path.exists(args.file) or not os.path.isfile(args.file) or not os.access(args.file, os.R_OK):
        print(f'`{args.file}` does not exist, is not a file, or is not readable.')
        sys.exit(1)
    if not any([v in magic.from_file(args.file, mime=True) for v in ['excel', 'openxml']]):
        print(f'`{args.file}` does not look like an XLS file.')
        sys.exit(1)

    # Parse the XLS file (all sheets)
    df = pandas.read_excel(args.file, index_col=0, sheet_name=None)

    # Rich setup
    console = Console()

    # Loop over the sheets
    for sheet in df:
        table = Table(caption=f'{args.file} - {sheet}', row_styles=["dim", ""], show_lines=True)
        for c in df[sheet].columns.values.tolist():
            table.add_column(f"{c}")
        for r in df[sheet].to_dict('records'):
            table.add_row(*[str(r) for r in r.values()])
        console.print(table)

