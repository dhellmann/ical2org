# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann.  All rights reserved.
#
"""Diary file formatter
"""

def format_for_diary(event, calendar_title=None):
    """Format a diary file entry for the event within the calendar
    """
    if event.dtstart.value.date() == event.dtend.value.date():
        # MM/DD/YY HH:MM-HH:MM summary (calendar title)
        start = event.dtstart.value.strftime('%m/%d/%y %H:%M')
        end = event.dtend.value.strftime('%H:%M')
        response = '%s-%s %s' % (start, end, event.summary.value)
    else:
        # %%(diary-block MM DD YYYY MM DD YYYY) summary (calendar title)
        start = event.dtstart.value.strftime('%m %d %Y')
        end = event.dtend.value.strftime('%m %d %Y')
        response = '%%%%(diary-block %s %s) %s' % (start, end, event.summary.value)
    if calendar_title:
        response = '%s (%s)' % (response, calendar_title)
    return response

