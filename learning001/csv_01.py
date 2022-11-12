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


def write_csv_01():
    with open('test.csv', 'w', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(row_data)


def write_csv_02():
    with open('test.csv', 'w', newline='') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(row_data_dict)


if __name__ == '__main__':
    write_csv_02()