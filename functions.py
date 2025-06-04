FILEPATH = "todos.txt"

# We add utf-8 for supporting more unicodes characters such as Burmese,etc.

def get_todos_from_file(filepath=FILEPATH):
    """Read a text file and return a list of to-do item."""
    with open(filepath, 'r', encoding="utf-8") as _file:
        _todos = _file.readlines()
    return _todos


def write_todos_to_file(_todos, filepath=FILEPATH):
    """Write a list of to-do item to a text file."""
    with open(filepath, 'w', encoding="utf-8") as _file:
        _file.writelines(_todos)