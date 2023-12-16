# ticker.py

from follow import follow
from report import read_portfolio
from tableformat import create_formatter
import csv

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row

def convert_types(rows, types):
    for row in rows:
        yield [t(r) for t, r in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def ticker(portfile, logfile, fmt):
    portfolio = read_portfolio(portfile)
    lines = follow(logfile)
    rows = parse_stock_data(lines)
    rows = (row for row in rows if row['name'] in portfolio)
    formatter = create_formatter(fmt)
    formatter.headings(['Name', 'Price', 'Change'])
    for row in rows:
        rowdata = [row['name'], row['price'], row['change']]
        formatter.row(rowdata)

if __name__ == '__main__':
    ticker('Data/portfolio.csv', 'Data/stocklog.csv', 'txt')
