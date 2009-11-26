#!python

from glob import glob
import os
import plistlib

import vobject

calendar_root = '/Users/dhellmann/Library/Calendars/'
#CC9C5E16-4395-4E3F-9982-18100D1C0EA8.caldav/9C32DEF4-5421-4142-8429-3D88BD183B92.calendar'

calendar_directories = (
    glob(os.path.join(calendar_root, '*.caldav', '*.calendar')) +
    glob(os.path.join(calendar_root, '*.calendar'))
    )

for dirname in calendar_directories:
    info_filename = os.path.join(dirname, 'Info.plist')
    if os.path.isfile(info_filename):
        info = plistlib.readPlist(info_filename)
        if info.get('Checked'):
            print info['Title']

#             for event_filename in glob(os.path.join(dirname, 'Events', '*.ics')):
#                 with open(event_filename, 'rt') as icalstream:
#                     for component in vobject.readComponents(icalstream):
#                         for event in component.vevent_list:
#                             event.prettyPrint()
#                     break
                    
