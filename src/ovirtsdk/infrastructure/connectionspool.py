#
# Copyright (c) 2010 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#           http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from Queue import Queue
import thread
from ovirtsdk.web.connection import Connection

class ConnectionsPool(object):
    '''
    ConnectionsManager used to manage pool of web connections
    '''
    def __init__(self, url, port, key_file, cert_file, strict, timeout, username, password, count=20):

        self.__free_connetcions = Queue(0)
        self.__busy_connetcions = {}

        self.__plock = thread.allocate_lock()
        self.__rlock = thread.allocate_lock()

        self.__url = url

        for _ in range(count):
            self.__free_connetcions.put(item=Connection(url=url, \
                                                        port=port, \
                                                        key_file=key_file, \
                                                        cert_file=cert_file, \
                                                        strict=strict, \
                                                        timeout=timeout, \
                                                        username=username, \
                                                        password=password,
                                                        manager=self))
    def getConnection(self, get_ttl=100):
#        try:
            with self.__plock:
                conn = self.__free_connetcions.get(block=True, timeout=get_ttl)
                self.__busy_connetcions[conn.get_id()] = conn
                return conn
#        except Empty, e:
#                self.__extendQueue()
#                return self.getConnection(get_ttl)

#    def __extendQueue(self):
#TODO: add more connections if needed
#        continue

    def _freeResource(self, conn):
        with self.__rlock:
            conn = self.__busy_connetcions.pop(conn.get_id())
            self.__free_connetcions.put_nowait(conn)

    def get_url(self):
        return self.__url
