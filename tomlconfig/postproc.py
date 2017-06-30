

def check_required_keys(configdict, required_keys=None):
    if required_keys is None:
        return
    if not set(configdict).issuperset(set(required_keys)):
        raise ValueError(
                'Config keys do not match required: {}'
                ''.format(required_keys))
