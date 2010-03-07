#!/usr/bin/env python
# coding: utf-8
#
# Copyright (c) 2009 Doug Hellmann.  All rights reserved.
#
"""
"""
from ConfigParser import SafeConfigParser as ConfigParser
from cStringIO import StringIO
import os

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
    output = StringIO()
    f = OrgTreeFormatter(output, ConfigParser(), None)
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
    f = OrgTreeFormatter(output, ConfigParser(), None)
    class FauxCalendar(object):
        title = 'Title'
    f.start_calendar(FauxCalendar())
    f.add_event(e)
    text = output.getvalue()
    assert text == '# -*- coding: utf-8 -*-\n* Title\n  :CATEGORY: Title\n** This is a note\n   <2009-11-06 Fri 00:00-00:00>\n'
    return

def test_format_with_description():
    c = vobject.iCalendar()
    e = c.add('vevent')
    e.add('summary').value = "This is a note"
    e.add('description').value = "This is more detail\non two lines"
    start = e.add('dtstart')
    start.value = datetime.datetime(2009, 11, 6, tzinfo = tz.local)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 11, 6, tzinfo = tz.local)
    output = StringIO()
    f = OrgTreeFormatter(output, ConfigParser(), None)
    class FauxCalendar(object):
        title = 'Title'
    f.start_calendar(FauxCalendar())
    f.add_event(e)
    text = output.getvalue()
    expected = '# -*- coding: utf-8 -*-\n* Title\n  :CATEGORY: Title\n** This is a note\n   <2009-11-06 Fri 00:00-00:00>\n   - This is more detail\n     on two lines\n'
    print repr(expected)
    print repr(text)
    assert text == expected
    return

def test_format_with_empty_description():
    c = vobject.iCalendar()
    e = c.add('vevent')
    e.add('summary').value = "This is a note"
    e.add('description').value = ""
    start = e.add('dtstart')
    start.value = datetime.datetime(2009, 11, 6, tzinfo = tz.local)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 11, 6, tzinfo = tz.local)
    output = StringIO()
    f = OrgTreeFormatter(output, ConfigParser(), None)
    class FauxCalendar(object):
        title = 'Title'
    f.start_calendar(FauxCalendar())
    f.add_event(e)
    text = output.getvalue()
    expected = '# -*- coding: utf-8 -*-\n* Title\n  :CATEGORY: Title\n** This is a note\n   <2009-11-06 Fri 00:00-00:00>\n'
    print repr(expected)
    print repr(text)
    assert text == expected
    return

def test_format_time_range():
    c = vobject.iCalendar()
    e = c.add('vevent')
    e.add('summary').value = "This is a note"
    start = e.add('dtstart')
    start.value = datetime.datetime(2009, 11, 26, 9, 5, tzinfo = tz.local)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 11, 26, 13, 25, tzinfo = tz.local)
    output = StringIO()
    f = OrgTreeFormatter(output, ConfigParser(), None)
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
    output = StringIO()
    f = OrgTreeFormatter(output, ConfigParser(), None)
    text = f.format_event(e)
    expected = '** This is a note\n   <2009-11-26 Thu 09:05>--<2009-12-26 Sat 13:25>\n'
    print repr(expected)
    print repr(text)
    assert text == expected, text
    return

def test_format_with_calendar_tags():
    c = vobject.iCalendar()
    e = c.add('vevent')
    e.add('summary').value = "This is a note"
    start = e.add('dtstart')
    start.value = datetime.datetime(2009, 11, 6, tzinfo = tz.local)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 11, 6, tzinfo = tz.local)
    output = StringIO()
    config = ConfigParser()
    config.add_section('Title')
    config.set('Title', 'tags', ':tag_value:')
    f = OrgTreeFormatter(output, config, None)
    class FauxCalendar(object):
        title = 'Title'
    f.start_calendar(FauxCalendar())
    f.add_event(e)
    text = output.getvalue()
    assert text == '# -*- coding: utf-8 -*-\n* Title\t:tag_value:\n  :CATEGORY: Title\n** This is a note\n   <2009-11-06 Fri 00:00-00:00>\n', text
    return

def test_format_with_calendar_tags_no_colons():
    c = vobject.iCalendar()
    e = c.add('vevent')
    e.add('summary').value = "This is a note"
    start = e.add('dtstart')
    start.value = datetime.datetime(2009, 11, 6, tzinfo = tz.local)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 11, 6, tzinfo = tz.local)
    output = StringIO()
    config = ConfigParser()
    config.add_section('Title')
    config.set('Title', 'tags', 'tag_value')
    f = OrgTreeFormatter(output, config, None)
    class FauxCalendar(object):
        title = 'Title'
    f.start_calendar(FauxCalendar())
    f.add_event(e)
    text = output.getvalue()
    assert text == '# -*- coding: utf-8 -*-\n* Title\t:tag_value:\n  :CATEGORY: Title\n** This is a note\n   <2009-11-06 Fri 00:00-00:00>\n', text
    return

def test_format_with_category():
    c = vobject.iCalendar()
    e = c.add('vevent')
    e.add('summary').value = "This is a note"
    start = e.add('dtstart')
    start.value = datetime.datetime(2009, 11, 6, tzinfo = tz.local)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 11, 6, tzinfo = tz.local)
    output = StringIO()
    config = ConfigParser()
    config.add_section('Title')
    config.set('Title', 'category', 'the_cat')
    f = OrgTreeFormatter(output, config, None)
    class FauxCalendar(object):
        title = 'Title'
    f.start_calendar(FauxCalendar())
    f.add_event(e)
    text = output.getvalue()
    assert text == '# -*- coding: utf-8 -*-\n* Title\n  :CATEGORY: the_cat\n** This is a note\n   <2009-11-06 Fri 00:00-00:00>\n', text
    return

def test_format_unicode():
    c = vobject.iCalendar()
    e = c.add('vevent')
    e.add('summary').value = "Unicode event"
    start = e.add('dtstart')
    start.value = datetime.datetime(2009, 11, 6, tzinfo = tz.local)
    end = e.add('dtend')
    end.value = datetime.datetime(2009, 11, 6, tzinfo = tz.local)
    e.add('description').value = u'This is the description. It has “unicode quotes.”'
    output = StringIO()
    config = ConfigParser()
    f = OrgTreeFormatter(output, config, None)
    class FauxCalendar(object):
        title = 'Title'
    f.start_calendar(FauxCalendar())
    text = f.format_event(e)
    assert text == u'** Unicode event\n   <2009-11-06 Fri 00:00-00:00>\n   - This is the description. It has “unicode quotes.”\n', text
    return
