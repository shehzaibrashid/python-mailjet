from mailjet.connection import Connection


class Api(object):
    def __init__(self, connection=None, access_key=None, secret_key=None):
        if connection is None:
            connection = Connection.get_connection(access_key, secret_key)

        self.connection = connection

    def __getattr__(self, function):
        return ApiFunction(self, function)


class ApiFunction(object):
    def __init__(self, api, function):
        self.api = api
        self.function = function

    def __getattr__(self, method):
        return ApiFunctionMethod(self, method)

    def __unicode__(self):
        return self.function

    def __str__(self):
        return self.function


class ApiFunctionMethod(object):
    def __init__(self, function, method):
        self.function = function
        self.method = method

    def __call__(self, **kwargs):
        if self.method == 'post':
            postdata = kwargs
            options = None
        else:
            options = kwargs
            postdata = None

        response = self.function.api.connection.open(
            self.function,
            self.method,
            options=options,
            postdata=postdata,
        )

        try:
            obj = response.json()
        except ValueError:
            return None
        return obj

    def __unicode__(self):
        return self.method

    def __str__(self):
        return self.method

