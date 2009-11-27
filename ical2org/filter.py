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
        event_rrule = getattr(event, 'rrule', None)
        log.debug('checking %s - %s == %s', 
                  event.dtstart.value, event.dtend.value,
                  event.summary.value,
                  )
        if event_rrule is not None:
            duration = event.dtend.value - event.dtstart.value
            log.debug('  duration %s', duration)
            for recurrance in event.rruleset.between(start, end, inc=True):
                log.debug('  recurrance %s %s', recurrance, type(recurrance))
                dupe = event.__class__.duplicate(event)
                dupe.dtstart.value = recurrance
                dupe.dtend.value = recurrance + duration
                yield dupe
        else:
            if not isinstance(event.dtstart.value, datetime.datetime):
                event_start = datetime.datetime.combine(event.dtstart.value,
                                                        datetime.time.min,
                                                        tzinfo=utc)
                event_end = datetime.datetime.combine(event.dtend.value,
                                                      datetime.time.max,
                                                      tzinfo=utc)
            else:
                event_start = event.dtstart.value
                event_end = event.dtend.value
            log.debug('event_start = %s', event_start)
            log.debug('event_end = %s', event_end)
            if event_start >= start and event_end <= end:
                yield event

    
