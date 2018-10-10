# coding=utf-8

import json
import requests
from vikicommon.config import ConfigNLU
from vikicommon.util.util import generate_base_url


class NLUGate(object):
    request_timeout = 5

    def __init__(self, host, port, url):
        self.base_url = generate_base_url(host, port, url)

    def predict(self, domain_id, context, question):
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
        url = self.base_url + '/v2/nlu/{}/predict'.format(domain_id)
        data = requests.post(url,
                             data=json.dumps(params),
                             headers=headers,
                             timeout=ConfigNLU.request_timeout)
        assert(data.status_code == 200)
        return json.loads(data.text)

    def train(self, domain_id, domain_name):
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
                             timeout=ConfigNLU.request_timeout)
        assert(data.status_code == 200)
        return json.loads(data.text)


nlu_gate = NLUGate(ConfigNLU.host, ConfigNLU.port, ConfigNLU.base_url)
