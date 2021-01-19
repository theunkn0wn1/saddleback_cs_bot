import attr
from typing import List


@attr.define
class Roll:
    name: str
    aliases: List[str]
