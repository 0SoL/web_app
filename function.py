FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(list_name, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(list_name)