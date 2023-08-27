from pathlib import Path
from xml.etree import ElementTree


def convert_td(file_extract_dir: Path, target_file: Path):
    # 解析所有 todolist
    todolist: list[str] = _convert_todolist(file_extract_dir)

    target_file.write_text("\n".join(todolist))

def _convert_todolist(file_extract_dir: Path):
    wiz_todolist = file_extract_dir.joinpath("index_files").joinpath("wiz_todolist.xml")
    if not wiz_todolist.exists():
        raise FileNotFoundError(f'todolist文件不存在！ {wiz_todolist}')
    tree = ElementTree.parse(str(wiz_todolist))
    todolist: list[str] = []
    _convert_todolist_children(tree.getroot(), todolist, 0)
    return todolist

def _convert_todolist_children(parent, todolist, level):
    for todo in parent:
        indent = " " * (level * 4)
        text = todo.attrib["Text"]
        complete = todo.attrib["Complete"]
        if complete == "4":
            todolist.append(f"{indent}- [x] {text}")
        else:
            todolist.append(f"{indent}- [ ] {text}")
        # 递归解析子节点
        _convert_todolist_children(todo, todolist, level + 1)
