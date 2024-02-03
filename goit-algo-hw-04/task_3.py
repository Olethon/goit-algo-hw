from pathlib import Path
from colorama import Fore


def directory_structure(folder_path, tab=0):
    path = Path(folder_path)
    if path.is_dir():
        directory = path.iterdir()
        for item in directory:
            if item.is_dir():
                print (f"{' '*tab} {Fore.LIGHTBLUE_EX} {item.name} {Fore.RESET}")
                directory_structure(item, tab+4)
            elif item.is_file():
                print (f"{' '*tab} {Fore.GREEN} {item.name} {Fore.RESET}")
    
         
directory_structure("./goit-algo-hw-04/my_directory")