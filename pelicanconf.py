#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
THEME = "medius"
AUTHOR = u'trexor'
SITENAME = u'tech babbles'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'
DISQUS_SITENAME = "techbabble"
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False
MEDIUS_AUTHORS = {
    'Reese': {
        'description': """
            I enjoy blogging about technology and tinkering with various things.
        """,
        'cover': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Milky_Way_Arch.jpg/1920px-Milky_Way_Arch.jpg',
        'image': 'https://lh6.googleusercontent.com/-zEMaXmWAhdI/AAAAAAAAAAI/AAAAAAAAAAA/eVdgsm3TIDU/s128-c-k/photo.jpg',
        'links': (('github', 'https://github.com/bank2600'),
                  ('twitter-square', 'https://twitter.com/rtfmjohnson')),
    }
}
MEDIUS_CATEGORIES = {
    'Labs': {
        'description': 'A galaxy is a gravitationally bound system of stars, stellar remnants, interstellar gas and dust, and dark matter.',
        'logo': 'https://www.seas.harvard.edu/sites/default/files/images/Teaching%20Labs/MD%20B%20EE.jpg',
        'thumbnail': 'http://s3.evcdn.com/images/block/I0-001/032/153/298-4.png_/open-level-computer-lab-98.png'
    }
}
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
