#! /usr/bin/python3

import sys
import csv
import re
from functools import reduce
from math import sqrt


def extract_columns(rows: list) -> list:
    columns = []
    column_number = str(rows[0]).count(',') + 1
    for i in range(0, column_number):
        columns.append([])

    for row in rows:
        cells = str(row).split(',')
        for i in range(0, column_number):   # start in 1 to skip headers
            columns[i].append(cells[i])

    del columns[0]          # Delete first column with frame numbers
    for col in columns:     # Delete column headers
        del col[0]
    return columns          # Leave only data


def collapse(path: str, segment_size: int) -> None:
    rows = []
    with open(path, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            rows.append(row)
    columns = extract_columns(rows)
    segs = segmentise(columns, segment_size)
    print(segs)
    write_result(segs, segment_size)


def remove_nonnumeric(string: str) -> float: return float(re.sub('[^0-9 .]', '', string))


def segmentise(columns: list, seg_size: int) -> list:
    row_num = 0
    segs = []
    for i in range(0, len(columns)):
        segs.append([])
    values = []

    i = 0
    for col in columns:
        for value in col:
            row_num += 1

            values.append(remove_nonnumeric(value))

            if row_num >= seg_size:
                segs[i].append(std_dev(values, seg_size))
                row_num = 0
                values.clear()
        i += 1
    return segs


def std_dev(values: list, iterations: int) -> tuple:
    summarise = lambda x, y: x + y
    mean = reduce(summarise, values) / iterations
    sqrd_list = map(lambda x: x * x, values)
    sqrd_sum = reduce(summarise, sqrd_list)
    return mean, sqrt((sqrd_sum - mean * mean * iterations) / (iterations - 1))     # Sestoft standard deviation formula


def write_result(columns: list, seg_size: int) -> None:
    with open('result.csv', 'w') as file:

        header = 'Frame No.'
        for i in range(0, len(columns)):
            header += ', ' + str(i) + ', ' + str(i) + ' error'
        file.write(header + '\n')

        for i in range(0, len(columns[0])):
            if i == 0:
                row = '0'
            else:
                row = str(i * seg_size)
            row += '-' + str(((i + 1) * seg_size) - 1)
            for col in columns:
                row += ', ' + str(col[i][0]) + ', ' + str(col[i][1])
            file.write(row + '\n')


def main() -> None:
    rows = 25

    if len(sys.argv) == 2:
        path = sys.argv[1]
        collapse(path, rows)

    elif len(sys.argv) == 3:
        path = sys.argv[1]
        rows = int(sys.argv[2])
        collapse(path, rows)


main()
