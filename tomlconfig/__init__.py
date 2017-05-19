import toml


def parse_toml(tomlfile, expected_keys=None):
    """Parse toml with optional keys check

    Parameters
    ----------
    tomlfile : str
        path to TOML file
    expected_keys : sequence
        keys expected in parsed TOML
    """
    with open(tomlfile) as f:
        configkw = toml.load(f)
    if expected_keys is not None:
        expected_keys = set(expected_keys)
        if not set(configkw) == expected_keys:
            raise ValueError('Server config keys set does not match expected: {}'.format(expected_keys))
    return configkw
