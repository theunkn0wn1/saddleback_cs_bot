import discord
from loguru import logger

from discord_university.config import ConfigurationRoot


class RollHelperClient(discord.Client):
    def __init__(self, configuration: ConfigurationRoot, *, loop=None, **options):
        super().__init__(loop=loop, **options)
        self._roll_config = configuration

    async def on_ready(self):
        logger.info("bot ready. we are user {} in guilds {}", self.user, self.guilds)