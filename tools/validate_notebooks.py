"""Проверяет nbformat, уникальность cell id и чистоту шаблонов ДЗ."""

import sys
from pathlib import Path

import nbformat


def validate(path):
    notebook = nbformat.read(path, as_version=4)
    nbformat.validate(notebook)
    ids = [cell.get("id") for cell in notebook.cells]
    if None in ids or len(ids) != len(set(ids)):
        raise ValueError("Нужны уникальные непустые идентификаторы ячеек")
    if "homeworks" in Path(path).parts:
        for cell in notebook.cells:
            if cell.cell_type == "code" and (cell.outputs or cell.execution_count is not None):
                raise ValueError("В шаблоне ДЗ остались результаты выполнения")


if __name__ == "__main__":
    failed = False
    for filename in sys.argv[1:]:
        try:
            validate(filename)
        except Exception as error:
            failed = True
            print(f"{filename}: {error}")
    sys.exit(int(failed))
