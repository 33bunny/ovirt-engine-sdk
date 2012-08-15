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

from ovirtsdk.xml import params

class ERROR(Exception):
    def __init__(self, content):
        Exception.__init__(self, content)

class ConnectionError(Exception):
    def __init__(self, expect):
        Exception.__init__(self, '[ERROR]::oVirt API connection failure, %s' % expect)

class NoCertificatesError(Exception):
    def __init__(self):
        Exception.__init__(self, '[ERROR]::key_file, cert_file, ca_file must be specified for SSL connection.')

class RequestError(Exception):
    def __init__(self, response):
        self.detail = None
        self.status = None
        self.reason = None
        res = response.read()
        detail = ''

        if res is not None and str(res) is not '' and str(res).find('Error report') != -1:
            detail = res.lstrip()
        elif res:
            f_detail = params.parseString(res)
            if isinstance(f_detail, params.Action) and f_detail.fault is not None:
                #self.reason = f_detail.fault.reason
                detail = f_detail.fault.detail.lstrip()
            else:
                #self.reason = response.reason
                if f_detail is not None:
                    detail = f_detail.detail.lstrip()

        #engine returns can-do-action error messages with brackets
        if detail.startswith('[') and detail.endswith(']'):
            detail = detail[1:len(detail) - 1]

        #application server error
        if detail.startswith('<html>'):
            start = detail.find('<h1>')
            end = detail.find('</h1>')
            if start != -1 and end != -1:
                detail = detail[start:end].replace('<h1>', '').replace('</h1>', '')
                if detail and detail.endswith(' - '):
                    detail = detail[:len(detail) - 3]

        self.detail = detail
        self.reason = response.reason
        self.status = response.status

        Exception.__init__(self, '[ERROR]::oVirt API request failure.' + self.__str__())

    def __str__(self):
        return '\r\nstatus: ' + str(self.status) + '\r\nreason: ' + self.reason + '\r\ndetail: ' + str(self.detail)

class ImmutableError(Exception):
    def __init__(self, key):
        Exception.__init__(self, '[ERROR]::\'%s\' is immutable.' % key)
