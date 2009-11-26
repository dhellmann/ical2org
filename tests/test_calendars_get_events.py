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
calendar_dir = os.path.join(test_dir, 'active.calendar')

def test_all():
    cal = calendars.Calendar(calendar_dir)
    events = list(cal.get_events())
    assert len(events) == 5
