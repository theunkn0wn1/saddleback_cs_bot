import click

from loguru import logger

from .config import load_configuration
from .bot import RollHelperClient
from pathlib import Path


@click.command("run")
@click.argument("path", type=click.Path(exists=True, file_okay=True, dir_okay=False))
def run(path: str):
    path = Path(path)
    config = load_configuration(path)
    logger.info("loaded configuration from {}", path)

    logger.trace("spawning client...")
    client = RollHelperClient(configuration=config)

    logger.info("spawning discord client....")
    client.run(config.secrets.token)


run()
