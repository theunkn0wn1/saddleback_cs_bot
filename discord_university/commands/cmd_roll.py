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
        else:
            # sanity check: are we even configured to manage this roll?
            logger.warning("someone tried request a roll this command isn't allowed to give")
            # bail out.
            return await ctx.reply("Cannot comply: not authorized.")
        return await super().convert(ctx, argument.upper())


@commands.command(
    name="role-new",
)
async def role(ctx: commands.Context, requested_role: CapsRole):
    requested_role: Role  # its actually this type, not the converter type.
    logger.debug("!role invoked with ctx: {} and requested_role := {!r}", ctx, requested_role)
    ctx.bot: "RollHelperClient"  # again, its actually this type, not what the annotation says.

    if requested_role in ctx.author.roles:
        logger.debug("user has the requested role, remove it!")
        await ctx.author.remove_roles(requested_role, reason="roll bot invocation")
        await ctx.reply(f"{ctx.author.mention} removed from {requested_role.name}")
    else:
        logger.debug("assigning role {} to user {}", requested_role, ctx.author)
        await ctx.author.add_roles(requested_role, reason="roll bot invocation")
        await ctx.reply(f"{ctx.author.mention} added to {requested_role.name}")