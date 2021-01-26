from typing import Set, List

import attr


@attr.define
class Blacklist:
    users: List[int] = attr.ib(factory=list)


@attr.define
class Secrets:
    token: str
    blacklist: Blacklist
