import os

IANA_HEADERS_CSV = os.getenv('IANA_HEADERS_CSV', 'https://www.iana.org/assignments/http-fields/field-names.csv')

if __name__ == '__main__':
    import csv
    import datetime
    import pathlib
    import urllib.request as requests

    with requests.urlopen(IANA_HEADERS_CSV) as url_connection:
        response = url_connection.read().decode('utf-8')

    print(response)

    csv_data = response.splitlines(keepends=False)
    header = csv_data[0].split(',')


    def write(f, binary: bool = False):
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
            f.write('\n{variable} = {binary}"{value}"\n"""{value} [{status}]\n\n{reference}{comment}\n"""\n'.format(
                variable=variable_name,
                value=value,
                status=entry_status,
                reference=entry_reference,
                comment=entry_comment,
                binary='b' if binary else ''
            ))


    here = pathlib.Path(__file__).parent.resolve()

    with open(here / 'src' / 'headers' / '__init__.py', 'w') as file:
        file.write(f'"""Headers: generated at: {datetime.datetime.now().isoformat()}\n"""\n')
        file.write(f'from .string import *\n\n__version__ = "{datetime.date.today().strftime("%Y.%m.%d")}"\n')

    with open(here / 'src' / 'headers' / 'string.py', 'w') as file:
        file.write(f'"""String Headers: generated at: {datetime.datetime.now().isoformat()}\n"""\n')
        write(file, False)

    with open(here / 'src' / 'headers' / 'binary.py', 'w') as file:
        file.write(f'"""Binary Headers: {datetime.datetime.now().isoformat()}\n"""\n')
        write(file, True)
