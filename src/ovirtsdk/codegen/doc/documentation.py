'''
Created on Dec 7, 2011

@author: mpastern
'''

class Documentation():
    ''' Documentation '''
    DOC_OFFSET = '        '

    @staticmethod
    def document(link, custom_params={}):#argument_type, signatures, return_type):
        '''
        @param body: request body
        @param custom_params: custom params to add {param:mandatory=true|false}
        @param offset: documentation offset
        
        @return: method documentation
        '''

        #link.request.body.parameters_set[0].parameter

        i = 0
        offset = Documentation.DOC_OFFSET

        doc_str = ""
        doc_str_in = offset + "'''\n"
        doc_str_out = offset + "'''\n\n"

        type_doc = offset + "@type %s:\n\n" % Documentation._getRequestType(link)
        return_doc = offset + "@return %s:\n" % Documentation._getResponseType(link)

        parameters_set_template = offset + "Overload %s:\n"
        parameters_set_offset = '  '
        mand_param_doc_template = "@param %s: %s\n"
        opt_param_doc_template = "[@param %s: %s]\n"
        custom_mand_param_doc_template = "@param %s\n"
        custom_opt_param_doc_template = "[@param %s]\n"

        doc_str += doc_str_in
        doc_str += type_doc if type_doc.find('@type None:') == -1 else ''
        if hasattr(link, 'request') and hasattr(link.request, 'body') and hasattr(link.request.body, 'parameters_set'):
            for parameters_set in link.request.body.parameters_set:
                if len(link.request.body.parameters_set) > 1:
                    i += 1
                    mand_params = ''
                    opt_params = ''
                    doc_str += parameters_set_template % str(i)
                    for parameter in parameters_set.parameter:
                        if parameter.mandatory == True:
                            mand_params += offset + \
                                           parameters_set_offset + \
                                           mand_param_doc_template % (parameter.name, parameter.type_.replace('xs:', ''))
                        else:
                            opt_params += offset + \
                                          parameters_set_offset + \
                                          opt_param_doc_template % (parameter.name, parameter.type_.replace('xs:', ''))
                else:
                    mand_params = ''
                    opt_params = ''
                    for parameter in parameters_set.parameter:
                        if parameter.mandatory == True:
                            mand_params += offset + \
                                           mand_param_doc_template % (parameter.name, parameter.type_.replace('xs:', ''))
                        else:
                            opt_params += offset + \
                                          opt_param_doc_template % (parameter.name, parameter.type_.replace('xs:', ''))
                doc_str += mand_params
                doc_str += opt_params

        for k in custom_params.keys(): #TODO: revisit - not optimal in terms of overload
            if custom_params[k] == True:
                doc_str += offset + custom_mand_param_doc_template % k
            else:
                doc_str += offset + custom_opt_param_doc_template % k

        doc_str += (('\n' + return_doc) if doc_str != offset + "'''\n"
                                        else return_doc)
        doc_str += doc_str_out

        return doc_str

    @staticmethod
    def _getRequestType(link):
        if link.rel != 'update' and hasattr(link, 'request') and hasattr(link.request, 'body') and hasattr(link.request.body, 'type_'):
            return link.request.body.type_
        return None

    @staticmethod
    def _getResponseType(link):
        if hasattr(link, 'response') and hasattr(link.response, 'type_'):
            return link.response.type_
        return None
