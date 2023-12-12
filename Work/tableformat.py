# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format.
    '''
    def headings(self, headers):
        print(' '.join(f'{str(h):>10s}' for h in headers))
        print(' '.join(['-' * 10] * len(headers)))

    def row(self, rowdata):
        print(' '.join(f'{str(r):>10s}' for r in rowdata))


class CSVTableFormatter(TableFormatter):
    '''
    Emit a table in CSV format.
    '''
    def headings(self, headers):
        print(','.join(str(h) for h in headers))

    def row(self, rowdata):
        print(','.join(str(r) for r in rowdata))


class HTMLTableFormatter(TableFormatter):
    '''
    Emit a table in HTML format.
    '''
    def headings(self, headers):
        print('<tr><th>' + '</th><th>'.join(str(h) for h in headers) + '</th></tr>')

    def row(self, rowdata):
        print('<tr><td>' + '</td><td>'.join(str(r) for r in rowdata) + '</td></tr>')


def create_formatter(fmt):
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {fmt}')


def print_table(rows, columns, formatter):
    '''
    Outputs a table with the given columns using a list of objects.
    '''
    formatter.headings(columns)
    for obj in rows:
        formatter.row(getattr(obj, attr) for attr in columns)
