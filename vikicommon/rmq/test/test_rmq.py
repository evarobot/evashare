import time

from multiprocessing import Process
from vikicommon.rmq import Receiver, Publisher


class TestRMQ(object):
    amqp_url = 'amqp://chi1st.xyz:5672?connection_attempts=3&heartbeat_interval=3600'
    exchange_type = 'x-delayed-message'
    exchange = 'delay_test'
    arguments = {"x-delayed-type": "fanout"}
    delay_time = 5000
    binding_key = 't'

    def consumer_callback(self, unused_channel, basic_deliver, properties,
                          body):
        send_time = time.strptime(body, '%Y-%m-%d %H:%M:%S')
        receive_time = time.localtime()
        assert receive_time.tm_sec - send_time.tm_sec == self.delay_time / 1000

    def send_message(self):
        publisher = Publisher(amqp_url=self.amqp_url, exchange=self.exchange,
                              exchange_type=self.exchange_type,
                              arguments=self.arguments)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        publisher.publish_message(date, self.binding_key,
                                  delay_time=self.delay_time)
        publisher.stop()

    def receive_message(self):
        receiver = Receiver(self.consumer_callback, self.amqp_url,
                            self.exchange,
                            binding_keys=[self.binding_key],
                            queue_durable=True, queue_exclusive=False)
        receiver.run()

    @classmethod
    def test_send_message(self):
        p1 = Process(target=self.send_message)
        p1.start()
        p2 = Process(target=self.receive_message)
        p2.start()
        time.sleep(8)
        p2.terminate()
        p2.join()


TestRMQ.test_send_message()
