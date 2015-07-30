#!/usr/bin/env python3
# -*-coding:utf-8 -*
__author__ = 'Yann Finidori'

import argparse
import sys, os
import logging
import urllib.request
import shutil

Logger = logging.getLogger("toto")

#conf
notInDocker = {'code': 200, 'image': 'inception.ansi'}
inDocker = {'code': 100, 'image': 'docker.ansi'}
url = 'https://raw.githubusercontent.com/mfy2a/dockerornot/master/images/'

def setImages():

    if not(os.path.isdir(os.getenv("HOME") + '/.dockerOrNot')):
        os.makedirs(os.getenv("HOME") + '/.dockerOrNot')
        Logger.debug('no .dockerOrNot ... creating it')
        #in Docker image
        urllib.request.urlretrieve(url + str(inDocker['image']), os.getenv("HOME") + '/.dockerOrNot/' + str(inDocker['image']))

        #NOT in Docker image
        urllib.request.urlretrieve(url + str(notInDocker['image']), os.getenv("HOME") + '/.dockerOrNot/' + str(notInDocker['image']))


def amIDreaming():
    setImages()
    if not(os.path.exists('/.dockerinit')):
        Logger.info('not in Docker')
        with open(os.getenv("HOME") + '/.dockerOrNot/' + str(notInDocker['image']), encoding="ascii") as txt:
            Logger.info(txt.read())
        sys.exit(notInDocker['code'])
    else:
        Logger.info('in Docker')
        with open(os.getenv("HOME") + '/.dockerOrNot/' + str(inDocker['image']), encoding="ascii") as txt:
            Logger.info(txt.read())
        sys.exit(inDocker['code'])


def main():
    parser = argparse.ArgumentParser()
#    parser.add_argument("url", type=str, help="URL or HOST" )
    #options
    parser.add_argument("-v", "--verbose", action="store_true",default=False, dest="info", help="verbose mode with ASCII ART")
    parser.add_argument("-d", "--debug", action="store_true",default=False, dest="debug", help="debug mode")
    args = parser.parse_args()

    if args.debug == True:
        Logger.setLevel(logging.DEBUG)
        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        Logger.addHandler(consoleHandler)

    if args.info == True:
        Logger.setLevel(logging.INFO)
        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(logging.Formatter('%(message)s'))
        Logger.addHandler(consoleHandler)

    amIDreaming()


if __name__ == "__main__":
    sys.exit(main())