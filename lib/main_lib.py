#!/usr/bin/env python
# pylint: disable=missing-docstring

import logging
import sys

logger = logging.getLogger(__name__)

class MainLib(object):

  def __init__(self, params):
    self._username = params.get('username', '')


  def print_username(self):
    print(self.username())


  #
  # getter/setter
  #
  def username(self, *_):
    """get/set _username"""
    if not _:
      return self._username
    self._username = _[0]
    return self


if __name__ == '__main__':

  logging.basicConfig(level=logging.INFO)

  import argparse

  def main():

    parser = argparse.ArgumentParser(description='operate ngrok.')
    parser.add_argument('-p', '--print', action='store_true', default=False, help='Print params')
    args = parser.parse_args()

    params = {
      'username': "iida"
    }

    mainlib = MainLib(params)

    if args.print:
      mainlib.print()

    return 0

  sys.exit(main())
