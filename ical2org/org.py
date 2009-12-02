#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann.  All rights reserved.
#
"""
"""

from ical2org import format, tz

class OrgTreeFormatter(format.CalendarFormatter):
    """Formats output as an org outline.
    """
    
    def start_calendar(self, calendar):
        """Begin a calendar node.
        
        Arguments:
        - `self`:
        - `calendar`:
        """
        self.active_calendar = calendar
        self.output.write('* %s\n' % calendar.title)
        return

    def format_event(self, event):
        event_start = event.dtstart.value.astimezone(tz.local)
        event_end = event.dtend.value.astimezone(tz.local)
        if event_start.date() == event_end.date():
            time_range = '<%s-%s>' % (event_start.strftime('%Y-%m-%d %a %H:%M'),
                                      event_end.strftime('%H:%M'))
        else:
            time_range = '<%s>--<%s>' % (event_start.strftime('%Y-%m-%d %a %H:%M'),
                                         event_end.strftime('%Y-%m-%d %a %H:%M'))
        
        lines = ['** %s %s' % (event.summary.value, time_range) ]
        if getattr(event, 'location', None):
            lines.append('   - Location: %s' % event.location.value)
# FIXME - Unicode errors from some events
#         if getattr(event, 'description', None):
#             lines.extend([ '   %s' % l
#                            for l in event.description.value.splitlines()
#                            ])

        lines.append('')
        return '\n'.join(lines)
    



        

