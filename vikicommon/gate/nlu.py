# coding=utf-8

import json
import requests
from vikicommon.config import ConfigNLU


class NLUGate(object):
    request_timeout = 5

    def __init__(self, host, port):
        self.host = host
        self.port = port

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
        url = "http://{0}:{1}/v2/nlu/{2}/predict".format(self.host,
                                                         self.port,
                                                         domain_id)
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
        url = "http://{0}:{1}/v2/nlu/{2}/train".format(self.host,
                                                       self.port,
                                                       domain_id)
        data = requests.post(url,
                             data=json.dumps(params),
                             headers=headers,
                             timeout=ConfigNLU.request_timeout)
        assert(data.status_code == 200)
        return json.loads(data.text)


nlu_gate = NLUGate(ConfigNLU.host, ConfigNLU.port)
