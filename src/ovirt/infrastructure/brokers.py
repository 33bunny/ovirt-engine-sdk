

########################################
############ GENERATED CODE ############
########################################

'''
Generated at: 2011-11-09 13:08:18.363238

@author: mpastern@redhat.com
'''

from ovirt.xml import params
from ovirt.utils.urlhelper import UrlHelper
from ovirt.utils.filterhelper import FilterHelper
from ovirt.utils.parsehelper import ParseHelper
from ovirt.utils.searchhelper import SearchHelper
from ovirt.infrastructure.common import Base


class ClusterNetwork(params.Network, Base):
    def __init__(self, cluster, network):
        self.parentclass = cluster
        self.superclass  =  network

    def __new__(cls, cluster, network):
        if network is None: return None
        obj = object.__new__(cls)
        obj.__init__(cluster, network)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/clusters/{cluster:id}/networks/{network:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{cluster:id}' : self.parentclass.get_id(),
                                                                         '{network:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{cluster:id}' : self.parentclass.get_id(),
                                                                         '{network:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def update(self):
        url = '/api/clusters/{cluster:id}/networks/{network:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{cluster:id}' : self.parentclass.get_id(),
                                                                     '{network:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))

        return ClusterNetwork(self.parentclass, result)

class ClusterNetworks(Base):
 
    def __init__(self, cluster):
        self.parentclass = cluster

    def add(self, network):

        url = '/api/clusters/{cluster:id}/networks'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{cluster:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(network))

        return ClusterNetwork(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/clusters/{cluster:id}/networks'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{cluster:id}': self.parentclass.get_id()})).get_clusternetwork()

        return ClusterNetwork(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/clusters/{cluster:id}/networks'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{cluster:id}': self.parentclass.get_id()})).get_clusternetwork()

        return ParseHelper.toSubCollection(ClusterNetwork,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class ClusterPermission(params.Permission, Base):
    def __init__(self, cluster, permission):
        self.parentclass = cluster
        self.superclass  =  permission

    def __new__(cls, cluster, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(cluster, permission)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/clusters/{cluster:id}/permissions/{permission:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{cluster:id}' : self.parentclass.get_id(),
                                                                         '{permission:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{cluster:id}' : self.parentclass.get_id(),
                                                                         '{permission:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class ClusterPermissions(Base):
 
    def __init__(self, cluster):
        self.parentclass = cluster

    def add(self, permission):

        url = '/api/clusters/{cluster:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{cluster:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permission))

        return ClusterPermission(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/clusters/{cluster:id}/permissions'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{cluster:id}': self.parentclass.get_id()})).get_clusterpermission()

        return ClusterPermission(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/clusters/{cluster:id}/permissions'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{cluster:id}': self.parentclass.get_id()})).get_clusterpermission()

        return ParseHelper.toSubCollection(ClusterPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class DatacenterPermission(params.Permission, Base):
    def __init__(self, datacenter, permission):
        self.parentclass = datacenter
        self.superclass  =  permission

    def __new__(cls, datacenter, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(datacenter, permission)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/datacenters/{datacenter:id}/permissions/{permission:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{datacenter:id}' : self.parentclass.get_id(),
                                                                         '{permission:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{datacenter:id}' : self.parentclass.get_id(),
                                                                         '{permission:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class DatacenterPermissions(Base):
 
    def __init__(self, datacenter):
        self.parentclass = datacenter

    def add(self, permission):

        url = '/api/datacenters/{datacenter:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{datacenter:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permission))

        return DatacenterPermission(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/datacenters/{datacenter:id}/permissions'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{datacenter:id}': self.parentclass.get_id()})).get_datacenterpermission()

        return DatacenterPermission(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/datacenters/{datacenter:id}/permissions'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{datacenter:id}': self.parentclass.get_id()})).get_datacenterpermission()

        return ParseHelper.toSubCollection(DatacenterPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class DatacenterStoragedomain(params.StorageDomain, Base):
    def __init__(self, datacenter, storagedomain):
        self.parentclass = datacenter
        self.superclass  =  storagedomain

    def __new__(cls, datacenter, storagedomain):
        if storagedomain is None: return None
        obj = object.__new__(cls)
        obj.__init__(datacenter, storagedomain)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{datacenter:id}' : self.parentclass.get_id(),
                                                                         '{storagedomain:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{datacenter:id}' : self.parentclass.get_id(),
                                                                         '{storagedomain:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def activate(self):
        url = '/api/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}/activate'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{datacenter:id}' : self.parentclass.get_id(),
                                                                     '{storagedomain:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))

        return result

    def deactivate(self):
        url = '/api/datacenters/{datacenter:id}/storagedomains/{storagedomain:id}/deactivate'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{datacenter:id}' : self.parentclass.get_id(),
                                                                     '{storagedomain:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))

        return result

class DatacenterStoragedomains(Base):
 
    def __init__(self, datacenter):
        self.parentclass = datacenter

    def add(self, storagedomain):

        url = '/api/datacenters/{datacenter:id}/storagedomains'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{datacenter:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(storagedomain))

        return DatacenterStoragedomain(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/datacenters/{datacenter:id}/storagedomains'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{datacenter:id}': self.parentclass.get_id()})).get_datacenterstoragedomain()

        return DatacenterStoragedomain(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/datacenters/{datacenter:id}/storagedomains'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{datacenter:id}': self.parentclass.get_id()})).get_datacenterstoragedomain()

        return ParseHelper.toSubCollection(DatacenterStoragedomain,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class DomainGroup(params.Group, Base):
    def __init__(self, domain, group):
        self.parentclass = domain
        self.superclass  =  group

    def __new__(cls, domain, group):
        if group is None: return None
        obj = object.__new__(cls)
        obj.__init__(domain, group)
        return obj

class DomainGroups(Base):
 
    def __init__(self, domain):
        self.parentclass = domain

    def get(self, name='None', **kwargs):

        url = '/api/domains/{domain:id}/groups'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{domain:id}': self.parentclass.get_id()})).get_domaingroup()

        return DomainGroup(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/domains/{domain:id}/groups'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{domain:id}': self.parentclass.get_id()})).get_domaingroup()

        return ParseHelper.toSubCollection(DomainGroup,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class DomainUser(params.User, Base):
    def __init__(self, domain, user):
        self.parentclass = domain
        self.superclass  =  user

    def __new__(cls, domain, user):
        if user is None: return None
        obj = object.__new__(cls)
        obj.__init__(domain, user)
        return obj

class DomainUsers(Base):
 
    def __init__(self, domain):
        self.parentclass = domain

    def get(self, name='None', **kwargs):

        url = '/api/domains/{domain:id}/users'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{domain:id}': self.parentclass.get_id()})).get_domainuser()

        return DomainUser(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/domains/{domain:id}/users'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{domain:id}': self.parentclass.get_id()})).get_domainuser()

        return ParseHelper.toSubCollection(DomainUser,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class GroupPermission(params.Permission, Base):
    def __init__(self, group, permission):
        self.parentclass = group
        self.superclass  =  permission

    def __new__(cls, group, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(group, permission)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/groups/{group:id}/permissions/{permission:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{group:id}' : self.parentclass.get_id(),
                                                                         '{permission:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{group:id}' : self.parentclass.get_id(),
                                                                         '{permission:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class GroupPermissions(Base):
 
    def __init__(self, group):
        self.parentclass = group

    def add(self, permission):

        url = '/api/groups/{group:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{group:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permission))

        return GroupPermission(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/groups/{group:id}/permissions'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{group:id}': self.parentclass.get_id()})).get_grouppermission()

        return GroupPermission(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/groups/{group:id}/permissions'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{group:id}': self.parentclass.get_id()})).get_grouppermission()

        return ParseHelper.toSubCollection(GroupPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class GroupRole(params.Role, Base):
    def __init__(self, group, role):
        self.parentclass = group
        self.superclass  =  role

    def __new__(cls, group, role):
        if role is None: return None
        obj = object.__new__(cls)
        obj.__init__(group, role)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/groups/{group:id}/roles/{role:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{group:id}' : self.parentclass.get_id(),
                                                                         '{role:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{group:id}' : self.parentclass.get_id(),
                                                                         '{role:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class GroupRoles(Base):
 
    def __init__(self, group):
        self.parentclass = group

    def add(self, role):

        url = '/api/groups/{group:id}/roles'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{group:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(role))

        return GroupRole(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/groups/{group:id}/roles'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{group:id}': self.parentclass.get_id()})).get_grouprole()

        return GroupRole(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/groups/{group:id}/roles'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{group:id}': self.parentclass.get_id()})).get_grouprole()

        return ParseHelper.toSubCollection(GroupRole,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class GroupTag(params.Tag, Base):
    def __init__(self, group, tag):
        self.parentclass = group
        self.superclass  =  tag

    def __new__(cls, group, tag):
        if tag is None: return None
        obj = object.__new__(cls)
        obj.__init__(group, tag)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/groups/{group:id}/tags/{tag:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{group:id}' : self.parentclass.get_id(),
                                                                         '{tag:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{group:id}' : self.parentclass.get_id(),
                                                                         '{tag:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class GroupTags(Base):
 
    def __init__(self, group):
        self.parentclass = group

    def add(self, tag):

        url = '/api/groups/{group:id}/tags'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{group:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(tag))

        return GroupTag(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/groups/{group:id}/tags'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{group:id}': self.parentclass.get_id()})).get_grouptag()

        return GroupTag(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/groups/{group:id}/tags'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{group:id}': self.parentclass.get_id()})).get_grouptag()

        return ParseHelper.toSubCollection(GroupTag,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class GroupsRolePermit(params.Permit, Base):
    def __init__(self, groupsRole, permit):
        self.parentclass = groupsRole
        self.superclass  =  permit

    def __new__(cls, groupsRole, permit):
        if permit is None: return None
        obj = object.__new__(cls)
        obj.__init__(groupsRole, permit)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/groups/{group:id}/roles/{role:id}/permits/{permit:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{groupsRole:id}' : self.parentclass.get_id(),
                                                                         '{Permit:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{groupsRole:id}' : self.parentclass.get_id(),
                                                                         '{Permit:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class HostNIC(params.HostNIC, Base):
    def __init__(self, host, nic):
        self.parentclass = host
        self.superclass  =  nic

    def __new__(cls, host, nic):
        if nic is None: return None
        obj = object.__new__(cls)
        obj.__init__(host, nic)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/hosts/{host:id}/nics/{nic:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{host:id}' : self.parentclass.get_id(),
                                                                         '{nic:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{host:id}' : self.parentclass.get_id(),
                                                                         '{nic:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def detach(self):
        url = '/api/hosts/{host:id}/nics/{nic:id}/detach'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}' : self.parentclass.get_id(),
                                                                     '{nic:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))

        return result

    def attach(self):
        url = '/api/hosts/{host:id}/nics/{nic:id}/attach'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}' : self.parentclass.get_id(),
                                                                     '{nic:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))

        return result

    def update(self):
        url = '/api/hosts/{host:id}/nics/{nic:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{host:id}' : self.parentclass.get_id(),
                                                                     '{nic:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))

        return HostNIC(self.parentclass, result)

class HostNics(Base):
 
    def __init__(self, host):
        self.parentclass = host

    def add(self, nic):

        url = '/api/hosts/{host:id}/nics'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(nic))

        return HostNIC(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/hosts/{host:id}/nics'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()})).get_hostnic()

        return HostNIC(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/hosts/{host:id}/nics'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()})).get_hostnic()

        return ParseHelper.toSubCollection(HostNIC,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class HostPermission(params.Permission, Base):
    def __init__(self, host, permission):
        self.parentclass = host
        self.superclass  =  permission

    def __new__(cls, host, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(host, permission)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/hosts/{host:id}/permissions/{permission:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{host:id}' : self.parentclass.get_id(),
                                                                         '{permission:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{host:id}' : self.parentclass.get_id(),
                                                                         '{permission:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class HostPermissions(Base):
 
    def __init__(self, host):
        self.parentclass = host

    def add(self, permission):

        url = '/api/hosts/{host:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permission))

        return HostPermission(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/hosts/{host:id}/permissions'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()})).get_hostpermission()

        return HostPermission(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/hosts/{host:id}/permissions'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()})).get_hostpermission()

        return ParseHelper.toSubCollection(HostPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class HostStatistic(params.Statistic, Base):
    def __init__(self, host, statistic):
        self.parentclass = host
        self.superclass  =  statistic

    def __new__(cls, host, statistic):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(host, statistic)
        return obj

class HostStatistics(Base):
 
    def __init__(self, host):
        self.parentclass = host

    def get(self, name='None', **kwargs):

        url = '/api/hosts/{host:id}/statistics'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()})).get_hoststatistic()

        return HostStatistic(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/hosts/{host:id}/statistics'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()})).get_hoststatistic()

        return ParseHelper.toSubCollection(HostStatistic,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class HostStorage(params.HostStorage, Base):
    def __init__(self, host, storage):
        self.parentclass = host
        self.superclass  =  storage

    def __new__(cls, host, storage):
        if storage is None: return None
        obj = object.__new__(cls)
        obj.__init__(host, storage)
        return obj

class HostTag(params.Tag, Base):
    def __init__(self, host, tag):
        self.parentclass = host
        self.superclass  =  tag

    def __new__(cls, host, tag):
        if tag is None: return None
        obj = object.__new__(cls)
        obj.__init__(host, tag)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/hosts/{host:id}/tags/{tag:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{host:id}' : self.parentclass.get_id(),
                                                                         '{tag:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{host:id}' : self.parentclass.get_id(),
                                                                         '{tag:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class HostTags(Base):
 
    def __init__(self, host):
        self.parentclass = host

    def add(self, tag):

        url = '/api/hosts/{host:id}/tags'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(tag))

        return HostTag(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/hosts/{host:id}/tags'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()})).get_hosttag()

        return HostTag(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/hosts/{host:id}/tags'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{host:id}': self.parentclass.get_id()})).get_hosttag()

        return ParseHelper.toSubCollection(HostTag,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class HostsNicStatistic(params.Statistic, Base):
    def __init__(self, hostsNic, statistic):
        self.parentclass = hostsNic
        self.superclass  =  statistic

    def __new__(cls, hostsNic, statistic):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(hostsNic, statistic)
        return obj

class RolePermit(params.Permit, Base):
    def __init__(self, role, permit):
        self.parentclass = role
        self.superclass  =  permit

    def __new__(cls, role, permit):
        if permit is None: return None
        obj = object.__new__(cls)
        obj.__init__(role, permit)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/roles/{role:id}/permits/{permit:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{role:id}' : self.parentclass.get_id(),
                                                                         '{permit:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{role:id}' : self.parentclass.get_id(),
                                                                         '{permit:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class RolePermits(Base):
 
    def __init__(self, role):
        self.parentclass = role

    def add(self, permit):

        url = '/api/roles/{role:id}/permits'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{role:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permit))

        return RolePermit(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/roles/{role:id}/permits'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{role:id}': self.parentclass.get_id()})).get_rolepermit()

        return RolePermit(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/roles/{role:id}/permits'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{role:id}': self.parentclass.get_id()})).get_rolepermit()

        return ParseHelper.toSubCollection(RolePermit,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class StoragedomainFile(params.File, Base):
    def __init__(self, storagedomain, file):
        self.parentclass = storagedomain
        self.superclass  =  file

    def __new__(cls, storagedomain, file):
        if file is None: return None
        obj = object.__new__(cls)
        obj.__init__(storagedomain, file)
        return obj

class StoragedomainFiles(Base):
 
    def __init__(self, storagedomain):
        self.parentclass = storagedomain

    def get(self, name='None', **kwargs):

        url = '/api/storagedomains/{storagedomain:id}/files'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{storagedomain:id}': self.parentclass.get_id()})).get_storagedomainfile()

        return StoragedomainFile(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/storagedomains/{storagedomain:id}/files'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{storagedomain:id}': self.parentclass.get_id()})).get_storagedomainfile()

        return ParseHelper.toSubCollection(StoragedomainFile,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class StoragedomainPermission(params.Permission, Base):
    def __init__(self, storagedomain, permission):
        self.parentclass = storagedomain
        self.superclass  =  permission

    def __new__(cls, storagedomain, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(storagedomain, permission)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/storagedomains/{storagedomain:id}/permissions/{permission:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{storagedomain:id}' : self.parentclass.get_id(),
                                                                         '{permission:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{storagedomain:id}' : self.parentclass.get_id(),
                                                                         '{permission:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class StoragedomainPermissions(Base):
 
    def __init__(self, storagedomain):
        self.parentclass = storagedomain

    def add(self, permission):

        url = '/api/storagedomains/{storagedomain:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{storagedomain:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permission))

        return StoragedomainPermission(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/storagedomains/{storagedomain:id}/permissions'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{storagedomain:id}': self.parentclass.get_id()})).get_storagedomainpermission()

        return StoragedomainPermission(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/storagedomains/{storagedomain:id}/permissions'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{storagedomain:id}': self.parentclass.get_id()})).get_storagedomainpermission()

        return ParseHelper.toSubCollection(StoragedomainPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class StoragedomainTemplate(params.Template, Base):
    def __init__(self, storagedomain, template):
        self.parentclass = storagedomain
        self.superclass  =  template

    def __new__(cls, storagedomain, template):
        if template is None: return None
        obj = object.__new__(cls)
        obj.__init__(storagedomain, template)
        return obj

    def import_storagedomain(self):
        url = '/api/storagedomains/{storagedomain:id}/templates/{template:id}/import'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{storagedomain:id}' : self.parentclass.get_id(),
                                                                     '{template:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))

        return result

class StoragedomainTemplates(Base):
 
    def __init__(self, storagedomain):
        self.parentclass = storagedomain

    def get(self, name='None', **kwargs):

        url = '/api/storagedomains/{storagedomain:id}/templates'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{storagedomain:id}': self.parentclass.get_id()})).get_storagedomaintemplate()

        return StoragedomainTemplate(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/storagedomains/{storagedomain:id}/templates'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{storagedomain:id}': self.parentclass.get_id()})).get_storagedomaintemplate()

        return ParseHelper.toSubCollection(StoragedomainTemplate,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class StoragedomainVm(params.VM, Base):
    def __init__(self, storagedomain, vm):
        self.parentclass = storagedomain
        self.superclass  =  vm

    def __new__(cls, storagedomain, vm):
        if vm is None: return None
        obj = object.__new__(cls)
        obj.__init__(storagedomain, vm)
        return obj

    def import_storagedomain(self):
        url = '/api/storagedomains/{storagedomain:id}/vms/{vm:id}/import'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{storagedomain:id}' : self.parentclass.get_id(),
                                                                     '{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))

        return result

class StoragedomainVms(Base):
 
    def __init__(self, storagedomain):
        self.parentclass = storagedomain

    def get(self, name='None', **kwargs):

        url = '/api/storagedomains/{storagedomain:id}/vms'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{storagedomain:id}': self.parentclass.get_id()})).get_storagedomainvm()

        return StoragedomainVm(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/storagedomains/{storagedomain:id}/vms'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{storagedomain:id}': self.parentclass.get_id()})).get_storagedomainvm()

        return ParseHelper.toSubCollection(StoragedomainVm,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class TemplateCdrom(params.CdRom, Base):
    def __init__(self, template, cdrom):
        self.parentclass = template
        self.superclass  =  cdrom

    def __new__(cls, template, cdrom):
        if cdrom is None: return None
        obj = object.__new__(cls)
        obj.__init__(template, cdrom)
        return obj

class TemplateCdroms(Base):
 
    def __init__(self, template):
        self.parentclass = template

    def get(self, name='None', **kwargs):

        url = '/api/templates/{template:id}/cdroms'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{template:id}': self.parentclass.get_id()})).get_templatecdrom()

        return TemplateCdrom(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/templates/{template:id}/cdroms'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{template:id}': self.parentclass.get_id()})).get_templatecdrom()

        return ParseHelper.toSubCollection(TemplateCdrom,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class TemplateDisk(params.Disk, Base):
    def __init__(self, template, disk):
        self.parentclass = template
        self.superclass  =  disk

    def __new__(cls, template, disk):
        if disk is None: return None
        obj = object.__new__(cls)
        obj.__init__(template, disk)
        return obj

class TemplateDisks(Base):
 
    def __init__(self, template):
        self.parentclass = template

    def get(self, name='None', **kwargs):

        url = '/api/templates/{template:id}/disks'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{template:id}': self.parentclass.get_id()})).get_templatedisk()

        return TemplateDisk(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/templates/{template:id}/disks'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{template:id}': self.parentclass.get_id()})).get_templatedisk()

        return ParseHelper.toSubCollection(TemplateDisk,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class TemplateNic(params.NIC, Base):
    def __init__(self, template, nic):
        self.parentclass = template
        self.superclass  =  nic

    def __new__(cls, template, nic):
        if nic is None: return None
        obj = object.__new__(cls)
        obj.__init__(template, nic)
        return obj

class TemplateNics(Base):
 
    def __init__(self, template):
        self.parentclass = template

    def get(self, name='None', **kwargs):

        url = '/api/templates/{template:id}/nics'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{template:id}': self.parentclass.get_id()})).get_templatenic()

        return TemplateNic(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/templates/{template:id}/nics'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{template:id}': self.parentclass.get_id()})).get_templatenic()

        return ParseHelper.toSubCollection(TemplateNic,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class TemplatePermission(params.Permission, Base):
    def __init__(self, template, permission):
        self.parentclass = template
        self.superclass  =  permission

    def __new__(cls, template, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(template, permission)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/templates/{template:id}/permissions/{permission:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{template:id}' : self.parentclass.get_id(),
                                                                         '{permission:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{template:id}' : self.parentclass.get_id(),
                                                                         '{permission:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class TemplatePermissions(Base):
 
    def __init__(self, template):
        self.parentclass = template

    def add(self, permission):

        url = '/api/templates/{template:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{template:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permission))

        return TemplatePermission(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/templates/{template:id}/permissions'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{template:id}': self.parentclass.get_id()})).get_templatepermission()

        return TemplatePermission(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/templates/{template:id}/permissions'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{template:id}': self.parentclass.get_id()})).get_templatepermission()

        return ParseHelper.toSubCollection(TemplatePermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class UserPermission(params.Permission, Base):
    def __init__(self, user, permission):
        self.parentclass = user
        self.superclass  =  permission

    def __new__(cls, user, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(user, permission)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/users/{user:id}/permissions/{permission:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{user:id}' : self.parentclass.get_id(),
                                                                         '{permission:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{user:id}' : self.parentclass.get_id(),
                                                                         '{permission:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class UserPermissions(Base):
 
    def __init__(self, user):
        self.parentclass = user

    def add(self, permission):

        url = '/api/users/{user:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{user:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permission))

        return UserPermission(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/users/{user:id}/permissions'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{user:id}': self.parentclass.get_id()})).get_userpermission()

        return UserPermission(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/users/{user:id}/permissions'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{user:id}': self.parentclass.get_id()})).get_userpermission()

        return ParseHelper.toSubCollection(UserPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class UserRole(params.Role, Base):
    def __init__(self, user, role):
        self.parentclass = user
        self.superclass  =  role

    def __new__(cls, user, role):
        if role is None: return None
        obj = object.__new__(cls)
        obj.__init__(user, role)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/users/{user:id}/roles/{role:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{user:id}' : self.parentclass.get_id(),
                                                                         '{role:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{user:id}' : self.parentclass.get_id(),
                                                                         '{role:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class UserRoles(Base):
 
    def __init__(self, user):
        self.parentclass = user

    def add(self, role):

        url = '/api/users/{user:id}/roles'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{user:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(role))

        return UserRole(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/users/{user:id}/roles'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{user:id}': self.parentclass.get_id()})).get_userrole()

        return UserRole(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/users/{user:id}/roles'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{user:id}': self.parentclass.get_id()})).get_userrole()

        return ParseHelper.toSubCollection(UserRole,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class UserTag(params.Tag, Base):
    def __init__(self, user, tag):
        self.parentclass = user
        self.superclass  =  tag

    def __new__(cls, user, tag):
        if tag is None: return None
        obj = object.__new__(cls)
        obj.__init__(user, tag)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/users/{user:id}/tags/{tag:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{user:id}' : self.parentclass.get_id(),
                                                                         '{tag:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{user:id}' : self.parentclass.get_id(),
                                                                         '{tag:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class UserTags(Base):
 
    def __init__(self, user):
        self.parentclass = user

    def add(self, tag):

        url = '/api/users/{user:id}/tags'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{user:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(tag))

        return UserTag(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/users/{user:id}/tags'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{user:id}': self.parentclass.get_id()})).get_usertag()

        return UserTag(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/users/{user:id}/tags'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{user:id}': self.parentclass.get_id()})).get_usertag()

        return ParseHelper.toSubCollection(UserTag,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class UsersRolePermit(params.Permit, Base):
    def __init__(self, usersRole, permit):
        self.parentclass = usersRole
        self.superclass  =  permit

    def __new__(cls, usersRole, permit):
        if permit is None: return None
        obj = object.__new__(cls)
        obj.__init__(usersRole, permit)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/users/{user:id}/roles/{role:id}/permits/{permit:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{usersRole:id}' : self.parentclass.get_id(),
                                                                         '{Permit:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{usersRole:id}' : self.parentclass.get_id(),
                                                                         '{Permit:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class VmCdrom(params.CdRom, Base):
    def __init__(self, vm, cdrom):
        self.parentclass = vm
        self.superclass  =  cdrom

    def __new__(cls, vm, cdrom):
        if cdrom is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, cdrom)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/vms/{vm:id}/cdroms/{cdrom:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                         '{cdrom:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                         '{cdrom:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def update(self):
        url = '/api/vms/{vm:id}/cdroms/{cdrom:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                     '{cdrom:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))

        return VmCdrom(self.parentclass, result)

class VmCdroms(Base):
 
    def __init__(self, vm):
        self.parentclass = vm

    def add(self, cdrom):

        url = '/api/vms/{vm:id}/cdroms'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(cdrom))

        return VmCdrom(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/vms/{vm:id}/cdroms'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_vmcdrom()

        return VmCdrom(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/vms/{vm:id}/cdroms'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_vmcdrom()

        return ParseHelper.toSubCollection(VmCdrom,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VmDisk(params.Disk, Base):
    def __init__(self, vm, disk):
        self.parentclass = vm
        self.superclass  =  disk

    def __new__(cls, vm, disk):
        if disk is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, disk)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/vms/{vm:id}/disks/{disk:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                         '{disk:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                         '{disk:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def update(self):
        url = '/api/vms/{vm:id}/disks/{disk:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                     '{disk:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))

        return VmDisk(self.parentclass, result)

class VmDisks(Base):
 
    def __init__(self, vm):
        self.parentclass = vm

    def add(self, disk):

        url = '/api/vms/{vm:id}/disks'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(disk))

        return VmDisk(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/vms/{vm:id}/disks'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_vmdisk()

        return VmDisk(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/vms/{vm:id}/disks'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_vmdisk()

        return ParseHelper.toSubCollection(VmDisk,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VmNic(params.NIC, Base):
    def __init__(self, vm, nic):
        self.parentclass = vm
        self.superclass  =  nic

    def __new__(cls, vm, nic):
        if nic is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, nic)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/vms/{vm:id}/nics/{nic:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                         '{nic:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                         '{nic:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def update(self):
        url = '/api/vms/{vm:id}/nics/{nic:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                     '{nic:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))

        return VmNic(self.parentclass, result)

class VmNics(Base):
 
    def __init__(self, vm):
        self.parentclass = vm

    def add(self, nic):

        url = '/api/vms/{vm:id}/nics'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(nic))

        return VmNic(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/vms/{vm:id}/nics'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_vmnic()

        return VmNic(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/vms/{vm:id}/nics'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_vmnic()

        return ParseHelper.toSubCollection(VmNic,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VmPermission(params.Permission, Base):
    def __init__(self, vm, permission):
        self.parentclass = vm
        self.superclass  =  permission

    def __new__(cls, vm, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, permission)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/vms/{vm:id}/permissions/{permission:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                         '{permission:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                         '{permission:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class VmPermissions(Base):
 
    def __init__(self, vm):
        self.parentclass = vm

    def add(self, permission):

        url = '/api/vms/{vm:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permission))

        return VmPermission(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/vms/{vm:id}/permissions'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_vmpermission()

        return VmPermission(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/vms/{vm:id}/permissions'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_vmpermission()

        return ParseHelper.toSubCollection(VmPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VmSnapshot(params.Snapshot, Base):
    def __init__(self, vm, snapshot):
        self.parentclass = vm
        self.superclass  =  snapshot

    def __new__(cls, vm, snapshot):
        if snapshot is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, snapshot)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/vms/{vm:id}/snapshots/{snapshot:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                         '{snapshot:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                         '{snapshot:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def restore(self):
        url = '/api/vms/{vm:id}/snapshots/{snapshot:id}/restore'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                     '{snapshot:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))

        return result

class VmSnapshots(Base):
 
    def __init__(self, vm):
        self.parentclass = vm

    def add(self, snapshot):

        url = '/api/vms/{vm:id}/snapshots'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(snapshot))

        return VmSnapshot(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/vms/{vm:id}/snapshots'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_vmsnapshot()

        return VmSnapshot(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/vms/{vm:id}/snapshots'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_vmsnapshot()

        return ParseHelper.toSubCollection(VmSnapshot,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VmStatistic(params.Statistic, Base):
    def __init__(self, vm, statistic):
        self.parentclass = vm
        self.superclass  =  statistic

    def __new__(cls, vm, statistic):
        if statistic is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, statistic)
        return obj

class VmStatistics(Base):
 
    def __init__(self, vm):
        self.parentclass = vm

    def get(self, name='None', **kwargs):

        url = '/api/vms/{vm:id}/statistics'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_vmstatistic()

        return VmStatistic(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/vms/{vm:id}/statistics'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_vmstatistic()

        return ParseHelper.toSubCollection(VmStatistic,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VmTag(params.Tag, Base):
    def __init__(self, vm, tag):
        self.parentclass = vm
        self.superclass  =  tag

    def __new__(cls, vm, tag):
        if tag is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm, tag)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/vms/{vm:id}/tags/{tag:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                         '{tag:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{vm:id}' : self.parentclass.get_id(),
                                                                         '{tag:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class VmTags(Base):
 
    def __init__(self, vm):
        self.parentclass = vm

    def add(self, tag):

        url = '/api/vms/{vm:id}/tags'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(tag))

        return VmTag(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/vms/{vm:id}/tags'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_vmtag()

        return VmTag(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/vms/{vm:id}/tags'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vm:id}': self.parentclass.get_id()})).get_vmtag()

        return ParseHelper.toSubCollection(VmTag,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class VmpoolPermission(params.Permission, Base):
    def __init__(self, vmpool, permission):
        self.parentclass = vmpool
        self.superclass  =  permission

    def __new__(cls, vmpool, permission):
        if permission is None: return None
        obj = object.__new__(cls)
        obj.__init__(vmpool, permission)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/vmpools/{vmpool:id}/permissions/{permission:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{vmpool:id}' : self.parentclass.get_id(),
                                                                         '{permission:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{vmpool:id}' : self.parentclass.get_id(),
                                                                         '{permission:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class VmpoolPermissions(Base):
 
    def __init__(self, vmpool):
        self.parentclass = vmpool

    def add(self, permission):

        url = '/api/vmpools/{vmpool:id}/permissions'

        result = self._getProxy().add(url=UrlHelper.replace(url, {'{vmpool:id}': self.parentclass.get_id()}),
                                      body=ParseHelper.toXml(permission))

        return VmpoolPermission(self.parentclass, result)

    def get(self, name='None', **kwargs):

        url = '/api/vmpools/{vmpool:id}/permissions'

        if(name is not None): kwargs['name']=name
        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vmpool:id}': self.parentclass.get_id()})).get_vmpoolpermission()

        return VmpoolPermission(self.parentclass,
                   FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, **kwargs):
        '''
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url = '/api/vmpools/{vmpool:id}/permissions'

        result = self._getProxy().get(url=UrlHelper.replace(url, {'{vmpool:id}': self.parentclass.get_id()})).get_vmpoolpermission()

        return ParseHelper.toSubCollection(VmpoolPermission,
                                           self.parentclass,
                                           FilterHelper.filter(result, kwargs))

class Capabilities(Base):
    def __init__(self):
        """Constructor."""

    def get(self, name='*', **kwargs):
        url = '/api/capabilities'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_capabilities()
        return Capabilities(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/capabilities'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_capabilities()
        return ParseHelper.toCollection(Capabilities,
                                        FilterHelper.filter(result, kwargs))

class Cluster(params.Cluster, Base):
    def __init__(self, cluster):
        self.superclass = cluster

    def __new__(cls, cluster):
        if cluster is None: return None
        obj = object.__new__(cls)
        obj.__init__(cluster)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/clusters/{cluster:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{cluster:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{cluster:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def update(self):
        url = '/api/clusters/{cluster:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{cluster:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))
        return Cluster(result)

class Clusters(Base):
    def __init__(self):
        """Constructor."""

    def add(self, cluster):
        url = '/api/clusters'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(cluster))
        return Cluster(result)

    def get(self, name='*', **kwargs):
        url = '/api/clusters'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_cluster()
        return Cluster(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/clusters'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_cluster()
        return ParseHelper.toCollection(Cluster,
                                        FilterHelper.filter(result, kwargs))

class DataCenter(params.DataCenter, Base):
    def __init__(self, datacenter):
        self.superclass = datacenter

    def __new__(cls, datacenter):
        if datacenter is None: return None
        obj = object.__new__(cls)
        obj.__init__(datacenter)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/datacenters/{datacenter:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{datacenter:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{datacenter:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def update(self):
        url = '/api/datacenters/{datacenter:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{datacenter:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))
        return DataCenter(result)

class DataCenters(Base):
    def __init__(self):
        """Constructor."""

    def add(self, datacenter):
        url = '/api/datacenters'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(datacenter))
        return DataCenter(result)

    def get(self, name='*', **kwargs):
        url = '/api/datacenters'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_datacenter()
        return DataCenter(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/datacenters'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_datacenter()
        return ParseHelper.toCollection(DataCenter,
                                        FilterHelper.filter(result, kwargs))

class Domain(params.Domain, Base):
    def __init__(self, domain):
        self.superclass = domain

    def __new__(cls, domain):
        if domain is None: return None
        obj = object.__new__(cls)
        obj.__init__(domain)
        return obj

class Domains(Base):
    def __init__(self):
        """Constructor."""

    def get(self, name='*', **kwargs):
        url = '/api/domains'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_domain()
        return Domain(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/domains'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_domain()
        return ParseHelper.toCollection(Domain,
                                        FilterHelper.filter(result, kwargs))

class Event(params.Event, Base):
    def __init__(self, event):
        self.superclass = event

    def __new__(cls, event):
        if event is None: return None
        obj = object.__new__(cls)
        obj.__init__(event)
        return obj

class Events(Base):
    def __init__(self):
        """Constructor."""

    def get(self, name='*', **kwargs):
        url = '/api/events'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_event()
        return Event(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/events'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_event()
        return ParseHelper.toCollection(Event,
                                        FilterHelper.filter(result, kwargs))

class Group(params.Group, Base):
    def __init__(self, group):
        self.superclass = group

    def __new__(cls, group):
        if group is None: return None
        obj = object.__new__(cls)
        obj.__init__(group)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/groups/{group:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{group:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{group:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class Groups(Base):
    def __init__(self):
        """Constructor."""

    def add(self, group):
        url = '/api/groups'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(group))
        return Group(result)

    def get(self, name='*', **kwargs):
        url = '/api/groups'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_group()
        return Group(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/groups'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_group()
        return ParseHelper.toCollection(Group,
                                        FilterHelper.filter(result, kwargs))

class Host(params.Host, Base):
    def __init__(self, host):
        self.superclass = host

    def __new__(cls, host):
        if host is None: return None
        obj = object.__new__(cls)
        obj.__init__(host)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/hosts/{host:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def install(self):
        url = '/api/hosts/{host:id}/install'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def fence(self):
        url = '/api/hosts/{host:id}/fence'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def activate(self):
        url = '/api/hosts/{host:id}/activate'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def deactivate(self):
        url = '/api/hosts/{host:id}/deactivate'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def approve(self):
        url = '/api/hosts/{host:id}/approve'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def iscsilogin(self):
        url = '/api/hosts/{host:id}/iscsilogin'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def iscsidiscover(self):
        url = '/api/hosts/{host:id}/iscsidiscover'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def commitnetconfig(self):
        url = '/api/hosts/{host:id}/commitnetconfig'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def storage(self):
        url = '/api/hosts/{host:id}/storage'

        action = params.Action()
        result = self._getProxy().request(method='GET',
                                          url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def update(self):
        url = '/api/hosts/{host:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{host:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))
        return Host(result)

class Hosts(Base):
    def __init__(self):
        """Constructor."""

    def add(self, host):
        url = '/api/hosts'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(host))
        return Host(result)

    def get(self, name='*', **kwargs):
        url = '/api/hosts'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_host()
        return Host(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/hosts'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_host()
        return ParseHelper.toCollection(Host,
                                        FilterHelper.filter(result, kwargs))

class Network(params.Network, Base):
    def __init__(self, network):
        self.superclass = network

    def __new__(cls, network):
        if network is None: return None
        obj = object.__new__(cls)
        obj.__init__(network)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/networks/{network:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{network:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{network:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def update(self):
        url = '/api/networks/{network:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{network:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))
        return Network(result)

class Networks(Base):
    def __init__(self):
        """Constructor."""

    def add(self, network):
        url = '/api/networks'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(network))
        return Network(result)

    def get(self, name='*', **kwargs):
        url = '/api/networks'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_network()
        return Network(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/networks'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_network()
        return ParseHelper.toCollection(Network,
                                        FilterHelper.filter(result, kwargs))

class Role(params.Role, Base):
    def __init__(self, role):
        self.superclass = role

    def __new__(cls, role):
        if role is None: return None
        obj = object.__new__(cls)
        obj.__init__(role)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/roles/{role:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{role:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{role:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class Roles(Base):
    def __init__(self):
        """Constructor."""

    def add(self, role):
        url = '/api/roles'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(role))
        return Role(result)

    def get(self, name='*', **kwargs):
        url = '/api/roles'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_role()
        return Role(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/roles'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_role()
        return ParseHelper.toCollection(Role,
                                        FilterHelper.filter(result, kwargs))

class StorageDomain(params.StorageDomain, Base):
    def __init__(self, storagedomain):
        self.superclass = storagedomain

    def __new__(cls, storagedomain):
        if storagedomain is None: return None
        obj = object.__new__(cls)
        obj.__init__(storagedomain)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/storagedomains/{storagedomain:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{storagedomain:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{storagedomain:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def update(self):
        url = '/api/storagedomains/{storagedomain:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{storagedomain:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))
        return StorageDomain(result)

class StorageDomains(Base):
    def __init__(self):
        """Constructor."""

    def add(self, storagedomain):
        url = '/api/storagedomains'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(storagedomain))
        return StorageDomain(result)

    def get(self, name='*', **kwargs):
        url = '/api/storagedomains'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_storagedomain()
        return StorageDomain(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/storagedomains'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_storagedomain()
        return ParseHelper.toCollection(StorageDomain,
                                        FilterHelper.filter(result, kwargs))

class Tag(params.Tag, Base):
    def __init__(self, tag):
        self.superclass = tag

    def __new__(cls, tag):
        if tag is None: return None
        obj = object.__new__(cls)
        obj.__init__(tag)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/tags/{tag:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{tag:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{tag:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def update(self):
        url = '/api/tags/{tag:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{tag:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))
        return Tag(result)

class Tags(Base):
    def __init__(self):
        """Constructor."""

    def add(self, tag):
        url = '/api/tags'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(tag))
        return Tag(result)

    def get(self, name='*', **kwargs):
        url = '/api/tags'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_tag()
        return Tag(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/tags'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_tag()
        return ParseHelper.toCollection(Tag,
                                        FilterHelper.filter(result, kwargs))

class Template(params.Template, Base):
    def __init__(self, template):
        self.superclass = template

    def __new__(cls, template):
        if template is None: return None
        obj = object.__new__(cls)
        obj.__init__(template)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/templates/{template:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{template:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{template:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def export(self):
        url = '/api/templates/{template:id}/export'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{template:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def update(self):
        url = '/api/templates/{template:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{template:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))
        return Template(result)

class Templates(Base):
    def __init__(self):
        """Constructor."""

    def add(self, template):
        url = '/api/templates'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(template))
        return Template(result)

    def get(self, name='*', **kwargs):
        url = '/api/templates'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_template()
        return Template(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/templates'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_template()
        return ParseHelper.toCollection(Template,
                                        FilterHelper.filter(result, kwargs))

class User(params.User, Base):
    def __init__(self, user):
        self.superclass = user

    def __new__(cls, user):
        if user is None: return None
        obj = object.__new__(cls)
        obj.__init__(user)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/users/{user:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{user:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{user:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

class Users(Base):
    def __init__(self):
        """Constructor."""

    def add(self, user):
        url = '/api/users'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(user))
        return User(result)

    def get(self, name='*', **kwargs):
        url = '/api/users'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_user()
        return User(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/users'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_user()
        return ParseHelper.toCollection(User,
                                        FilterHelper.filter(result, kwargs))

class VM(params.VM, Base):
    def __init__(self, vm):
        self.superclass = vm

    def __new__(cls, vm):
        if vm is None: return None
        obj = object.__new__(cls)
        obj.__init__(vm)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/vms/{vm:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def shutdown(self):
        url = '/api/vms/{vm:id}/shutdown'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def start(self):
        url = '/api/vms/{vm:id}/start'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def stop(self):
        url = '/api/vms/{vm:id}/stop'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def suspend(self):
        url = '/api/vms/{vm:id}/suspend'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def detach(self):
        url = '/api/vms/{vm:id}/detach'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def export(self):
        url = '/api/vms/{vm:id}/export'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def move(self):
        url = '/api/vms/{vm:id}/move'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def ticket(self):
        url = '/api/vms/{vm:id}/ticket'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def migrate(self):
        url = '/api/vms/{vm:id}/migrate'

        action = params.Action()
        result = self._getProxy().request(method='POST',
                                          url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                          body=ParseHelper.toXml(action))
        return result

    def update(self):
        url = '/api/vms/{vm:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{vm:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))
        return VM(result)

class VmPool(params.VmPool, Base):
    def __init__(self, vmpool):
        self.superclass = vmpool

    def __new__(cls, vmpool):
        if vmpool is None: return None
        obj = object.__new__(cls)
        obj.__init__(vmpool)
        return obj

    def delete(self, force=False, grace_period=False):
        url = '/api/vmpools/{vmpool:id}'

        if ((force or grace_period) is not False):
            action = params.Action(force=force, grace_period=grace_period)
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{vmpool:id}': self.get_id()}),
                                             body=ParseHelper.toXml(action))
        else:
            result = self._getProxy().delete(url=UrlHelper.replace(url, {'{vmpool:id}': self.get_id()}),
                                             headers={'Content-type':None})
        return result

    def update(self):
        url = '/api/vmpools/{vmpool:id}'

        result = self._getProxy().update(url=UrlHelper.replace(url, {'{vmpool:id}': self.get_id()}),
                                         body=ParseHelper.toXml(self.superclass))
        return VmPool(result)

class VmPools(Base):
    def __init__(self):
        """Constructor."""

    def add(self, vmpool):
        url = '/api/vmpools'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(vmpool))
        return VmPool(result)

    def get(self, name='*', **kwargs):
        url = '/api/vmpools'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_vmpool()
        return VmPool(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/vmpools'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_vmpool()
        return ParseHelper.toCollection(VmPool,
                                        FilterHelper.filter(result, kwargs))

class VMs(Base):
    def __init__(self):
        """Constructor."""

    def add(self, vm):
        url = '/api/vms'

        result = self._getProxy().add(url=url,
                                      body=ParseHelper.toXml(vm))
        return VM(result)

    def get(self, name='*', **kwargs):
        url = '/api/vms'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, 'name='+name)).get_vm()
        return VM(FilterHelper.getItem(FilterHelper.filter(result, kwargs)))

    def list(self, query=None, **kwargs):
        '''
        @param query   : oVirt engine dialect query
        @param **kwargs: used to filter collection members if no search capabilities
                         available at given collection resource
        '''

        url='/api/vms'

        result = self._getProxy().get(url=SearchHelper.appendQuery(url, query)).get_vm()
        return ParseHelper.toCollection(VM,
                                        FilterHelper.filter(result, kwargs))

