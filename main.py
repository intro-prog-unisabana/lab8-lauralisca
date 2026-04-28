"""Laboratorio 8 - CLI del gestor de tareas."""
import sys
from todo_manager import read_todo_file, write_todo_file

if len(sys.argv) < 2:
        raise IndexError("Insufficient arguments provided!")

    
if sys.argv[1] == "--help":
        print("""Usage: python main.py <file_path> <command> [arguments]...
Examples:
  python main.py tasks.txt add "Buy groceries"
  python main.py tasks.txt remove "Do laundry"
  python main.py tasks.txt view
  python main.py tasks.txt add "Call mom" remove "Take out trash" view""")
        sys.exit()

