# Copyright 2024 Bloomberg Finance L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import pika
import os

class mqProducerInterface:
    def __init__(self, routing_key: str, exchange_name: str) -> None:
        # Save parameters to class variables
        self.routine_key = routine_key
        self.exchange_name = exchange_name
        # Call setupRMQConnection
        setupRMQConnection()
        

    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        connection = pika.BlockingConnection(parameters=con_params)
        # Establish Channel
        channel = connection.channel()
        # Create the exchange if not already present
        exchange = channel.exchange_declare(exchange = "Exchange Name")
        

    def publishOrder(self, message: str) -> None:
        # Basic Publish to Exchange
        channel.basic_pulish(
            exhange = "Exchange Name",
            routing_key = "Routing Key",
            body = "Message",
        )
        # Close Channel
        channel.close()
        # Close Connection
        connection.close()
        