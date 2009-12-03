#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann.  All rights reserved.
#
"""
"""
from cStringIO import StringIO

import vobject
import datetime

from ical2org.org import OrgTreeFormatter
from ical2org import tz

def test_format_allday():
    c = vobject.iCalendar()
    e = c.add('vevent')
    e.add('summary').value = "This is a note"
    start = e.add('dtstart')
    start.value = datetime.datetime(2009, 11, 6, tzinfo = tz.local)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 11, 6, tzinfo = tz.local)
    f = OrgTreeFormatter(None)
    text = f.format_event(e)
    assert text == '** This is a note\n   <2009-11-06 Fri 00:00-00:00>\n', text
    return

def test_format_with_calendar_title():
    c = vobject.iCalendar()
    e = c.add('vevent')
    e.add('summary').value = "This is a note"
    start = e.add('dtstart')
    start.value = datetime.datetime(2009, 11, 6, tzinfo = tz.local)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 11, 6, tzinfo = tz.local)
    output = StringIO()
    f = OrgTreeFormatter(output)
    class FauxCalendar(object):
        title = 'Title'
    f.start_calendar(FauxCalendar())
    f.add_event(e)
    text = output.getvalue()
    assert text == '* Title\n** This is a note\n   <2009-11-06 Fri 00:00-00:00>\n', text
    return

def test_format_time_range():
    c = vobject.iCalendar()
    e = c.add('vevent')
    e.add('summary').value = "This is a note"
    start = e.add('dtstart')
    start.value = datetime.datetime(2009, 11, 26, 9, 5, tzinfo = tz.local)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 11, 26, 13, 25, tzinfo = tz.local)
    f = OrgTreeFormatter(None)
    text = f.format_event(e)
    assert text == '** This is a note\n   <2009-11-26 Thu 09:05-13:25>\n', text
    return

def test_format_date_range():
    c = vobject.iCalendar()
    e = c.add('vevent')
    e.add('summary').value = "This is a note"
    start = e.add('dtstart')
    start.value = datetime.datetime(2009, 11, 26, 9, 5, tzinfo = tz.local)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 12, 26, 13, 25, tzinfo = tz.local)
    f = OrgTreeFormatter(None)
    text = f.format_event(e)
    expected = '** This is a note\n   <2009-11-26 Thu 09:05>--<2009-12-26 Sat 13:25>\n'
    print repr(expected)
    print repr(text)
    assert text == expected, text
    return
