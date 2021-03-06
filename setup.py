from setuptools import setup

setup(
    name='discogs-import',
    version='0.1',
    description='A fork of discogs import/export scripts',
    author='*',
    author_email='*',
    url='http://github.com/bmcfee/discogs-import',
    download_url='http://github.com/bmcfee/discogs-import/releases',
    long_description="""\
    A fork of discogs import/export scripts
    """,
    packages=['discogs_import'],
    scripts=[   'parse_discogs.py',
                'tools/discogs-import-fix-xml.py',
                'tools/discogs-import-get_latest_dumps.sh',
                'tools/discogs-import-make_artist_name_id_pair.py',
                'tools/discogs-import-make_md5.py'
    ],
    classifiers=[
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Programming Language :: Python",
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "Topic :: Multimedia :: Text Processing :: Markup",
    ],
    keywords='web xml discography database',
    license='GPL',
    extras_require = {
        'ujson': 'ujson',
        'couchdb': 'couchdb',
        'mongodb': 'pymongo',
        'postgres': 'psycopg2'
    }
)
