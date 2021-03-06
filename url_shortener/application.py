from werkzeug.routing import BaseConverter
from jinja2 import Undefined
from urlparse import urlparse
import random

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


DEVICE_TYPES = {
  'desktop': [ 'macos', 'windows', 'linux' ],
  'tablet': [ 'ipad' ],
  'mobile': [ 'iphone', 'android' ]
}

def sanitize_device(criteria):
    if criteria is None or isinstance(criteria, Undefined):
        return 'Default'

    return criteria.replace('device_type:', '').capitalize()


def random_short_url():
    sequence = 'abcdefghijklmnopqrstuvwxyz' + \
               'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + \
               '0123456789'
    url = ''
    for _ in range(6):
         url += random.choice(sequence)
    return url

def valid_url(url):
    if len(url) == 0:
         return False

    try:
        result = urlparse(url)
        if [result.scheme, result.netloc, result.path]:
            return True
        else:
            return False
    except:
        return False
