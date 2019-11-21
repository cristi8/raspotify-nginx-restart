#!/usr/bin/env python3

import os
import logging
import time

logger = logging.getLogger(__name__)
PATH = '/etc/restart-raspotify'


def check():
    try:
        with open(PATH, 'r') as f:
            val = int(f.read().strip() or '0')
    except Exception as ex:
        logger.error("Can't get config value from %s: %s", PATH, ex)
        return

    if val:
        logger.info("Restarting raspotify...")
        os.system('systemctl restart raspotify')
        with open(PATH, 'w') as f:
            f.write('0')


def main():
    logging.basicConfig(level=logging.INFO)
    logger.info("Watching file %s...", PATH)

    while True:
        try:
            check()
        except Exception as ex:
            logger.error('Error: %s', ex)

        time.sleep(1)


if __name__ == '__main__':
    main()
