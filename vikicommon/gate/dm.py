# encoding=utf-8
import json
import requests
from vikicommon.config import ConfigDM, Config
from vikicommon.util.util import generate_base_url


class DMGate(object):
    """"""
    def __init__(self, host, port, sidecar_url):
        self.base_url = generate_base_url(host, port,
                                          sidecar_url,
                                          "sidecar-vikidm")

    def process_question(self, data, timeout=Config.http_timeout):
        url = self.base_url + '/dm/robot/question/'
        headers = {'content-type': 'application/json'}
        ret = requests.post(url, data=json.dumps(data), headers=headers,
                            timeout=timeout)
        assert(ret.status_code == 200)
        return ret.text

    def reset_robot(self, data, timeout=Config.http_timeout):
        url = self.base_url + '/dm/robot/reset/'
        headers = {'content-type': 'application/json'}
        ret = requests.post(url, data=json.dumps(data), headers=headers,
                            timeout=timeout)
        assert(ret.status_code == 200)
        return ret.text

    def confirm(self, data, timeout=Config.http_timeout):
        url = self.base_url + '/dm/robot/confirm/'
        headers = {'content-type': 'application/json'}
        ret = requests.post(url, data=json.dumps(data), headers=headers,
                            timeout=timeout)
        assert(ret.status_code == 200)
        return ret.text


dm_gate = DMGate(ConfigDM.host, ConfigDM.port, Config.sidecar_url)
