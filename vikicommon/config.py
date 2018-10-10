import os


class _ConfigCMS(object):
    request_timeout = 10.0
    _host = "127.0.0.1"
    _port = 8888
    _base_url = ''

    @property
    def host(self):
        host = os.environ.get("CMS_HOST")
        return host if host is not None else self._host

    @property
    def port(self):
        port = os.environ.get("CMS_PORT")
        return port if port is not None else self._port

    @property
    def base_url(self):
        url = os.environ.get("CMS_URL")
        return url if url is not None else self._base_url


class _ConfigNLU(object):
    request_timeout = 10.0
    _host = "127.0.0.1"
    _port = 5000
    _base_url = ''

    @property
    def host(self):
        host = os.environ.get("NLU_HOST")
        return host if host is not None else self._host

    @property
    def port(self):
        port = os.environ.get("NLU_PORT")
        return port if port is not None else self._port

    @property
    def base_url(self):
        url = os.environ.get("NLU_URL")
        return url if url is not None else self._base_url


class _ConfigDM(object):
    input_timeout = 10.0
    _host = "127.0.0.1"
    _port = 9999
    _base_url = ''

    @property
    def host(self):
        host = os.environ.get("DM_HOST")
        return host if host is not None else self._host

    @property
    def port(self):
        port = os.environ.get("DM_PORT")
        return port if port is not None else self._port

    @property
    def base_url(self):
        url = os.environ.get("DM_URL")
        return url if url is not None else self._base_url


ConfigNLU = _ConfigNLU()
ConfigCMS = _ConfigCMS()
ConfigDM = _ConfigDM()
