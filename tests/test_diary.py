#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann.  All rights reserved.
#
"""
"""

import vobject
import datetime

from ical2org.diary import format_for_diary

def test_format_allday():
    c = vobject.iCalendar()
    e = c.add('vevent')
    e.add('summary').value = "This is a note"
    start = e.add('dtstart')
    utc = vobject.icalendar.utc
    start.value = datetime.datetime(2009, 11, 26, tzinfo = utc)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 11, 26, tzinfo = utc)
    text = format_for_diary(e)
    assert text == '11/26/09 00:00-00:00 This is a note', text
    return

def test_format_with_calendar_title():
    c = vobject.iCalendar()
    e = c.add('vevent')
    e.add('summary').value = "This is a note"
    start = e.add('dtstart')
    utc = vobject.icalendar.utc
    start.value = datetime.datetime(2009, 11, 26, tzinfo = utc)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 11, 26, tzinfo = utc)
    text = format_for_diary(e, 'Title')
    assert text == '11/26/09 00:00-00:00 This is a note (Title)', text
    return

def test_format_time_range():
    c = vobject.iCalendar()
    e = c.add('vevent')
    e.add('summary').value = "This is a note"
    start = e.add('dtstart')
    utc = vobject.icalendar.utc
    start.value = datetime.datetime(2009, 11, 26, 9, 5, tzinfo = utc)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 11, 26, 13, 25, tzinfo = utc)
    text = format_for_diary(e)
    assert text == '11/26/09 09:05-13:25 This is a note', text
    return

def test_format_date_range():
    c = vobject.iCalendar()
    e = c.add('vevent')
    e.add('summary').value = "This is a note"
    start = e.add('dtstart')
    utc = vobject.icalendar.utc
    start.value = datetime.datetime(2009, 11, 26, 9, 5, tzinfo = utc)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 12, 26, 13, 25, tzinfo = utc)
    text = format_for_diary(e)
    assert text == '%%(diary-block 11 26 2009 12 26 2009) This is a note', text
    return
