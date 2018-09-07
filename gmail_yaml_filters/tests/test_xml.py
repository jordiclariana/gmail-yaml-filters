# -*- coding: utf-8 -*-

from __future__ import unicode_literals


import pytest
from gmail_yaml_filters.main import RuleSet
from gmail_yaml_filters.main import ruleset_to_xml


NS = {'apps': 'http://schemas.google.com/apps/2006'}


def sample_rule(name):
    return {
        'from': '{}@aapl.com'.format(name),
        'trash': True,
    }


@pytest.fixture
def ruleset():
    return RuleSet.from_object([sample_rule('alice'), sample_rule('🐶')])


def test_ruleset_to_xml(ruleset):
    """
    A hideous, basic, but working integration test for turning rules into XML.
    """
    xml = ruleset_to_xml(ruleset, pretty_print=False)
    assert '<apps:property name="from" value="alice@aapl.com"/><apps:property name="shouldTrash" value="true"/></entry>' in xml
    assert '<apps:property name="from" value="🐶@aapl.com"/><apps:property name="shouldTrash" value="true"/></entry>' in xml
