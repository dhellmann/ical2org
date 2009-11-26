# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann.  All rights reserved.
#
"""Diary file formatter
"""

def format_for_diary(event, calendar_title=None):
    """Format a diary file entry for the event within the calendar
    """
    # MM/DD/YY HH:MM-HH:MM summary (calendar title)
    start = event.dtstart.value.strftime('%m/%d/%y %H:%M')
    end = event.dtend.value.strftime('%H:%M')
    response = '%s-%s %s' % (start, end, event.summary.value)
    if calendar_title:
        response = '%s (%s)' % (response, calendar_title)
    return response

