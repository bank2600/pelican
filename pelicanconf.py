#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
THEME = "medius"
AUTHOR = u'Reese'
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
    'ARM': {
        'description': 'mini me',
        'logo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/ARM_logo.svg/2000px-ARM_logo.svg.png',
        'thumbnail': 'https://www.arm.com/assets/images/ARM_Logo_Corporate_Blue.png'
    }

    'Labs': {
        'description': 'Learning @ ~/',
        'logo': 'https://www.seas.harvard.edu/sites/default/files/images/Teaching%20Labs/MD%20B%20EE.jpg',
        'thumbnail': 'http://s3.evcdn.com/images/block/I0-001/032/153/298-4.png_/open-level-computer-lab-98.png'
    }
    'Life': {
        'description': 'Learning @ ~/',
        'logo': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/LIFE_magazine_logo.svg/1200px-LIFE_magazine_logo.svg.png',
        'thumbnail': 'https://www.timeinc.com/wp-content/uploads/2014/03/life_logo.svg'
    }

}
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
