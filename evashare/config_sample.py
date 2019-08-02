import os


class _Config(object):
    http_timeout = 5

    _sidecar_url = ""

    @property
    def sidecar_url(self):
        url = os.environ.get("SIDECAR_URL")
        return url if url else self._sidecar_url


class _ConfigCMS(object):
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
Config = _Config()
