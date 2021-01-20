from discord.ext import commands

from loguru import logger
import typing
from discord import Role

if typing.TYPE_CHECKING:
    from discord_university.bot import RollHelperClient


class CapsRole(commands.RoleConverter):
    """ cast the role to ALLCAPS before converting it to a discord.role"""

    async def convert(self, ctx, argument):
        ctx.bot: "RollHelperClient"
        argument = argument.upper()
        # resolve aliases
        if argument in ctx.bot.alias_mapping:
            logger.debug(
                "role {!r} found in alias map, replacing with {}",
                argument,
                ctx.bot.alias_mapping[argument],
            )
            argument = ctx.bot.alias_mapping[argument]

        return await super().convert(ctx, argument.upper())


@commands.command(
    name="role-new",
)
async def role(ctx: commands.Context, requested_role: CapsRole):
    requested_role: Role  # its actually this type, not the converter type.
    logger.debug("!role invoked with ctx: {} and requested_role := {!r}", ctx, requested_role)
    ctx.bot: "RollHelperClient"
    # logger.debug("assigning role {} to user {}", )
