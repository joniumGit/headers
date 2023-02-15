import os
import pathlib

VERSION_FORMAT = '%Y.%m.%d'

IANA_URL = os.getenv('IANA_HEADERS_CSV', 'https://www.iana.org/assignments/http-fields/field-names.csv')
IANA_DOC_URL = os.getenv('IANA_HEADERS_DOC_URL', 'https://www.iana.org/assignments/http-fields/http-fields.xhtml')

CURRENT_DIR = pathlib.Path(__file__).parent.resolve().relative_to(pathlib.Path.cwd())
INIT_PY = CURRENT_DIR / 'src' / 'headers' / '__init__.py'
STRING_PY = CURRENT_DIR / 'src' / 'headers' / 'string.py'
BINARY_PY = CURRENT_DIR / 'src' / 'headers' / 'binary.py'


def get_headers():
    """Returns IANA headers as (csv_header, csv_rows)
    """
    import urllib.request as requests
    with requests.urlopen(IANA_URL) as url_connection:
        response = url_connection.read().decode('utf-8')
    csv_data = response.splitlines(keepends=False)
    header = csv_data[0].split(',')
    print(response)
    return header, csv_data


def fhash(file: pathlib.Path):
    """SHA2565 on file content
    """
    import hashlib
    with open(file, 'rb') as f:
        return hashlib.sha512(f.read()).digest()


def read_version():
    with open(INIT_PY, 'r') as f:
        for line in f:
            if line.startswith('__version__'):
                return line.split('"')[1]


def write(f, header, csv_data, as_bytes: bool = False):
    """Writes IANA returned headers to file
    """
    import csv
    # IANA Csv fields (check manually)
    name, template, status, reference, comments, *other = header
    for line in csv.DictReader(csv_data[1:], fieldnames=header):
        value = line[name]
        variable_name = value.upper().replace('-', '_')
        if variable_name == '*':
            variable_name = 'STAR'
        entry_status = line[status]
        entry_comment = '\n' * 2 + line[comments] if line[comments] != '' else ''
        entry_reference = line[reference]
        f.write('\n{variable} = {raw}"{value}"\n"""{value} [{status}]\n\n{reference}{comment}\n"""\n'.format(
            variable=variable_name,
            value=value,
            status=entry_status,
            reference=entry_reference,
            comment=entry_comment,
            raw='b' if as_bytes else ''
        ))


def create_files():
    import datetime

    _created_at = datetime.datetime.today()
    _header, _csv_data = get_headers()

    with open(INIT_PY, 'w') as f:
        f.write(f'"""HTTP Headers\n\nsee: {IANA_DOC_URL}\ngenerated at: {_created_at.isoformat()}\n"""\n')
        f.write(f'from .string import *\n\n__version__ = "{_created_at.strftime(VERSION_FORMAT)}"\n')

    with open(STRING_PY, 'w') as f:
        f.write(f'"""HTTP Headers as str\n\nsee: {IANA_DOC_URL}\n"""\n')
        write(f, _header, _csv_data, as_bytes=False)

    with open(BINARY_PY, 'w') as f:
        f.write(f'"""HTTP Headers as bytes\n\nsee: {IANA_DOC_URL}\n"""\n')
        write(f, _header, _csv_data, as_bytes=True)


if __name__ == '__main__':
    import datetime

    version = read_version()
    start = [fhash(f) for f in (STRING_PY, BINARY_PY)]
    create_files()
    end = [fhash(f) for f in (STRING_PY, BINARY_PY)]

    if version == datetime.date.today().strftime(VERSION_FORMAT):
        print('Cannot release with the same date')
        exit(2)
    elif all(map(lambda t: t[0] == t[1], zip(start, end))):
        print('Nothing to change...')
        exit(1)
    else:
        print('Files changed!')
        exit(0)
