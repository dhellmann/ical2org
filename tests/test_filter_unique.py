#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann.  All rights reserved.
#
"""
"""

import datetime

import vobject

from ical2org import filter

utc = vobject.icalendar.utc

def test_same_start_time():
    c = vobject.iCalendar()

    e = c.add('vevent')
    one = e
    one.add('uid').value = 'one_uid'
    e.add('summary').value = "one"
    start = e.add('dtstart')
    start.value = datetime.datetime(2009, 11, 26, tzinfo = utc)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 11, 26, tzinfo = utc)

    e = c.add('vevent')
    e.add('uid').value = 'one_uid'
    e.add('summary').value = "two"
    start = e.add('dtstart')
    start.value = datetime.datetime(2009, 11, 26, tzinfo = utc)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 11, 26, tzinfo = utc)

    results = list(filter.unique(c.vevent_list))
    assert len(results) == 1, len(results)
    assert results[0].summary.value == 'one', results[0].summary.value
    return

def test_diff_start_time():
    c = vobject.iCalendar()

    e = c.add('vevent')
    one = e
    one.add('uid').value = 'one_uid'
    e.add('summary').value = "one"
    start = e.add('dtstart')
    start.value = datetime.datetime(2009, 11, 26, tzinfo = utc)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 11, 26, tzinfo = utc)

    e = c.add('vevent')
    e.add('uid').value = 'one_uid'
    e.add('summary').value = "two"
    start = e.add('dtstart')
    start.value = datetime.datetime(2009, 11, 27, tzinfo = utc)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 11, 27, tzinfo = utc)

    results = list(filter.unique(c.vevent_list))
    assert len(results) == 2, len(results)
    assert [ r.summary.value for r in results ] == [ 'one', 'two' ], results[0].summary.value
    return
    
