import logging
import sys

import yaml

from argparse import ArgumentParser

from trackr.notifier.common import NotifierFactory


logger = logging.getLogger(__name__)


def parse_arguments(args: list[str]):
    """"""
    parser = ArgumentParser()
    commands = parser.add_subparsers(required=True, dest='command') 
    
    run = commands.add_parser('run')
    run.add_argument('-t', '--track', nargs='+', required=True, dest='track')
    run.add_argument('-n', '--notify', required=True, dest='notify')
    
    test = commands.add_parser('test')
    test.add_argument('notify', metavar='notify')
    
    return parser.parse_args(args)


def main(argv: list[str]):
    """"""
    parsed = parse_arguments(argv[1:])
    
    notifiers = []

    with open(parsed.notify) as file:
        notifier_configs = yaml.safe_load(file)
        for notifier_config in notifier_configs:
            name = notifier_config['name']
            notifier_class = NotifierFactory.get_class(name)
            notifier = notifier_class.from_dict(notifier_config['kwargs'])
            notifiers.append(notifier)

    print(notifiers[0].user_key)


    # with open(parsed.notify) as file:
    #     loaded = yaml.safe_load(file)
    #     notifier_class = NotifierFactory.get_class(loaded['name'])
    #     notifier = notifier_class.from_dict(loaded['notifier'])
    #     for event in ['in_stock', 'no_stock', 'error']:
    #         if event not in loaded['when']:
    #             print(f"Skipping event '{event}'.")
    #             continue
    #         print(f"Testing event '{event}'... ", end='')
    #         notifier.execute(f'Test Event: {event}', 'Just checking :)')
    #         print('Sent.')


if __name__ == '__main__':
    main(sys.argv)
