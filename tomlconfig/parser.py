import toml

from .postproc import check_required_keys


def parse_toml(tomlfile, required_keys=None):
    """Parse toml with optional keys check

    Parameters
    ----------
    tomlfile : str
        path to TOML file
    required_keys : sequence
        keys required in parsed TOML
    """
    with open(tomlfile) as f:
        configdict = toml.load(f)
    check_required_keys(configdict, required_keys=required_keys)
    return configdict
