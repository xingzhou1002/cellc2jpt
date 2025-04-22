import pathlib
import sys
import json

def main():
    if len(sys.argv) != 2:
        print("Usage: cellc2jpt <file_path>")
        sys.exit(1)

    input_path = pathlib.Path(sys.argv[1])

    if not input_path.exists():
        print(f"Error: File {input_path} does not exist.")
        sys.exit(1)

    if not input_path.is_file():
        print(f"Error: {input_path} is not a file.")
        sys.exit(1)

    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except UnicodeDecodeError:
        print(f"Error: Could not read file {input_path} with UTF-8 encoding.")
        sys.exit(1)

    cells = []
    current_cell = None

    for line in lines:
        stripped_line = line.strip()
        if stripped_line == '# cell':
            if current_cell is not None:
                if current_cell:
                    cells.append(current_cell)
                current_cell = []
            else:
                current_cell = []
            continue
        else:
            if current_cell is not None:
                current_cell.append(line)

    if current_cell is not None and current_cell:
        cells.append(current_cell)

    if not cells:
        print("Error: No valid code cells found. Ensure the file contains at least one non-empty '# cell' section.")
        sys.exit(1)

    notebook = {
        "cells": [
            {
                "cell_type": "code",
                "source": cell,
                "metadata": {},
                "execution_count": None,
                "outputs": []
            }
            for cell in cells
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": sys.version.split()[0]
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

    output_path = input_path.with_suffix('.ipynb')
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1)
    except Exception as e:
        print(f"Error writing to {output_path}: {str(e)}")
        sys.exit(1)

    print(f"Notebook saved to {output_path}")

if __name__ == "__main__":
    main()