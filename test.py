from pathlib import Path

PACKAGE = Path('src') / 'headers'
PATHS = [
    PACKAGE / '__init__.py',
    PACKAGE / 'string.py',
    PACKAGE / 'binary.py',
]

all_names = set()

for file in PATHS:
    with open(file, 'r') as f:

        try:
            code = compile(f.read(), file, 'exec')
        except SyntaxError:
            print('Failed to compile!', file)
            exit(1)

    _globals = {'__name__': '__main__', '__package__': '.'.join(PACKAGE.parts)}
    exec(code, _globals)
    _variables = {k: v for k, v in _globals.items() if not k.startswith('__')}

    if not all_names:
        all_names.update(_variables.keys())

    assert len(all_names) != 0, 'Got no names'

    assert all(k in all_names for k in _variables.keys()), f'Failed ensure consistent variables {file}'

exit(0)
