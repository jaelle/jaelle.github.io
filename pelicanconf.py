#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jaelle'
SITENAME = 'JLCreations'
SITEURL = ''
SITESUBTITLE = 'Jaelle Scheuerman'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
MARKUP = ('md', 'ipynb')
STATIC_PATHS = ['pdfs']

MENUITEMS = [
    ('Resume','http://cs.tulane.edu/jaelle/JaelleScheuermanCV.pdf')
]

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']

LOAD_CONTENT_CACHE = False
THEME = "themes/crowsfoot"
GITHUB_ADDRESS = "http://www.github.com/jaelle"
TWITTER_ADDRESS = "http://www.twitter.com/jaelle"
PROFILE_IMAGE_URL = "theme/images/logo.png"
SHOW_ARTICLE_AUTHOR = False
