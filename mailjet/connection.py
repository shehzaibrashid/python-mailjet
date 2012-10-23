import urllib
import urllib2
import base64
import httplib
from mailjet.conf import settings

class Connection(object):
    def __init__(self, access_key=None, secret_key=None, timeout=None):
        self.access_key = access_key or settings.API_KEY
        self.secret_key = secret_key or settings.SECRET_KEY
        self.timeout = timeout or settings.TIMEOUT

    def open(self, method, function, options=None, postdata=None):
        url = u'%s%s%s' % (settings.URL, method, function)
        default_options = {
            'output': 'json',
        }
        if options:
            default_options.update(options)

        url += '?' + urllib.urlencode(default_options)
        if postdata:
            poststring = urllib.urlencode(postdata.items())
        else:
            poststring = None

    	request = urllib2.Request(url)
        base64string = base64.encodestring('%s:%s' % (self.access_key, self.secret_key)).replace('\n', '')
        request.add_header("Authorization", "Basic %s" % base64string)   
        r = urllib2.urlopen(request)

        return r

    @classmethod
    def get_connection(cls, access_key, secret_key):
        return Connection(access_key, secret_key)
  
