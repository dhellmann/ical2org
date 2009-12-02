#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann.  All rights reserved.
#
"""
"""

class CalendarFormatter(object):
    """Base class for formatters.
    """
    
    def __init__(self, output):
        """Initialize
        
        Arguments:
        - `output`: 
        """
        self.output = output
        return

    def close(self):
        """Finalize the output, if necessary.
        """
        return

    def start_calendar(self, calendar):
        """Begin processing a calendar.
        
        Arguments:
        - `calendar`: The ical2org.calendars.Calendar instance.
        """
        return

    def end_calendar(self, calendar):
        """Finish processing a calendar.
        
        Arguments:
        - `calendar`: The ical2org.calendars.Calendar instance.
        """
        return

    def add_event(self, event):
        """The event falls passes the filter rules and should be added
        to the output.
        
        Arguments:
        - `event`: A vobject.icalendar component.
        """
        self.output.write(self.format_event(event))
        return

    def format_event(self, event):
        """Return an appropriate string representation of the event.
        
        Arguments:
        - `event`: A vobject.icalendar component.
        """
        return
