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

class UnsupportedArgument(Exception):
    def __init__(self, arg):
        Exception.__init__(self, '[ERROR]:: Argument [%s] is NOT supported!' % arg)

class AmbiguousParameterException(Exception):
    def __init__(self, method, param):
        Exception.__init__(self, '[ERROR]:: Parameter [\'-%s\'] at method [\'%s\'] is ambiguous,\nplease specify more specific path to argument or use \'root\' argumentProcessingAlgorithm!' % (param, method))

class ServiceMetadataEndPointLocationFailure(Exception):
    def __init__(self, url):
        Exception.__init__(self, '[ERROR]:: Service metadata endpoint [\'%s\'] cannot be found!' % (url))

class ServiceMetadataRetrievalFailure(Exception):
    def __init__(self, url):
        Exception.__init__(self, '[ERROR]:: Service [\'%s\'] metadata retrieval failure' % (url))

class AccessRuleValidation(Exception):
    def __init__(self, module, fName):
        Exception.__init__(self, '[ERROR]:: \'%s\' is not accessible member of \'%s\'!' % (fName, module))

class WrongArgumentFormat(Exception):
    def __init__(self, arg):
        Exception.__init__(self, '[ERROR]:: Wrong argument format [%s], argument must start with \'-\' or \'--\'!' % arg)

class NoFurtherEntries(Exception):
    def __init__(self, name):
        Exception.__init__(self, "[ERROR]:: No further entries of \'%s\' can be created!" % name)

class ServiceNotFound(Exception):
    def __init__(self, name):
        Exception.__init__(self, "[ERROR]:: Service not found: '%s'!" % name)

class TypeNotFound(Exception):
    def __init__(self, name):
        Exception.__init__(self, "[ERROR]:: Type not found: '%s'!" % (name))

class NotValidArgumentForMethod(Exception):
    def __init__(self, method, key):
        Exception.__init__(self, '[ERROR]:: NOT valid argument \'-%s\' for method \'%s\', please review help!' % (key, method))

class MethodShouldHaveNoArgs(Exception):
    def __init__(self, methodName, arg):
        Exception.__init__(self, '[ERROR]:: Method \'%s\' should have no args, wile specified \'%s\'!' % (methodName, arg))

class NoArgumentsSpecified(Exception):
    def __init__(self):
        Exception.__init__(self, '[ERROR]:: No arguments specified!')

class ConfigurationFileNotFound(Exception):
    def __init__(self, curdir, file_path):
        Exception.__init__(self, '[ERROR]:: Curr. dir. is: %s,\nConfiguration file NOT found at \'%s\' or not accessible!' % (curdir, file_path))

class RhevmClientHandlerInitiationTimeout(Exception):
    def __init__(self, ttl):
        Exception.__init__(self, '[ERROR]:: oVirt ClientHandler Initiation Timed Out [%s seconds]!' % (ttl))

class ExpectationError(Exception):
    def __init__(self, expect):
        Exception.__init__(self, '[ERROR]:: %s' % expect)

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
