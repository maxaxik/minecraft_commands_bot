import argparse
import logging

import minecraft_commands_bot

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('token')
arg_parser.add_argument('--log', help='log level')
args = arg_parser.parse_args()

logging.basicConfig(level=args.log)

minecraft_commands_bot.run(args.token)
