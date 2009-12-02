#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann.  All rights reserved.
#
"""
"""

import vobject
import datetime

from ical2org.diary import DiaryFormatter
from ical2org import tz

def test_format_allday():
    c = vobject.iCalendar()
    e = c.add('vevent')
    e.add('summary').value = "This is a note"
    start = e.add('dtstart')
    start.value = datetime.datetime(2009, 11, 26, tzinfo = tz.local)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 11, 26, tzinfo = tz.local)
    f = DiaryFormatter(None)
    text = f.format_event(e)
    assert text == '11/26/09 00:00-00:00 This is a note\n', text
    return

def test_format_with_calendar_title():
    c = vobject.iCalendar()
    e = c.add('vevent')
    e.add('summary').value = "This is a note"
    start = e.add('dtstart')
    start.value = datetime.datetime(2009, 11, 26, tzinfo = tz.local)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 11, 26, tzinfo = tz.local)
    f = DiaryFormatter(None)
    class FauxCalendar(object):
        title = 'Title'
    f.start_calendar(FauxCalendar())
    text = f.format_event(e)
    assert text == '11/26/09 00:00-00:00 This is a note (Title)\n', text
    return

def test_format_time_range():
    c = vobject.iCalendar()
    e = c.add('vevent')
    e.add('summary').value = "This is a note"
    start = e.add('dtstart')
    start.value = datetime.datetime(2009, 11, 26, 9, 5, tzinfo = tz.local)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 11, 26, 13, 25, tzinfo = tz.local)
    f = DiaryFormatter(None)
    text = f.format_event(e)
    assert text == '11/26/09 09:05-13:25 This is a note\n', text
    return

def test_format_date_range():
    c = vobject.iCalendar()
    e = c.add('vevent')
    e.add('summary').value = "This is a note"
    start = e.add('dtstart')
    start.value = datetime.datetime(2009, 11, 26, 9, 5, tzinfo = tz.local)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 12, 26, 13, 25, tzinfo = tz.local)
    f = DiaryFormatter(None)
    text = f.format_event(e)
    assert text == '%%(diary-block 11 26 2009 12 26 2009) This is a note\n', text
    return
