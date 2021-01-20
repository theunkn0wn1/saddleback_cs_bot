from typing import Optional, Dict

import discord
from discord import Guild, Role
from discord.ext.commands import Bot
from loguru import logger

from discord_university.config import ConfigurationRoot

from discord_university.commands.cmd_roll import role as cmd_role


class RollHelperClient(Bot):
    def __init__(self, configuration: ConfigurationRoot, *, loop=None, **options):
        super().__init__(loop=loop, **options)
        self.roll_helper_config = configuration
        """ Bot configuration """
        self._subject_guild: Optional[Guild] = None
        self.alias_mapping = {}
        """
        Mapping that resolves aliases back to the underlying discord role name.
        """
        for role in self.roll_helper_config.rolls:
            for alias in role.aliases:
                self.alias_mapping[alias] = role.name
        logger.debug("alias_map := {}", self.alias_mapping)

        # hook in commands
        self.add_command(cmd_role)

    async def on_ready(self):
        logger.info("bot ready. we are user {} in guilds {}", self.user, self.guilds)

        self._subject_guild = self.get_guild(self.roll_helper_config.guild)
