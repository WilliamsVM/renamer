from os import scandir, mkdir
from pathlib import Path
from shutil import move


def mover(source=None):
    """
    Function to split a folder full of files into a bunch of folders full of up to 10 files
    :param source: path to the source directory
    :return: collection of sub-directories each containing up to 10 files
    """
    list_of_files = set()
    number_of_files = 0

    if source is None:
        directory = Path(r'')
    else:
        directory = Path(source)

    with scandir(directory) as it:
        for file in it:
            if file.is_file():
                list_of_files.add(file.name)
                number_of_files += 1

    make_folders(number_of_files, directory)

    number_moved = move_files(directory, list_of_files)

    print(f'Files moved: {number_moved}')


def make_folders(number_of_files, directory):
    number_of_folders = (number_of_files // 10)
    if (number_of_files % 10) != 0:
        number_of_folders += 1

    for num in range(1, number_of_folders + 1):
        mkdir(Path(f"{directory}\\{num}"))


def move_files(directory, list_of_files):
    number_moved = 0
    current_folder = 1

    for filename in list_of_files:
        move(Path(f"{directory}\\{filename}"), Path(f"{directory}\\{current_folder}\\{filename}"))
        number_moved += 1

        if (number_moved % 10) == 0:
            current_folder += 1

    return number_moved


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    mover()
