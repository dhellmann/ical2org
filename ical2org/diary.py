# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann.  All rights reserved.
#
"""Diary file formatter
"""

import datetime

import vobject

utc = vobject.icalendar.utc

def format_for_diary(event, calendar_title=None):
    """Format a diary file entry for the event within the calendar
    """
    event_start = event.dtstart.value
    event_end = event.dtend.value
    if not isinstance(event_start, datetime.datetime):
        log.debug('rebuilding dates')
        event_start = datetime.datetime.combine(event_start, datetime.time.min)
        event_end = datetime.datetime.combine(event_end, datetime.time.max)
        
    if event_start.date() == event_end.date():
        # MM/DD/YY HH:MM-HH:MM summary (calendar title)
        start = event_start.strftime('%m/%d/%y %H:%M')
        end = event_end.strftime('%H:%M')
        response = '%s-%s %s' % (start, end, event.summary.value)
    else:
        # %%(diary-block MM DD YYYY MM DD YYYY) summary (calendar title)
        start = event_start.strftime('%m %d %Y')
        end = event_end.strftime('%m %d %Y')
        response = '%%%%(diary-block %s %s) %s' % (start, end, event.summary.value)
    if calendar_title:
        response = '%s (%s)' % (response, calendar_title)
    return response

