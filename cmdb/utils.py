import re


SLUGIFY_CHAR_MAP = {
    'ä': 'a',
    'å': 'a',
    'ö': 'o',
    'ü': '',
    ' ': '-',
    '_': '-',
    '.': '-',
}
SLUGIFY_FORBANNAD_RE = re.compile(r'[^a-z0-9-/]', re.UNICODE)
SLUGIFY_MULTIDASH_RE = re.compile(r'-+', re.UNICODE)


def slugify(ustr):
    ustr = ustr.lower()
    ustr = ''.join(SLUGIFY_CHAR_MAP.get(c, c) for c in ustr)
    ustr = SLUGIFY_FORBANNAD_RE.sub('', ustr)
    ustr = SLUGIFY_MULTIDASH_RE.sub('-', ustr)
    return ustr


def log_get_or_create(logger, obj, created):
    logger.info('{kind} {name} {what_done}'.format(
        kind=obj.__class__.__name__,
        name=str(obj),
        what_done='created' if created else 'already exists',
    ))
