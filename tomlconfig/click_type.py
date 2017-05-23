import click
import toml

from .postproc import check_required_keys


class TOMLConfig(click.ParamType):

    name = 'tomlconfig'

    def __init__(self, required_keys=None, squeeze=False):
        """TOML config file to dict

        Parameters
        ----------
        required_keys : list of str
            keys that must be in the top level of the config dict
            or the squeezed level
        squeeze : bool
            squeeze single-key top level from config dict
        """
        self.required_keys = required_keys
        self.squeeze = squeeze

    def convert(self, value, param, ctx):
        try:
            fin = open(value, 'r')
        except IOError as exc:
            self.fail('Unable to open \'{}\' for reading ({}).'.format(value, exc), param, ctx)
        try:
            configkw = toml.load(fin)
        except (TypeError, toml.TomlDecodeError) as exc:
            self.fail('Unable to parse TOML from \'{}\' ({}).'.format(value, exc), param, ctx)
        if self.squeeze and len(configkw) == 1:
            configkw = configkw[list(configkw)[0]]
        try:
            check_required_keys(configkw, required_keys=self.required_keys)
        except ValueError as exc:
            self.fail(str(exc), param, ctx)
        return configkw
