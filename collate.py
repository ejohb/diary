"""

Bulk rename sheets in order scanned to folios in collation order.

"""
from pathlib import Path

MAPPINGS = {
    'sheet1a': 'folio4b',
    'sheet1b': 'folio4a',
    'sheet2a': 'folio1b',
    'sheet2b': 'folio1a',
    'sheet3a': 'folio2a',
    'sheet3b': 'folio2b',
    'sheet4a': 'folio5a',
    'sheet4b': 'folio5b',
    'sheet5a': 'folio7b',
    'sheet5b': 'folio7a',
    'sheet6a': 'folio6b',
    'sheet6b': 'folio6a',
    'sheet7a': 'folio8a',
    'sheet7b': 'folio8b',
    'sheet8a': 'folio9b',
    'sheet8b': 'folio9a',
    'sheet9a': 'folio10b',
    'sheet9b': 'folio10a',
    'sheet10a': 'folio11a',
    'sheet10b': 'folio11b',
    'sheet11a': 'folio12b',
    'sheet11b': 'folio12a',
    'sheet12a': 'folio14a',
    'sheet12b': 'folio14b',
    'sheet13a': 'folio15b',
    'sheet13b': 'folio15a',
    'sheet14a': 'folio16b',
    'sheet14b': 'folio16a',
    'sheet15a': 'folio17a',
    'sheet15b': 'folio17b',
    'sheet16a': 'folio13a',
    'sheet16b': 'folio13b',
    'sheet17a': 'folio3a',
    'sheet17b': 'folio3b',
    'sheet18a': 'folio18a',
    'sheet18b': 'folio18b',
}

if __name__ == '__main__':
    renames = {}
    for stem_before, stem_after in MAPPINGS.items():
        filenames = list(Path('.').glob(f'{stem_before}.*'))
        for filename in filenames:
            renames[filename] = Path(stem_after).with_suffix(filename.suffix)
    for path_before, path_after in renames.items():
        path_before.rename(path_after)
