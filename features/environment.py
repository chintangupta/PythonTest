# -*- coding: utf-8 -*-

import os
import logging

import requests
from behave import *  # noqa


def before_step(context, step):
    logging.debug('Step: {} {}'.format(step.step_type, str(repr(step.name))))


def before_all(context):
    SUT_URL = u'http://jsonplaceholder.typicode.com'
    context.sut_url = SUT_URL

    # get the root logger
    rootLogger = logging.getLogger()

    ## configure the formatter
    fmt='%(asctime)s-%(filename)s[line:%(lineno)d]-%(name)s-%(levelname)s: %(message)s'
    logFormatter = logging.Formatter(fmt)

    ## configure and add file logger
    logFile = "./reports/behave.log"
    fileHandler = logging.FileHandler(logFile)
    fileHandler.setLevel(logging.DEBUG)
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)

    ## configure and add console logger
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    consoleHandler.setLevel(logging.ERROR)
    rootLogger.addHandler(consoleHandler)


def before_scenario(context, scenario):
    logging.debug(u'***************************Started Scenario: {}'
                  .format(str(repr(context.scenario.name))))


def after_scenario(context, scenario):
    logging.debug(u'***************************Finished Scenario: {}\n\n\n\n\n'
                  .format(str(repr(context.scenario.name))))

