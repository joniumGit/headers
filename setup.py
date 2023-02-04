import pathlib

from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

with open(here / 'src' / 'headers' / '__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.split('"')[1]

setup(
    name='httpheaders',
    version=version,
    description='HTTP Headers',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/joniumGit/headers',
    author='joniumGit',
    # https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
    ],
    keywords='HTTP, headers, API',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3',
    install_requires=[],
    project_urls={
        'Bug Reports': 'https://github.com/joniumGit/headers',
        'Source': 'https://github.com/joniumGit/headers',
    },
)
