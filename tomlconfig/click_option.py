

def toml_config_option(keys=None, **clickkwargs):
    """Generate TOML config file option for click

    Parameters
    ----------
    keys : list of str
        top-level keys that are required to be in TOML config
    **clickkwargs : additional keyword arguments
        passed to click.option
        e.g. `required` or `help`

    Returns
    -------
    callable : decorator to use on cli function
    """
    import functools
    import click
    from .click_type import TOMLConfig

    configkey = '__config'

    tomltype = TOMLConfig(required_keys=keys)

    kw = dict(required=True, help='Config TOML file')
    kw.update(clickkwargs)
    toml_option = click.option('--config', '-c', configkey, type=tomltype, **kw)

    def wrap_maker(f):

        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            config = kwargs.pop(configkey)
            if keys is None:
                # subset config
                config = {k:config[k] for k in keys}
            kwargs.update(config)
            return f(*args, **kwargs)

        return toml_option(wrapped)

    return wrap_maker
