# coding=utf-8
import json
import requests
from vikicommon.config import ConfigCMS


class CMSGate(object):
    """"""
    request_timeout = 10

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def get_dm_biztree(self, domain_id):
        """ Call CMS module for tree.

        """
        url = "http://{0}:{1}/v2/{2}/dm".format(self.host,
                                                self.port,
                                                domain_id)
        data = requests.get(url, timeout=self.request_timeout)
        assert(data.status_code == 200)
        return json.loads(data.text)

    def event_id_to_answer(self, domain_id, event_id):
        """

        Parameters
        ----------
        domain_id : 项目ID
        event_id : 事件ID

        """
        params = {
            'domain_id': domain_id,
            'event_id': event_id
        }
        headers = {'content-type': 'application/json'}
        url = "http://{0}:{1}/v2/event_id_to_answer".format(self.host,
                                                            self.port)
        data = requests.post(url,
                             data=json.dumps(params),
                             headers=headers,
                             timeout=self.request_timeout)
        assert(data.status_code == 200)
        return json.loads(data.text)

    def get_domain_by_name(self, name):
        """ Call CMS module for domain id.

        """
        params = {
            'name': name,
        }
        url = "http://{0}:{1}/v2/rpc/get_domain_by_name".format(self.host,
                                                                self.port)
        headers = {'content-type': 'application/json'}
        data = requests.post(url,
                             data=json.dumps(params),
                             headers=headers,
                             timeout=self.request_timeout)
        assert(data.status_code == 200)
        return json.loads(data.text)

    def get_filter_words(self, domain_id):
        url = "http://{0}:{1}/v2/{2}/filter_words".format(
            self.host, self.port, domain_id)
        data = requests.get(url, timeout=self.request_timeout)
        assert(data.status_code == 200)
        return json.loads(data.text)

    def get_domain_slots(self, domain_id):
        url = "http://{0}:{1}/v2/rpc/get_domain_slots".format(
            self.host, self.port)
        headers = {'content-type': 'application/json'}
        data = requests.post(url,
                             data=json.dumps({
                                 'domain_id': domain_id
                             }),
                             headers=headers,
                             timeout=self.request_timeout)
        assert(data.status_code == 200)
        return json.loads(data.text)

    def get_slot_values_for_nlu(self, slot_id):
        url = "http://{0}:{1}/v2/rpc/get_slot_values_for_nlu".format(
            self.host, self.port)
        headers = {'content-type': 'application/json'}
        data = requests.post(url,
                             data=json.dumps({
                                 'slot_id': slot_id
                             }),
                             headers=headers,
                             timeout=self.request_timeout)
        assert(data.status_code == 200)
        return json.loads(data.text)

    def get_tree_label_data(self, domain_id):
        url = "http://{0}:{1}/v2/rpc/get_tree_label_data".format(
            self.host, self.port)
        headers = {'content-type': 'application/json'}
        data = requests.post(url,
                             data=json.dumps({
                                 'domain_id': domain_id
                             }),
                             headers=headers,
                             timeout=self.request_timeout)
        assert(data.status_code == 200)
        return json.loads(data.text)

    def get_intent_slots_without_value(self, domain_id, intent_name):
        url = "http://{0}:{1}/v2/rpc/get_intent_slots_without_value".format(
            self.host, self.port)
        headers = {'content-type': 'application/json'}
        data = requests.post(url,
                             data=json.dumps({
                                 'domain_id': domain_id,
                                 'intent_name': intent_name
                             }),
                             headers=headers,
                             timeout=self.request_timeout)
        assert(data.status_code == 200)
        return json.loads(data.text)

    def get_domain_values(self, domain_id):
        url = "http://{0}:{1}/v2/domains/{2}/values".format(
            self.host, self.port, domain_id)
        data = requests.get(url, timeout=self.request_timeout)
        assert(data.status_code == 200)
        return json.loads(data.text)

    def train_notify(self, data):
        url = "http://{0}:{1}/v2/rpc/robot/train_notify".format(
            self.host, self.port)
        headers = {'content-type': 'application/json'}
        ret = requests.post(url,
                            data=json.dumps(data),
                            headers=headers,
                            timeout=self.request_timeout)
        assert(ret.status_code == 200)
        return json.loads(ret.text)


cms_gate = CMSGate(ConfigCMS.host, ConfigCMS.port)
