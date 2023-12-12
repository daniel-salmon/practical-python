#!/usr/bin/env python3
# report.py
#
# Exercise 2.4
import tableformat
from fileparse import parse_csv
from portfolio import Portfolio
from stock import Stock

def read_portfolio(filename):
    '''
    Reads the file and returns the portfolio data as a list of Stocks.
    '''
    with open(filename, 'rt') as f:
        lines = f.read().split('\n')
    portfolio = [Stock(**s) for s in parse_csv(lines, types=[str, int, float])]
    return Portfolio(portfolio)

def read_prices(filename):
    '''
    Reads the file and returns the stock prices data as a dictionary keyed by stock names.
    '''
    with open(filename, 'rt') as f:
        lines = f.read().split('\n')
    return dict(parse_csv(lines, types=[str, float], has_headers=False))

def make_report(portfolio, prices):
    report = []
    for stock in portfolio:
        price = prices[stock.name]
        change = price - stock.price
        r = (stock.name, stock.shares, price, change)
        report.append(r)
    return report

def print_report(report, formatter):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)

def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    '''
    Generate a report from a portfolio file and a prices file.
    '''
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(argv):
    if len(argv) == 3:
        portfolio_report(argv[1], argv[2])
    elif len(argv) == 4:
        portfolio_report(argv[1], argv[2], argv[3])
    else:
        raise SystemExit(f'Usage: {argv[0]} ' 'portfolio-file price-file output-fmt')

if __name__ == '__main__':
    import sys
    main(sys.argv)
