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

CALENDAR_DATA = """BEGIN:VCALENDAR\r
VERSION:2.0\r
PRODID:-//Apple Inc.//iCal 3.0//EN\r
CALSCALE:GREGORIAN\r
BEGIN:VEVENT\r
UID:040000008200E00074C5B7101A82E00800000000A008AB984D59CA0100000000000000\r
 0010000000A692F000C5BC0C4EB7AC6BB83BBB4391\r
DTSTART;TZID=EST:20091106T133000\r
DTEND;TZID=EST:20091106T143000\r
ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-PARTICIPANT;CN=everyone;RSVP=TRUE:mail\r
 to:everyone@example.com\r
ATTENDEE;CUTYPE=INDIVIDUAL;PARTSTAT=ACCEPTED:mailto:test@example.com\r
CREATED:20100315T180322Z\r
DESCRIPTION:This meeting starts outside DST and recurs inside.\r
DTSTAMP:20091030T144154Z\r
LOCATION:Boardroom\r
ORGANIZER:mailto:test@example.com\r
RRULE:FREQ=WEEKLY;INTERVAL=2;BYDAY=FR\r
SEQUENCE:0\r
STATUS:CONFIRMED\r
SUMMARY:Recurring DST meeting\r
TRANSP:OPAQUE\r
BEGIN:VALARM\r
ACTION:DISPLAY\r
DESCRIPTION:Reminder\r
TRIGGER:-PT15M\r
X-WR-ALARMUID:907071B7-E769-41C9-9303-93C5D54BC19C\r
END:VALARM\r
END:VEVENT\r
END:VCALENDAR\r
"""

def test_filter_dst_event_in_dst():
    components = list(vobject.readComponents(CALENDAR_DATA))
    events = components[0].vevent_list
    results = list(filter.by_date_range(
            events,
            datetime.datetime(2009, 11, 5, tzinfo = utc),
            datetime.datetime(2009, 11, 7, tzinfo = utc),
            ))
    assert len(results) == 1
    return

def test_filter_dst_event_out_of_dst():
    components = list(vobject.readComponents(CALENDAR_DATA))
    events = components[0].vevent_list
    results = list(filter.by_date_range(
            events,
            datetime.datetime(2010, 3, 20, tzinfo = utc),
            datetime.datetime(2010, 3, 28, tzinfo = utc),
            ))
    assert len(results) == 1
    return
