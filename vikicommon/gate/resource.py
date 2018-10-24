# coding=utf-8

import json
import requests
from vikicommon.config import Config
from vikicommon.util.util import generate_base_url


class ResourceGate(object):

    def __init__(self, host, port, sidecar_url):
        self.base_url = generate_base_url(host, port,
                                          sidecar_url, "sidecar-resource")

    def get_slots(self, domain_name, version, timeout=Config.http_timeout):
        params = {
            'project': domain_name,
            'version': version
        }
        headers = {'content-type': 'application/json'}
        url = self.base_url + '/v2/nlu/{}/predict'.format(domain_name)
        data = requests.post(url,
                             data=json.dumps(params),
                             headers=headers,
                             timeout=timeout)
        assert(data.status_code == 200)
        return json.loads(data.text)
