import csv
from os.path import join, abspath, dirname, exists
# TODO оформить в тест, добавить ассерты и использовать универсальный путь

csv_path = abspath(
    join(dirname(__file__), './resources/username.csv')
)


def test_csv_save_to_file():
    names_1 = ['Anna', 'Pavel', 'Peter']
    names_2 = ['Alex', 'Serj', 'Yana']

    with open(csv_path, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(names_1)
        csvwriter.writerow(names_2)

    assert exists(csv_path)

    rows = []
    with open(csv_path) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if len(row) > 0:
                rows.append(row)

    assert names_1 in rows
    assert names_2 in rows


