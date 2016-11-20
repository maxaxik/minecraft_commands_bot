import json
import logging
import os

log = logging.getLogger(__name__)


def lines(cmd, data):
    yield 'See: <http://minecraft.gamepedia.com/Commands#{}>'.format(cmd)
    yield '```'

    usage = data['usage']
    if not isinstance(usage, list):
        usage = [usage]

    for usage_item in usage:
        yield '{} {}'.format(cmd, usage_item)

    yield '```'


def scope_cmd(bot, cmd, message):
    @bot.command(name=cmd)
    async def callback():
        await bot.say(message)


def load_command_data():
    with open(os.path.join(os.path.dirname(__file__), 'resources', 'game_commands.json')) as fp:
        command_data = json.load(fp)
    return command_data


def load_command_messages():
    command_data = load_command_data()
    for cmd, data in command_data.items():
        message = '\n'.join(lines(cmd, data))
        yield cmd, message


def setup(bot):
    log.info('loading commands...')

    num_commands = 0

    for cmd, message in load_command_messages():
        scope_cmd(bot, cmd, message)
        num_commands += 1

    log.info('finished loading {} commands'.format(num_commands))
