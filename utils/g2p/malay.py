import re

import phonemizer

_ipa_mapping = [(re.compile('%s' % x[0]), x[1]) for x in [
    ('ɲ', 'ŋ'),
    ('ʔ', 'ɦ'),
    ('r', 'ɹ'),
    ('ʤ', 'dʒ'),
    ('ʧ', 'tʃ')
]]


def malay_to_ipa(text):
    text = phonemizer.phonemize(text, 'ms')
    for regex, replacement in _ipa_mapping:
        text = re.sub(regex, replacement, text)
    return text
