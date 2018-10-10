# encoding=utf-8
import json
import requests
from vikicommon.config import ConfigDM


class DMGate(object):
    """"""
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def process_question(self, data, timeout=3):
        url = 'http://{0}:{1}/dm/robot/question/'.format(self.host, self.port)
        headers = {'content-type': 'application/json'}
        ret = requests.post(url, data=json.dumps(data), headers=headers,
                            timeout=timeout)
        assert(ret.status_code == 200)
        return ret.text

    def reset_robot(self, data, timeout=3):
        url = 'http://{0}:{1}/dm/robot/reset/'.format(self.host, self.port)
        headers = {'content-type': 'application/json'}
        ret = requests.post(url, data=json.dumps(data), headers=headers,
                            timeout=timeout)
        assert(ret.status_code == 200)
        return ret.text

    def confirm(self, data, timeout=3):
        url = 'http://{0}:{1}/dm/robot/confirm/'.format(self.host, self.port)
        headers = {'content-type': 'application/json'}
        ret = requests.post(url, data=json.dumps(data), headers=headers,
                            timeout=timeout)
        assert(ret.status_code == 200)
        return ret.text


dm_gate = DMGate(ConfigDM.host, ConfigDM.port)
