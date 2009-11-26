#!python

import glob
import os

import vobject

caldirname = '/Users/dhellmann/Library/Calendars/CC9C5E16-4395-4E3F-9982-18100D1C0EA8.caldav/9C32DEF4-5421-4142-8429-3D88BD183B92.calendar'
calfilenames = glob.glob(os.path.join(caldirname, 'Events', '*.ics'))

for calfilename in calfilenames:
    with open(calfilename, 'rt') as icalstream:
        for component in vobject.readComponents(icalstream):
            # .next().vevent.dtstart.value
            for event in component.vevent_list:
                event.prettyPrint()
                break
    break
