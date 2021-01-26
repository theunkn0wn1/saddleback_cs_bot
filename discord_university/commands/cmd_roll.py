from discord.ext import commands

from loguru import logger
import typing
from discord import Role

if typing.TYPE_CHECKING:
    from discord_university.bot import RollHelperClient


class CapsRole(commands.RoleConverter):
    """ cast the role to ALLCAPS before converting it to a discord.role"""

    async def convert(self, ctx, argument):
        ctx.bot: "RollHelperClient"  # type is too dynamic to determine statically without this

        if ctx.author.id in ctx.bot.roll_helper_config.secrets.blacklist.users:
            return await ctx.reply("Cannot comply: unauthorized.")

        argument = argument.upper()
        # resolve aliases
        if argument not in ctx.bot.alias_mapping:
            # sanity check: are we even configured to manage this roll?
            logger.warning(
                f"{ctx.author} @{ctx.author.id} tried request a roll this command isn't "
                f"allowed to give"
            )
            # bail out.
            return await ctx.reply("Cannot comply.")

        logger.debug(
            "role {!r} found in alias map, replacing with {}",
            argument,
            ctx.bot.alias_mapping[argument],
        )
        argument = ctx.bot.alias_mapping[argument]

        return await super().convert(ctx, argument.upper())


@commands.command(
    name="role",
)
async def role(ctx: commands.Context, requested_role: CapsRole):
    requested_role: Role  # its actually this type, not the converter type.
    logger.debug("!role invoked with ctx: {} and requested_role := {!r}", ctx, requested_role)
    ctx.bot: "RollHelperClient"  # again, its actually this type, not what the annotation says.
    if ctx.author.id in ctx.bot.roll_helper_config.secrets.blacklist.users:
        return await ctx.reply("Cannot comply: unauthorized.")

    if requested_role in ctx.author.roles:
        logger.debug("user has the requested role, remove it!")
        await ctx.author.remove_roles(requested_role, reason="roll bot invocation")
        return await ctx.reply(f"{ctx.author.mention} removed from {requested_role.name}")

    logger.debug("assigning role {} to user {}", requested_role, ctx.author)
    await ctx.author.add_roles(requested_role, reason="roll bot invocation")
    await ctx.reply(f"{ctx.author.mention} added to {requested_role.name}")


@commands.command(name="roles")
async def roles(ctx: commands.Context):
    ctx.bot: "RollHelperClient"  # again, its actually this type, not what the annotation says.

    await ctx.reply(
        f"valid roles (case insensitive) :: {', '.join(ctx.bot.alias_mapping.keys())}".casefold()
    )
