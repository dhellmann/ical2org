#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann.  All rights reserved.
#
"""
"""

from cStringIO import StringIO
import datetime

import vobject
utc = vobject.icalendar.utc

from ical2org import filter

CALENDAR_DATA = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Apple Inc.//iCal 3.0//EN
CALSCALE:GREGORIAN
BEGIN:VEVENT
SEQUENCE:17
TRANSP:OPAQUE
UID:04384ECB-DCD9-4A95-9FD7-D5483CE6F659
DTSTART;TZID=America/New_York:20080314T130000
STATUS:CONFIRMED
DTSTAMP:20080310T115347Z
SUMMARY:Status report
EXDATE;TZID=America/New_York:20080314T130000
CREATED:20090516T010238Z
DTEND;TZID=America/New_York:20080314T131500
RRULE:FREQ=WEEKLY;INTERVAL=1;UNTIL=20080321T035959Z
END:VEVENT
END:VCALENDAR
"""

def event_generator():
    calendar = vobject.readComponents(StringIO(CALENDAR_DATA))
    for c in calendar:
        for e in c.vevent_list:
            yield e

def test_exclude():
    results = list(filter.by_date_range(
            event_generator(),
            datetime.datetime(2009, 3, 21, tzinfo=utc),
            datetime.datetime(2009, 3, 21, tzinfo=utc),
            ))
    assert len(results) == 0, results

def test_include():
    results = list(filter.by_date_range(
            event_generator(),
            datetime.datetime(2008, 3, 13, tzinfo=utc),
            datetime.datetime(2008, 3, 15, tzinfo=utc),
            ))
    assert len(results) == 1, results
    
