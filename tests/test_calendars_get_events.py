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

def test_all():
    cal = calendars.get_by_titles(test_dir, ['ical2org active']).next()
    events = list(cal.get_events())
    assert len(events) == 5
