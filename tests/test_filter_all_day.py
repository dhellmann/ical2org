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
    
def test_one_day():
    # See issue #2
    c = vobject.iCalendar()
    calendar = c

#     VEVENT
#         DTSTAMP: 2007-09-24 06:51:23+00:00
#         UID: EF86F13E-2130-42F5-8809-D37251BB7B7D
#         SEQUENCE: 5
#         CREATED: 2009-02-14 17:04:06+00:00
#         TRANSP: OPAQUE
#         SUMMARY: Marcel vrij
#         EXDATE: [datetime.date(2009, 3, 27)]
#         params for  EXDATE:
#            VALUE [u'DATE']
#         EXDATE: [datetime.date(2009, 3, 20)]
#         params for  EXDATE:
#            VALUE [u'DATE']
#         DTEND: 2007-09-21
#         params for  DTEND:
#            VALUE [u'DATE']
#         DTSTART: 2007-09-21
#         params for  DTSTART:
#            VALUE [u'DATE']
#         RRULE: FREQ=WEEKLY;INTERVAL=1

    e = c.add('vevent')
    e.add('summary').value = "Marcel vrij"
    start = e.add('dtstart')
    start.value = datetime.date(2007, 9, 21)
    end = e.add('dtend')
    end.value = datetime.date(2007, 9, 22)
    results = list(filter.by_date_range(
            calendar.vevent_list,
            datetime.datetime(2007, 9, 19, tzinfo = local),
            datetime.datetime(2007, 9, 23, tzinfo = local),
            ))
    event = results[0]
    print 'START:', event.dtstart.value
    print 'END  :', event.dtend.value
    assert event.dtstart.value == datetime.date(2007, 9, 21)
    assert event.dtend.value == datetime.date(2007, 9, 22)
    return
    
