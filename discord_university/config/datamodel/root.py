import attr
from typing import List, Optional

from .roll import Roll
from .secrets import Secrets


@attr.define
class ConfigurationRoot:
    rolls: List[Roll] = attr.ib(
        validator=attr.validators.deep_iterable(
            member_validator=attr.validators.instance_of(Roll),
            iterable_validator=attr.validators.instance_of(list),
        )
    )
    secrets: Optional[Secrets] = attr.ib(
        validator=attr.validators.optional(attr.validators.instance_of(Secrets))
    )
    guild: int  # TODO: validator
    command_prefix: str = attr.ib(default="!", validator=attr.validators.instance_of(str))
