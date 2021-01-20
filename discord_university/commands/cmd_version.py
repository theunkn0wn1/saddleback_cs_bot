try:
    from importlib import metadata
except ImportError:
    import importlib_metadata as metadata

from discord.ext.commands import command, Context


@command(name="version")
async def cmd_version(ctx: Context):
    """ Fetches the current bot version. """
    try:
        return await ctx.reply(f"version {metadata.version('discord_university')}")
    except metadata.PackageNotFoundError:
        return await ctx.reply("version ?.?.? (Unversioned source run) ")
