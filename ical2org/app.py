# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann.  All rights reserved.
#
"""Command line interface for ical2org.
"""

import datetime
import logging
import optparse
import os
import sys

from ical2org import calendars, filter, diary
import vobject

utc = vobject.icalendar.utc

VERBOSE_LEVELS = {
    0:logging.WARNING,
    1:logging.INFO,
    2:logging.DEBUG,
    }

def main(args=sys.argv[1:]):
    option_parser = optparse.OptionParser(
        usage='usage: ical2org [options] [calendar titles]',
        conflict_handler='resolve',
        description='Convert iCal calendar entries to org-mode data for use with emacs',
        )
    option_parser.add_option('--begin', '-b', '--days-ago',
                             action='store',
                             dest='days_ago',
                             help='Number of days back in time to search. Defaults to 14.',
                             default=14,
                             type=int,
                             )
    option_parser.add_option('--end', '-e', '--days-ahead',
                             action='store',
                             dest='days_ahead',
                             help='Number of days forward in time to search. Defaults to 30.',
                             default=30,
                             type=int,
                             )
    option_parser.add_option('-v', '--verbose',
                             action='count',
                             dest='verbose_level',
                             default=0,
                             help='Increase verbose level',
                             )
    option_parser.add_option('--output-file', '-o',
                             action='store',
                             dest='output_file_name',
                             help='Write the output to the named file instead of stdout',
                             default=None,
                             )
    option_parser.add_option('--all',
                             action='store_false',
                             dest='active_only',
                             default=True,
                             help='Include all calendars, not just active.',
                             )
    option_parser.add_option('--input-directory',
                             action='store',
                             dest='input_directory',
                             default=os.path.expanduser('~/Library/Calendars'),
                             help='Directory containing calendars. Defaults to ~/Library/Calendars.',
                             )
                             
    options, calendar_titles = option_parser.parse_args(args)

    log_level = VERBOSE_LEVELS.get(options.verbose_level, logging.DEBUG)
    logging.basicConfig(level=log_level, format='%(message)s')

    start_date = datetime.datetime.combine(
        datetime.date.today() - datetime.timedelta(options.days_ago),
        datetime.time.min,
        )#.replace(tzinfo=utc)
    end_date = datetime.datetime.combine(
        datetime.date.today() + datetime.timedelta(options.days_ahead),
        datetime.time.max,
        )#.replace(tzinfo=utc)
    logging.info('Starting %d days ago at %s', options.days_ago, start_date)
    logging.info('Ending %d days from now at %s', options.days_ahead, end_date)

    if options.output_file_name:
        logging.info('Writing to %s', options.output_file_name)

    if calendar_titles:
        calendar_generator = calendars.get_by_titles(path=options.input_directory,
                                                     titles=calendar_titles)
    else:
        calendar_generator = calendars.discover(path=options.input_directory,
                                                active_only=options.active_only)

    for calendar in calendar_generator:
        logging.info('Processing: %s', calendar.title)
        for event in filter.unique(filter.by_date_range(calendar.get_events(),
                                                        start_date,
                                                        end_date,
                                                        )):
            logging.info('  %s', event.summary.value)
            print diary.format_for_diary(event, calendar.title)
    return
    
    
if __name__ == '__main__':
    main()
