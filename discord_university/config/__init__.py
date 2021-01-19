from .datamodel.root import ConfigurationRoot

import toml
import cattr
from loguru import logger
from pathlib import Path


def load_configuration(path: Path) -> ConfigurationRoot:
    logger.debug("attempting to load configuration at {}", path.resolve())

    # verify the path exists, and that its a file.
    if not path.exists() or not path.is_file():
        raise FileNotFoundError(f"Specified path {path} does not exist!")
    logger.debug("file seems to exist... loading...")

    # read the text, and parse it immediately as a toml document
    raw = toml.loads(path.read_text())
    logger.debug("loaded raw data, attempting to structure...")
    # convert the raw dictionary into a more proper data structure
    data = cattr.structure(raw, ConfigurationRoot)

    return data
