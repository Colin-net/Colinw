import csv


headers = ['name', 'age', 'sex']
row_data = [('xiaowang', 'xiaolan', 'xiaoqing'),
            (18, 19, 20),
            ('boy', 'boy', 'girl')]


def write_csv_01():
    with open('test.csv', 'a') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(row_data)


if __name__ == '__main__':
    write_csv_01()