#!/usr/bin/env python
# encoding: utf-8

import time

from multiprocessing import Process
from evashare.rmq import Receiver, Publisher

amqp_url = 'amqp://chi1st.xyz:5672?connection_attempts=3&heartbeat_interval=3600'
exchange_type = 'x-delayed-message'
exchange = 'delay_test'
arguments = {"x-delayed-type": "fanout"}
delay_time = 5000
binding_key = 't'


def consumer_callback(unused_channel, basic_deliver, properties,
                      body):
    send_time = time.strptime(body, '%Y-%m-%d %H:%M:%S')
    receive_time = time.localtime()
    assert receive_time.tm_sec - send_time.tm_sec == delay_time / 1000


def send_message():
    publisher = Publisher(amqp_url=amqp_url, exchange=exchange,
                          exchange_type=exchange_type,
                          arguments=arguments)
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    publisher.publish_message(date, binding_key,
                              delay_time=delay_time)
    publisher.stop()


def receive_message():
    receiver = Receiver(consumer_callback, amqp_url,
                        exchange,
                        binding_keys=[binding_key],
                        queue_durable=True, queue_exclusive=False)
    receiver.run()


if __name__ == '__main__':
    p1 = Process(target=send_message)
    p1.start()
    p2 = Process(target=receive_message)
    p2.start()
    time.sleep(8)
    p2.terminate()
    p2.join()
