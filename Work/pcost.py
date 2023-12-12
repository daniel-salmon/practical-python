#!/usr/bin/env python3
# pcost.py
#
# Exercise 1.27

import report

def portfolio_cost(filename):
    total = 0.0
    portfolio = report.read_portfolio(filename)
    for stock in portfolio:
        total += stock.cost
    return total

def main(argv):
    if len(argv) > 2:
        raise SystemExit(f'Usage: {argv[0]} ' ' portfolio-file')
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = 'Data/portfolio.csv'

    cost = portfolio_cost(filename)
    print('Total cost:', cost)

if __name__ == '__main__':
    import sys
    main(sys.argv)
