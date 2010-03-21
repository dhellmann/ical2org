#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann.  All rights reserved.
#
"""
"""

import datetime

import vobject

from ical2org import filter, tz

calendar = None
local = tz.local

def setup():
    global calendar
    
    c = vobject.iCalendar()
    calendar = c

    e = c.add('vevent')
    e.add('summary').value = "weekly expired"
    start = e.add('dtstart')
    start.value = datetime.datetime(2008, 11, 26, 13, 00, tzinfo = local)
    end = e.add('dtend')
    end.value = datetime.datetime(2008, 11, 26, 14, 00, tzinfo = local)
    rrule = e.add('rrule')
    rrule.value = 'FREQ=WEEKLY;INTERVAL=1;UNTIL=20090101T045959Z'

    e = c.add('vevent')
    e.add('summary').value = "daily expired"
    start = e.add('dtstart')
    start.value = datetime.datetime(2008, 11, 26, 13, 00, tzinfo = local)
    end = e.add('dtend')
    end.value = datetime.datetime(2008, 11, 26, 14, 00, tzinfo = local)
    rrule = e.add('rrule')
    rrule.value = 'FREQ=DAILY;INTERVAL=1;UNTIL=20090101T045959Z'

    e = c.add('vevent')
    e.add('summary').value = "weekly"
    start = e.add('dtstart')
    start.value = datetime.datetime(2009, 11, 26, 13, 00, tzinfo = local)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 11, 26, 14, 00, tzinfo = local)
    rrule = e.add('rrule')
    rrule.value = 'FREQ=WEEKLY;INTERVAL=1'

    e = c.add('vevent')
    e.add('summary').value = "daily"
    start = e.add('dtstart')
    start.value = datetime.datetime(2009, 11, 26, 13, 00, tzinfo = local)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 11, 26, 14, 00, tzinfo = local)
    rrule = e.add('rrule')
    rrule.value = 'FREQ=DAILY;INTERVAL=1'

    e = c.add('vevent')
    e.add('summary').value = "weekly future"
    start = e.add('dtstart')
    start.value = datetime.datetime(2010, 11, 26, 13, 00, tzinfo = local)
    end = e.add('dtend')
    end.value = datetime.datetime(2010, 11, 26, 14, 00, tzinfo = local)
    rrule = e.add('rrule')
    rrule.value = 'FREQ=WEEKLY;INTERVAL=1'

    e = c.add('vevent')
    e.add('summary').value = "daily future"
    start = e.add('dtstart')
    start.value = datetime.datetime(2010, 11, 26, 13, 00, tzinfo = local)
    end = e.add('dtend')
    end.value = datetime.datetime(2010, 11, 26, 14, 00, tzinfo = local)
    rrule = e.add('rrule')
    rrule.value = 'FREQ=DAILY;INTERVAL=1'

    return
    

def test_filter_one_day():
    results = list(filter.by_date_range(
            calendar.vevent_list,
            datetime.datetime(2009, 11, 26, tzinfo = local),
            datetime.datetime(2009, 11, 27, tzinfo = local),
            ))
    summaries = [ r.summary.value for r in results ]
    assert summaries == ['weekly', 'daily'], summaries
    return

def test_filter_several_days():
    results = list(filter.by_date_range(
            calendar.vevent_list,
            datetime.datetime(2009, 11, 1, tzinfo = local),
            datetime.datetime(2009, 11, 30, tzinfo = local),
        ))
    summaries = [ (r.summary.value, r.dtstart.value) for r in results ]
    print summaries
    assert summaries == [
        ('weekly', datetime.datetime(2009, 11, 26, 13, 0, tzinfo=local)),
        ('daily',  datetime.datetime(2009, 11, 26, 13, 0, tzinfo=local)),
        ('daily',  datetime.datetime(2009, 11, 27, 13, 0, tzinfo=local)),
        ('daily',  datetime.datetime(2009, 11, 28, 13, 0, tzinfo=local)),
        ('daily',  datetime.datetime(2009, 11, 29, 13, 0, tzinfo=local)),
        ]
    return
    
