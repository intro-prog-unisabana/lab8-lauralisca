"""Laboratorio 8 - Módulo de persistencia para lista de tareas."""


def read_todo_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"File {file_path} not found! Returning an empty to-do list.")
        return []

def write_todo_file(file_path, tasks):
    """Writes tasks to a file, one per line."""
    # TODO: Implementar escritura de tareas según README.md
    raise NotImplementedError
