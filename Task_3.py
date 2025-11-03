import sys 
from pathlib import Path
from colorama import Fore, init

def parse_directory(current_path, indent=0):
    indent_str = ' ' * indent #Код 
    for item in current_path.iterdir():
        if item.is_dir():
            print(f"{Fore.BLUE}{indent_str}{item.name}")
            parse_directory(item, indent + 4)
        elif item.is_file():
            print(f"{Fore.GREEN}{indent_str}{item.name}")

def main():
    init(autoreset=True)
    if len(sys.argv) < 2:
        sys.stderr.write("Помилка: Не вказано файл!\n")
        sys.exit(1)

    path_from_user = sys.argv[1]

    dir_path = Path(path_from_user)
    parse_directory(dir_path)
        
if __name__ == "__main__":
    main()