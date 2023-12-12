#!/usr/bin/env python3
# pcost.py
#
# Exercise 1.27

from report import read_portfolio

def portfolio_cost(filename):
    '''
    Computes the total cost of a portfolio.
    '''
    return read_portfolio(filename).total_cost

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
