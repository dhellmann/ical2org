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
    e.add('summary').value = "weekly expired"
    start = e.add('dtstart')
    utc = vobject.icalendar.utc
    start.value = datetime.datetime(2008, 11, 26, 13, 00, tzinfo = utc)
    end = e.add('dtend')
    end.value = datetime.datetime(2008, 11, 26, 14, 00, tzinfo = utc)
    rrule = e.add('rrule')
    rrule.value = 'FREQ=WEEKLY;INTERVAL=1;UNTIL=20090101T045959Z'

    e = c.add('vevent')
    e.add('summary').value = "daily expired"
    start = e.add('dtstart')
    utc = vobject.icalendar.utc
    start.value = datetime.datetime(2008, 11, 26, 13, 00, tzinfo = utc)
    end = e.add('dtend')
    end.value = datetime.datetime(2008, 11, 26, 14, 00, tzinfo = utc)
    rrule = e.add('rrule')
    rrule.value = 'FREQ=DAILY;INTERVAL=1;UNTIL=20090101T045959Z'

    e = c.add('vevent')
    e.add('summary').value = "weekly"
    start = e.add('dtstart')
    utc = vobject.icalendar.utc
    start.value = datetime.datetime(2009, 11, 26, 13, 00, tzinfo = utc)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 11, 26, 14, 00, tzinfo = utc)
    rrule = e.add('rrule')
    rrule.value = 'FREQ=WEEKLY;INTERVAL=1'

    e = c.add('vevent')
    e.add('summary').value = "daily"
    start = e.add('dtstart')
    utc = vobject.icalendar.utc
    start.value = datetime.datetime(2009, 11, 26, 13, 00, tzinfo = utc)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 11, 26, 14, 00, tzinfo = utc)
    rrule = e.add('rrule')
    rrule.value = 'FREQ=DAILY;INTERVAL=1'

    e = c.add('vevent')
    e.add('summary').value = "weekly future"
    start = e.add('dtstart')
    utc = vobject.icalendar.utc
    start.value = datetime.datetime(2010, 11, 26, 13, 00, tzinfo = utc)
    end = e.add('dtend')
    end.value = datetime.datetime(2010, 11, 26, 14, 00, tzinfo = utc)
    rrule = e.add('rrule')
    rrule.value = 'FREQ=WEEKLY;INTERVAL=1'

    e = c.add('vevent')
    e.add('summary').value = "daily future"
    start = e.add('dtstart')
    utc = vobject.icalendar.utc
    start.value = datetime.datetime(2010, 11, 26, 13, 00, tzinfo = utc)
    end = e.add('dtend')
    end.value = datetime.datetime(2010, 11, 26, 14, 00, tzinfo = utc)
    rrule = e.add('rrule')
    rrule.value = 'FREQ=DAILY;INTERVAL=1'

    return
    

def test_filter_one_day():
    results = list(filter.by_date_range(
            calendar.vevent_list,
            datetime.datetime(2009, 11, 26, tzinfo = utc),
            datetime.datetime(2009, 11, 27, tzinfo = utc),
            ))
    summaries = [ r.summary.value for r in results ]
    assert summaries == ['weekly', 'daily'], summaries
    return

def test_filter_several_days():
    results = list(filter.by_date_range(
            calendar.vevent_list,
            datetime.datetime(2009, 11, 1, tzinfo = utc),
            datetime.datetime(2009, 11, 30, tzinfo = utc),
        ))
    summaries = [ (r.summary.value, r.dtstart.value) for r in results ]
    assert summaries == [
        ('weekly', datetime.datetime(2009, 11, 26, 13, 00, tzinfo=utc)),
        ('daily', datetime.datetime(2009, 11, 26, 13, 00, tzinfo=utc)),
        ('daily', datetime.datetime(2009, 11, 27, 13, 00, tzinfo=utc)),
        ('daily', datetime.datetime(2009, 11, 28, 13, 00, tzinfo=utc)),
        ('daily', datetime.datetime(2009, 11, 29, 13, 00, tzinfo=utc)),
        ], summaries
    return
    
