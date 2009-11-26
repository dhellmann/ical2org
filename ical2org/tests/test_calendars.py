#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann.  All rights reserved.
#
"""
"""

import os

from ical2org import calendars

test_dir = os.path.join(os.path.dirname(__file__), 'Calendars')

active_names = [ 'ical2org active',
                 'remote ical2org active' ]

def test_discover_all():
    cals = list(calendars.discover(test_dir, False))
    assert len(cals) == 4

def test_discover_active():
    cals = list(calendars.discover(test_dir, True))
    assert len(cals) == 2
    titles = sorted([ c.title for c in cals ])
    assert titles == active_names

def test_get_by_titles():
    cals = list(calendars.get_by_titles(test_dir, active_names))
    assert len(cals) == 2
    titles = sorted([ c.title for c in cals ])
    assert titles == active_names
    
