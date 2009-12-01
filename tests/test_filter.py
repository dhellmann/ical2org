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

calendar = None
utc = vobject.icalendar.utc

def setup():
    global calendar
    global utc
    
    c = vobject.iCalendar()
    calendar = c

    e = c.add('vevent')
    e.add('summary').value = "past"
    start = e.add('dtstart')
    start.value = datetime.datetime(2008, 11, 26, tzinfo = utc)
    end = e.add('dtend')
    end.value = datetime.datetime(2008, 11, 26, tzinfo = utc)

    e = c.add('vevent')
    e.add('summary').value = "present"
    start = e.add('dtstart')
    start.value = datetime.datetime(2009, 11, 26, tzinfo = utc)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 11, 26, tzinfo = utc)

    e = c.add('vevent')
    e.add('summary').value = "future"
    start = e.add('dtstart')
    start.value = datetime.datetime(2010, 11, 26, tzinfo = utc)
    end = e.add('dtend')
    end.value = datetime.datetime(2010, 11, 26, tzinfo = utc)
    return
    

def test_filter_same_day():
    results = list(filter.by_date_range(
            calendar.vevent_list,
            datetime.datetime(2009, 11, 26, tzinfo = utc),
            datetime.datetime(2009, 11, 27, tzinfo = utc),
            ))
    assert len(results) == 1, len(results)
    assert results[0].summary.value == 'present', results[0].summary.value
    return


def test_filter_several_days():
    results = list(filter.by_date_range(
            calendar.vevent_list,
            datetime.datetime(2009, 11, 1, tzinfo = utc),
            datetime.datetime(2009, 11, 30, tzinfo = utc),
        ))
    assert len(results) == 1, len(results)
    assert results[0].summary.value == 'present', results[0].summary.value
    return
    
