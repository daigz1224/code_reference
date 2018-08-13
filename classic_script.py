"""
 File Name: classic_script.py
    Author: Dai Guozheng
    E-mail: daiguozheng@baidu.com
Created on: Mon Aug 13 2018 20:00:00 CST

"""

import os
import argparse
import logging

import ipdb
assert ipdb

DESCRIPTION = """
"""


def runcmd(cmd):
    """
    Run command.
    :param cmd:
    :return:
    """
    logging.info("%s" % cmd)
    os.system(cmd)

def getargs():
    """
    Parse program arguments.
    :return:
    """
    parser = argparse.ArgumentParser(
        description=DESCRIPTION,
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--log", type=str, default="INFO",
                        help="log level")

    return parser.parse_args()

def main(args):
    """
    Main entry.
    :param args:
    :return:
    """

if __name__ == '__main__':
    args = getargs()
    numeric_level = getattr(logging, args.log.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError("Invalid log level: " + args.log)
    logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s",
                        level=numeric_level)
    main(args)
