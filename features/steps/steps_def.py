# -*- coding: utf-8 -*-

import logging

import requests
from behave import *  # noqa



@given(u'the SUT is available')
def step_impl(context):
    try:
        requests.get(context.sut_url)
        logging.debug(u'SUT is available')
    except requests.ConnectionError:
        raise Exception(u'Unable to connect to {} - please ensure the SUT '
                        'is running correctly'.format(context.sut_url))


@when(u'I request to get all posts')
def step_impl(context):
    url = u'{}{}'.format(context.sut_url, '/posts')
    context.response = requests.get(url)
    logging.debug(u'Successfully got all posts')


@then('I should get a list of "{nop}" posts')
def step_impl(context, nop=None):
    posts = context.response.json()
    assert len(posts) == int(nop)
    logging.debug(u'Response contains {} posts'.format(len(posts)))


@when(u'I request to get all comments')
def step_impl(context):
    url = u'{}{}'.format(context.sut_url, '/comments')
    context.response = requests.get(url)
    logging.debug(u'Successfully got all comments')


@then('I should get a list of "{noc}" comments')
def step_impl(context, noc=None):
    comments = context.response.json()
    assert len(comments) == int(noc)
    logging.debug(u'Response contains {} comments'.format(len(comments)))


@when(u'I request to get all albums')
def step_impl(context):
    url = u'{}{}'.format(context.sut_url, '/albums')
    context.response = requests.get(url)
    logging.debug(u'Successfully got all albums')


@then('I should get a list of "{noa}" albums')
def step_impl(context, noa=None):
    albums = context.response.json()
    assert len(albums) == int(noa)
    logging.debug(u'Response contains {} albums'.format(len(albums)))


@when(u'I request to get all photos')
def step_impl(context):
    url = u'{}{}'.format(context.sut_url, '/photos')
    context.response = requests.get(url)
    logging.debug(u'Successfully got all photos')


@then('I should get a list of "{noph}" photos')
def step_impl(context, noph=None):
    photos = context.response.json()
    assert len(photos) == int(noph)
    logging.debug(u'Response contains {} photos'.format(len(photos)))


@when(u'I request to get all todos')
def step_impl(context):
    url = u'{}{}'.format(context.sut_url, '/todos')
    context.response = requests.get(url)
    logging.debug(u'Successfully got all todos')


@then('I should get a list of "{noto}" todos')
def step_impl(context, noto=None):
    todos = context.response.json()
    assert len(todos) == int(noto)
    logging.debug(u'Response contains {} todos'.format(len(todos)))


@when(u'I request to get all users')
def step_impl(context):
    url = u'{}{}'.format(context.sut_url, '/users')
    context.response = requests.get(url)
    logging.debug(u'Successfully got all users')


@then('I should get a list of "{nou}" users')
def step_impl(context, nou=None):
    users = context.response.json()
    assert len(users) == int(nou)
    logging.debug(u'Response contains {} users'.format(len(users)))




