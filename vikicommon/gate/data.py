# coding=utf-8
import json
import requests
import logging

from vikicommon.config import ConfigData
from vikicommon.util.util import generate_base_url

log = logging.getLogger(__name__)


class DataGate(object):
    """"""
    request_timeout = 10

    def __init__(self, host, port, sidecar_url):
        self.base_url = generate_base_url(host, port,
                                          sidecar_url,
                                          "sidecar-vikidm")

    def session_history(self, domain_id, robot_id):
        """ Call DATA module for tree.

        """
        url = self.base_url + '/v2/day_questions'
        payload = {
            "domain_id": domain_id,
            "robot_id": robot_id
        }
        try:
            ret = requests.get(url, params=payload,
                               timeout=0.5)
        except Exception as e:
            log.warning(
                "get session history has an error: {} remote api {}".format(e,
                                                                            url))
            return []
        data = json.loads(ret.text)
        if data['code'] == -1:
            log.warning(
                "get session history has an error: {} remote api {}".format(
                    data['message'], url))
            return []
        return data['data']

    def save_session(self, **params):
        """

        Parameters
        ----------
        domain_id : 项目ID
        question : 问题
        answer : 答案
        answerer: 回答者
        question_datetime: 提问时间
        answer_datetime: 回答时间
        machine_intent: 机器意图
        robot_id: 设备id
        sid: 会话id
        """
        headers = {'content-type': 'application/json'}
        url = self.base_url + '/v2/questions'
        log.info('save session: {}'.format(params))
        try:
            ret = requests.post(url,
                                json=params,
                                headers=headers,
                                timeout=0.5)
        except Exception as e:
            log.warning("save session has an error: {} - api {} ".format(e, url))
            return False
        data = json.loads(ret.text)
        if data['code'] == -1:
            log.warning(
                "save session has an error: {} - api {} ".format(data['message'], url))
            return False
        log.info('save session success')
        return True

    def is_session_complete(self, sid):
        url = self.base_url + '/v2/questions/{}'.format(sid)
        try:
            ret = requests.get(url, timeout=0.5)
        except Exception as e:
            log.warning("remote api {} has an error: {}".format(url, e))
            return False
        return json.loads(ret.text)['data']


data_gate = DataGate(ConfigData.host, ConfigData.port, ConfigData.base_url)
