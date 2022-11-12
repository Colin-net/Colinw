import csv


headers = ['name', 'age', 'sex']
row_data = [('xiaowang', 18, 'boy'),
            ('xiaolan', 19, 'boy'),
            ('xiaoqing', 20, 'girl')]
row_data_dict = [{'name': 'xiaowang', 'age': 18, 'sex': 'boy'},
                 {'name': 'xiaolan', 'age': 19, 'sex': 'boy'},
                 {'name': 'xiaoqin', 'age': 20, 'sex': 'girl'}]


def read_csv_01():
    with open('test.csv') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        print(headers)
        for row in f_csv:
            print("{}:{}".format(headers[0], row[0]))


def read_csv_02():
    with open('test.csv') as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            print(row['name'])


if __name__ == '__main__':
    read_csv_01()