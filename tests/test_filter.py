#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann.  All rights reserved.
#
"""
"""

import datetime

import dateutil
import vobject

from ical2org import filter, tz

calendar = None
utc = vobject.icalendar.utc
local = tz.local

def setup():
    global calendar
    global utc
    
    c = vobject.iCalendar()
    calendar = c

    e = c.add('vevent')
    e.add('summary').value = "past"
    start = e.add('dtstart')
    start.value = datetime.datetime(2008, 11, 26, tzinfo = local)
    end = e.add('dtend')
    end.value = datetime.datetime(2008, 11, 26, tzinfo = local)

    e = c.add('vevent')
    e.add('summary').value = "present"
    start = e.add('dtstart')
    start.value = datetime.datetime(2009, 11, 26, tzinfo = local)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 11, 26, tzinfo = local)

    e = c.add('vevent')
    e.add('summary').value = "future"
    start = e.add('dtstart')
    start.value = datetime.datetime(2010, 11, 26, tzinfo = local)
    end = e.add('dtend')
    end.value = datetime.datetime(2010, 11, 26, tzinfo = local)
    return
    

def test_filter_same_day():
    results = list(filter.by_date_range(
            calendar.vevent_list,
            datetime.datetime(2009, 11, 26, tzinfo = local),
            datetime.datetime(2009, 11, 27, tzinfo = local),
            ))
    assert len(results) == 1, len(results)
    assert results[0].summary.value == 'present', results[0].summary.value
    return


def test_filter_several_days():
    results = list(filter.by_date_range(
            calendar.vevent_list,
            datetime.datetime(2009, 11, 1, tzinfo = local),
            datetime.datetime(2009, 11, 30, tzinfo = local),
        ))
    assert len(results) == 1, len(results)
    assert results[0].summary.value == 'present', results[0].summary.value
    return
    
