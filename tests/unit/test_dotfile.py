"""Test njsscan dotfile."""
from .setup_test import (
    get_paths,
    scanner,
)


TMPL_IDS = [
    'underscore_template',
    'pug_jade_template',
]

NJS_IDS = [
    'eval_warning',
]


def test_njsscan_dotfile():
    paths = get_paths('nodejs')
    files = paths['dot_file']
    res = scanner([files], True)
    tmpl = [*res['templates']]
    njs = [*res['nodejs']]
    tmpl.sort()
    njs.sort()
    TMPL_IDS.sort()
    NJS_IDS.sort()
    assert tmpl == TMPL_IDS
    assert njs == NJS_IDS
