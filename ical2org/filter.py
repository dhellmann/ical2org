#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann.  All rights reserved.
#
"""Filter events by a date range.
"""

import datetime
import logging

import vobject

log = logging.getLogger(__name__)
utc = vobject.icalendar.utc

def by_date_range(events, start, end):
    """Iterate over the incoming events and yield those that fall within the date range.
    """
    log.debug('filtering between %s and %s', start, end)
    for event in events:

        # Fix time zones in date objects
        if not isinstance(event.dtstart.value, datetime.datetime):
            event_start = datetime.datetime.combine(event.dtstart.value,
                                                    datetime.time.min,
                                                    )
            event_end = datetime.datetime.combine(event.dtend.value,
                                                  datetime.time.max,
                                                  )
        else:
            event_start = event.dtstart.value
            event_end = event.dtend.value

        if not event_start.tzinfo:
            event_start = event_start.replace(tzinfo=utc)
        if not event_end.tzinfo:
            event_end = event_end.replace(tzinfo=utc)

        # Replace the dates in case we updated the timezone
        event.dtstart.value = event_start
        event.dtend.value = event_end
        
        event_rrule = getattr(event, 'rrule', None)
        log.debug('checking %s - %s == %s', 
                  event.dtstart.value, event.dtend.value,
                  event.summary.value,
                  )
        try:
            if event_rrule is not None:
                duration = event.dtend.value - event.dtstart.value
                log.debug('  duration %s', duration)
                for recurrance in event.rruleset.between(start, end, inc=True):
                    log.debug('  recurrance %s %s', recurrance, type(recurrance))
                    dupe = event.__class__.duplicate(event)
                    dupe.dtstart.value = recurrance.replace(tzinfo=utc)
                    dupe.dtend.value = (recurrance + duration).replace(tzinfo=utc)
                    yield dupe
            elif event_start >= start and event_end <= end:
                yield event
        except TypeError:
            event.prettyPrint()
            raise
        
    
