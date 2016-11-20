import logging

from discord.ext import commands

log = logging.getLogger(__name__)

extensions = [
    'game_commands'
]

description = '''Minecraft commands helper bot.

Type `::` followed by a Minecraft command for help with that command.'''

bot = commands.Bot(command_prefix='::', description=description, help_attrs={'name': '_help', 'hidden': True})


@bot.event
async def on_ready():
    log.info('logged in as {} (id {})'.format(bot.user.name, bot.user.id))

    log.info('loading extensions...')

    num_extensions = 0

    for ext in extensions:
        log.info('loading extension: {}'.format(ext))
        bot.load_extension('extensions.' + ext)
        num_extensions += 1

    log.info('finished loading {} extensions'.format(num_extensions))


def run(*args, **kwargs):
    bot.run(*args, **kwargs)
