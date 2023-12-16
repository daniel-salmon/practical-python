# portfolio.py

class Portfolio:

    def __init__(self, holdings):
        self._holdings = holdings

    def __repr__(self):
        return self._holdings.__repr__()

    def __iter__(self):
        return self._holdings.__iter__()

    def __len__(self):
        return len(self._holdings)

    def __getitem__(self, idx):
        return self._holdings[idx]

    def __contains__(self, name):
        return any(s.name == name for s in self._holdings)

    def sort(self, key=lambda s: getattr(s, 'name'), reverse=False):
        self._holdings.sort(key=key, reverse=reverse)

    @property
    def total_cost(self):
        return sum(s.cost for s in self._holdings)

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()
        for s in self._holdings:
            total_shares[s.name] += s.shares
        return total_shares
