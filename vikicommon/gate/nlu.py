# coding=utf-8

import json
import requests
from vikicommon.config import ConfigNLU, Config
from vikicommon.util.util import generate_base_url

http_timeout = Config.http_timeout


class NLUGate(object):

    def __init__(self, host, port, sidecar_url):
        self.base_url = generate_base_url(host, port,
                                          sidecar_url, "sidecar-vikinlu")

    def predict(self, domain_id, context, question, timeout=http_timeout):
        """

        Parameters
        ----------
        domain_id : TODO
        context : TODO
        question : TODO

        Returns
        -------
        TODO

        """
        params = {
            'context': context,
            'question': question
        }
        headers = {'content-type': 'application/json'}
        url = self.base_url + '/v2/nlu/{0}/predict'.format(domain_id)
        data = requests.post(url,
                             data=json.dumps(params),
                             headers=headers,
                             timeout=timeout)
        assert(data.status_code == 200)
        return json.loads(data.text)

    def train(self, domain_id, domain_name, timeout=http_timeout):
        """

        Parameters
        ----------
        domain_id : TODO

        Returns
        -------
        TODO

        """
        params = {
            'project': domain_name,
        }
        headers = {'content-type': 'application/json'}
        url = self.base_url + '/v2/nlu/{}/train'.format(domain_id)
        data = requests.post(url,
                             data=json.dumps(params),
                             headers=headers,
                             timeout=timeout)
        assert(data.status_code == 200)
        return json.loads(data.text)


nlu_gate = NLUGate(ConfigNLU.host, ConfigNLU.port, Config.sidecar_url)
