import csv

from tools.file_action import FILE_PATH_csv


def average():
    with open(FILE_PATH_csv, newline="") as file:
        read_file = csv.DictReader(file)
        average_height = 0
        average_weight = 0
        counter = 0
        for row in read_file:
            average_height += float(row[' "Height(Inches)"'])
            average_weight += float(row[' "Weight(Pounds)"'])
            counter += 1

        return (
            f"<p>Average height is: {round(average_height / counter, 2)} Inch</p>"
            f"<p>Average weight is: {round(average_weight / counter, 2)} Pound</p>"
        )
