"""
Utility script to append new roles to an existing configuration
"""

import click
from loguru import logger
from .config.datamodel import Roll, ConfigurationRoot
from .config import load_configuration, write_configuration

from pathlib import Path


@click.command("add_roll")
@click.option("--name", default=None, help="name of the roll in discord")
@click.option("--alias", "-a", multiple=True, default=None, type=str)
@click.argument("path", type=click.Path(exists=True, path_type=click.File))
def add_roll(path: bytes, name, alias):
    logger.debug("called with path := {} and name := {!r} aliases := {!r}", path, name, alias)

    # ensure there is always one alias: the name of the roll.
    if not alias:
        alias = [name]

    roll = Roll(
        name=name,
        aliases=list(alias)
    )
    click.confirm(f"creating roll {roll!r}. This look about right?", abort=True)

    logger.trace("user confirmed generation. loading config....")
    # if we get this far they have their roll and have confirmed to generate it.
    # load the configuration file
    # decode the path and load the configuration into memory
    path = Path(path.decode())
    config = load_configuration(path)

    # append new roll.
    config.rolls.append(roll)

    write_configuration(path, config)


if __name__ == "__main__":
    add_roll()
