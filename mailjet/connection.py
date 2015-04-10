import urllib
import requests
from mailjet.conf import settings


class Connection(object):
    def __init__(self, access_key=None, secret_key=None, timeout=None):
        self.access_key = access_key or settings.API_KEY
        self.secret_key = secret_key or settings.SECRET_KEY
        self.timeout = timeout or settings.TIMEOUT
        self.connection = requests.Session()
        self.connection.auth = (self.access_key, self.secret_key)

    def open(self, function, method, options=None, postdata=None):
        url = u'%s%s' % (settings.URL, function)
        default_options = dict()
        if options:
            default_options.update(options)
            url += '?' + urllib.urlencode(default_options)

        if postdata:
            poststring = urllib.urlencode(postdata.items())
        else:
            poststring = None

        if method == 'post':
            response = self.connection.post(url, data=postdata)
        else:
            response = self.connection.get(url)

        return response

    @classmethod
    def get_connection(cls, access_key, secret_key):
        return Connection(access_key, secret_key)
