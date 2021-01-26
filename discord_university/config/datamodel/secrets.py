from typing import Set

import attr


class Blacklist:
    users: Set[int] = attr.ib(factory=list)


@attr.define
class Secrets:
    token: str
    blacklist: Blacklist
