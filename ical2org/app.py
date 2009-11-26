# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann.  All rights reserved.
#
"""Command line interface for ical2org.
"""

import logging
import optparse
import sys

VERBOSE_LEVELS = {
    0:logging.WARNING,
    1:logging.INFO,
    2:logging.DEBUG,
    }

def main(args=sys.argv[1:]):
    option_parser = optparse.OptionParser(
        usage='usage: ical2org [options] [calendar files]',
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
                             
    options, args = option_parser.parse_args(args)

    logging.basicConfig(level=VERBOSE_LEVELS.get(options.verbose_level, logging.WARNING),
                        format='%(message)s',
                        )
    logging.info('Starting %d days ago', options.days_ago)
    logging.info('Ending %d days from now', options.days_ahead)

    if options.output_file_name:
        logging.info('Writing to %s', options.output_file_name)
    return
                        
    
    
if __name__ == '__main__':
    main()
