# fileparse.py
#
# Exercise 3.3
import csv
import logging
log = logging.getLogger(__name__)

def parse_csv(
    lines,
    delimiter=',',
    select=None,
    types=None,
    has_headers=True,
    silence_errors=False
):
    '''
    Parse an iterable into a list of records
    '''
    if not iter(lines) or type(lines) is str:
        raise ValueError("rows is not iterable")
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    rows = csv.reader(lines, delimiter=delimiter)

    records = []
    for i, row in enumerate(rows):
        if not row:
            continue

        if i == 0:
            headers, select, types, idx = setup(row, select, types, has_headers)
            if has_headers:
                continue

        try:
            record = make_record(row, idx, types)
        except ValueError as e:
            if silence_errors:
                continue
            log.warning("Row %d: Couldn't convert %s", i, row)
            log.debug("Row %d: Reason %s", i, e)
            continue

        if has_headers:
            record = dict(zip(select, record))
        records.append(record)

    return records

def setup(row, select, types, has_headers):
    headers = []
    if has_headers:
        headers = row
    else:
        headers = list(range(len(row)))

    if not select:
        select = headers

    if not types:
        types = [str for i in select]

    validate(headers, select, types)

    idx = [headers.index(col) for col in select]

    return (headers, select, types, idx)

def validate(headers, select, types):
    for s in select:
        if s not in headers:
            raise ValueError("select list has a column not in the header")

    if len(types) != len(select):
        raise ValueError("Number of types doesn't match number of columns")

def make_record(row, idx, types):
    record = [row[i] for i in idx]
    return tuple([t(x) for t, x in zip(types, record)])
