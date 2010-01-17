#!/usr/bin/env python

from distutils.core import setup

PROJECT = 'ical2org'
VERSION = '1.0'

setup(
    name=PROJECT,
    description='Convert iCal files to emacs org-mode data',
    version=VERSION,

    author = 'Doug Hellmann',
    author_email = 'doug.hellmann@gmail.com',
    url = 'http://www.doughellmann.com/projects/ical2org/',
    download_url = 'http://www.doughellmann.com/downloads/%s-%s.tar.gz' % \
        (PROJECT, VERSION),

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Communications',
        'Topic :: Office/Business',
        'Topic :: Office/Business :: Scheduling',
        ],
    
    packages=['ical2org'],
    )
