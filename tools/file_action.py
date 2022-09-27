import pathlib


ROOT_PATH_txt = pathlib.Path(__file__).parents[1]
FILE_PATH_txt = ROOT_PATH_txt.joinpath("requirements.txt")

ROOT_PATH_csv = pathlib.Path(__file__).parents[0]
FILE_PATH_csv = ROOT_PATH_csv.joinpath("database.csv")


def read_file():
    with open(FILE_PATH_txt) as file:
        return file.read()
