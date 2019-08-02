# coding=utf-8

import json
import requests
from evashare.config import Config, ConfigResource
from evashare.util.util import generate_base_url


class ResourceGate(object):

    def __init__(self, host, port, sidecar_url):
        self.base_url = generate_base_url(host, port,
                                          sidecar_url, "sidecar-resource")

    def get_slots(self, domain_name, version, timeout=Config.http_timeout):
        return {
            "ret_code": "0000",
            "ret_msg": "sucess",
            "result": {}
        }
        params = {
            'product': domain_name,
            'version': version
        }
        headers = {'content-type': 'application/json'}
        url = self.base_url + '/resource/nlu/v1/metadata'
        data = requests.post(url,
                             data=json.dumps(params),
                             headers=headers,
                             timeout=timeout)
        assert(data.status_code == 200)
        return json.loads(data.text)


resource_gate = ResourceGate(ConfigResource.host,
                             ConfigResource.port,
                             Config.sidecar_url)
