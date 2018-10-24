import os


class _ConfigCMS(object):
    request_timeout = 10.0
    _host = "127.0.0.1"
    _port = 7777

    @property
    def host(self):
        host = os.environ.get("CMS_HOST")
        return host if host is not None else self._host

    @property
    def port(self):
        port = os.environ.get("CMS_PORT")
        return port if port is not None else self._port


class _ConfigResource(object):
    request_timeout = 10.0
    _host = "127.0.0.1"
    _port = 8888

    @property
    def host(self):
        host = os.environ.get("RESOURCE_HOST")
        return host if host is not None else self._host

    @property
    def port(self):
        port = os.environ.get("RESOURCE_PORT")
        return port if port is not None else self._port


class _ConfigNLU(object):
    request_timeout = 10.0
    _host = "127.0.0.1"
    _port = 8888

    @property
    def host(self):
        host = os.environ.get("NLU_HOST")
        return host if host is not None else self._host

    @property
    def port(self):
        port = os.environ.get("NLU_PORT")
        return port if port is not None else self._port


class _ConfigDM(object):
    input_timeout = 10.0
    _host = "127.0.0.1"
    _port = 5000

    @property
    def host(self):
        host = os.environ.get("DM_HOST")
        return host if host is not None else self._host

    @property
    def port(self):
        port = os.environ.get("DM_PORT")
        return port if port is not None else self._port


ConfigNLU = _ConfigNLU()
ConfigCMS = _ConfigCMS()
ConfigResource = _ConfigResource()
ConfigDM = _ConfigDM()
