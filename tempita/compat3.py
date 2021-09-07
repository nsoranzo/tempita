__all__ = ['b', 'basestring_', 'bytes', 'next', 'is_unicode']


def b(s):
    if isinstance(s, str):
        return s.encode('latin1')
    return bytes(s)


basestring_ = (bytes, str)
text = str


def is_unicode(obj):
    return isinstance(obj, str)


def coerce_text(v):
    if not isinstance(v, basestring_):
        attr = '__str__'
        if hasattr(v, attr):
            return str(v)
        else:
            return bytes(v)
    return v
