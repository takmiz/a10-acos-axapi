#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Copyright 2018 A10 Networks
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")


DOCUMENTATION = r'''
module: a10_network_vlan
description:
    - Configure VLAN
short_description: Configures A10 network.vlan
author: A10 Networks 2018 
version_added: 2.4
options:
    state:
        description:
        - State of the object to be created.
        choices:
          - noop
          - present
          - absent
        required: True
    ansible_host:
        description:
        - Host for AXAPI authentication
        required: True
    ansible_username:
        description:
        - Username for AXAPI authentication
        required: True
    ansible_password:
        description:
        - Password for AXAPI authentication
        required: True
    ansible_port:
        description:
        - Port for AXAPI authentication
        required: True
    a10_device_context_id:
        description:
        - Device ID for aVCS configuration
        choices: [1-8]
        required: False
    a10_partition:
        description:
        - Destination/target partition for object/command
        required: False
    oper:
        description:
        - "Field oper"
        required: False
        suboptions:
            ve_num:
                description:
                - "Field ve_num"
            vlan_name:
                description:
                - "Field vlan_name"
            un_tagg_logical_ports:
                description:
                - "Field un_tagg_logical_ports"
            tagg_logical_ports:
                description:
                - "Field tagg_logical_ports"
            vlan_num:
                description:
                - "VLAN number"
            tagg_eth_ports:
                description:
                - "Field tagg_eth_ports"
            is_shared_vlan:
                description:
                - "Field is_shared_vlan"
            un_tagg_eth_ports:
                description:
                - "Field un_tagg_eth_ports"
    traffic_distribution_mode:
        description:
        - "'sip'= sip; 'dip'= dip; 'primary'= primary; 'blade'= blade; 'l4-src-port'= l4-src-port; 'l4-dst-port'= l4-dst-port; "
        required: False
    stats:
        description:
        - "Field stats"
        required: False
        suboptions:
            shared_vlan_partition_switched_counter:
                description:
                - "SVLAN Partition switched counter"
            unknown_unicast_count:
                description:
                - "Unknown Unicast counter"
            broadcast_count:
                description:
                - "Broadcast counter"
            mac_movement_count:
                description:
                - "Mac Movement counter"
            vlan_num:
                description:
                - "VLAN number"
            multicast_count:
                description:
                - "Multicast counter"
            ip_multicast_count:
                description:
                - "IP Multicast counter"
    uuid:
        description:
        - "uuid of the object"
        required: False
    untagged_trunk_list:
        description:
        - "Field untagged_trunk_list"
        required: False
        suboptions:
            untagged_trunk_start:
                description:
                - "Trunk groups"
            untagged_trunk_end:
                description:
                - "Trunk Group"
    untagged_lif:
        description:
        - "Logical tunnel interface (Logical tunnel interface number)"
        required: False
    untagged_eth_list:
        description:
        - "Field untagged_eth_list"
        required: False
        suboptions:
            untagged_ethernet_end:
                description:
                - "Ethernet port"
            untagged_ethernet_start:
                description:
                - "Ethernet port (Interface number)"
    user_tag:
        description:
        - "Customized tag"
        required: False
    name:
        description:
        - "VLAN name"
        required: False
    vlan_num:
        description:
        - "VLAN number"
        required: True
    sampling_enable:
        description:
        - "Field sampling_enable"
        required: False
        suboptions:
            counters1:
                description:
                - "'all'= all; 'broadcast_count'= Broadcast counter; 'multicast_count'= Multicast counter; 'ip_multicast_count'= IP Multicast counter; 'unknown_unicast_count'= Unknown Unicast counter; 'mac_movement_count'= Mac Movement counter; 'shared_vlan_partition_switched_counter'= SVLAN Partition switched counter; "
    tagged_trunk_list:
        description:
        - "Field tagged_trunk_list"
        required: False
        suboptions:
            tagged_trunk_start:
                description:
                - "Trunk groups"
            tagged_trunk_end:
                description:
                - "Trunk Group"
    shared_vlan:
        description:
        - "Configure VLAN as a shared VLAN"
        required: False
    tagged_eth_list:
        description:
        - "Field tagged_eth_list"
        required: False
        suboptions:
            tagged_ethernet_end:
                description:
                - "Ethernet port"
            tagged_ethernet_start:
                description:
                - "Ethernet port (Interface number)"
    ve:
        description:
        - "ve number"
        required: False


'''

EXAMPLES = """
"""

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'supported_by': 'community',
    'status': ['preview']
}

# Hacky way of having access to object properties for evaluation
AVAILABLE_PROPERTIES = ["name","oper","sampling_enable","shared_vlan","stats","tagged_eth_list","tagged_trunk_list","traffic_distribution_mode","untagged_eth_list","untagged_lif","untagged_trunk_list","user_tag","uuid","ve","vlan_num",]

# our imports go at the top so we fail fast.
try:
    from ansible_collections.a10.acos_axapi.plugins.module_utils import errors as a10_ex
    from ansible_collections.a10.acos_axapi.plugins.module_utils.axapi_http import client_factory, session_factory
    from ansible_collections.a10.acos_axapi.plugins.module_utils.kwbl import KW_IN, KW_OUT, translate_blacklist as translateBlacklist

except (ImportError) as ex:
    module.fail_json(msg="Import Error:{0}".format(ex))
except (Exception) as ex:
    module.fail_json(msg="General Exception in Ansible module import:{0}".format(ex))


def get_default_argspec():
    return dict(
        ansible_host=dict(type='str', required=True),
        ansible_username=dict(type='str', required=True),
        ansible_password=dict(type='str', required=True, no_log=True),
        state=dict(type='str', default="present", choices=['noop', 'present', 'absent']),
        ansible_port=dict(type='int', choices=[80, 443], required=True),
        a10_partition=dict(type='dict', name=dict(type='str',), shared=dict(type='str',), required=False, ),
        a10_device_context_id=dict(type='int', choices=[1, 2, 3, 4, 5, 6, 7, 8], required=False, ),
        get_type=dict(type='str', choices=["single", "list", "oper", "stats"]),
    )

def get_argspec():
    rv = get_default_argspec()
    rv.update(dict(
        oper=dict(type='dict', ve_num=dict(type='int', ), vlan_name=dict(type='str', ), un_tagg_logical_ports=dict(type='dict', ports=dict(type='int', )), tagg_logical_ports=dict(type='dict', ports=dict(type='int', )), vlan_num=dict(type='int', required=True, ), tagg_eth_ports=dict(type='dict', ports=dict(type='int', )), is_shared_vlan=dict(type='str', ), un_tagg_eth_ports=dict(type='dict', ports=dict(type='int', ))),
        traffic_distribution_mode=dict(type='str', choices=['sip', 'dip', 'primary', 'blade', 'l4-src-port', 'l4-dst-port']),
        stats=dict(type='dict', shared_vlan_partition_switched_counter=dict(type='str', ), unknown_unicast_count=dict(type='str', ), broadcast_count=dict(type='str', ), mac_movement_count=dict(type='str', ), vlan_num=dict(type='int', required=True, ), multicast_count=dict(type='str', ), ip_multicast_count=dict(type='str', )),
        uuid=dict(type='str', ),
        untagged_trunk_list=dict(type='list', untagged_trunk_start=dict(type='int', ), untagged_trunk_end=dict(type='int', )),
        untagged_lif=dict(type='int', ),
        untagged_eth_list=dict(type='list', untagged_ethernet_end=dict(type='str', ), untagged_ethernet_start=dict(type='str', )),
        user_tag=dict(type='str', ),
        name=dict(type='str', ),
        vlan_num=dict(type='int', required=True, ),
        sampling_enable=dict(type='list', counters1=dict(type='str', choices=['all', 'broadcast_count', 'multicast_count', 'ip_multicast_count', 'unknown_unicast_count', 'mac_movement_count', 'shared_vlan_partition_switched_counter'])),
        tagged_trunk_list=dict(type='list', tagged_trunk_start=dict(type='int', ), tagged_trunk_end=dict(type='int', )),
        shared_vlan=dict(type='bool', ),
        tagged_eth_list=dict(type='list', tagged_ethernet_end=dict(type='str', ), tagged_ethernet_start=dict(type='str', )),
        ve=dict(type='int', )
    ))
   

    return rv

def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/network/vlan/{vlan-num}"

    f_dict = {}
    f_dict["vlan-num"] = module.params["vlan_num"]

    return url_base.format(**f_dict)

def oper_url(module):
    """Return the URL for operational data of an existing resource"""
    partial_url = existing_url(module)
    return partial_url + "/oper"

def stats_url(module):
    """Return the URL for statistical data of and existing resource"""
    partial_url = existing_url(module)
    return partial_url + "/stats"

def list_url(module):
    """Return the URL for a list of resources"""
    ret = existing_url(module)
    return ret[0:ret.rfind('/')]

def get(module):
    return module.client.get(existing_url(module))

def get_list(module):
    return module.client.get(list_url(module))

def get_oper(module):
    if module.params.get("oper"):
        query_params = {}
        for k,v in module.params["oper"].items():
            query_params[k.replace('_', '-')] = v 
        return module.client.get(oper_url(module),
                                 params=query_params)
    return module.client.get(oper_url(module))

def get_stats(module):
    if module.params.get("stats"):
        query_params = {}
        for k,v in module.params["stats"].items():
            query_params[k.replace('_', '-')] = v
        return module.client.get(stats_url(module),
                                 params=query_params)
    return module.client.get(stats_url(module))

def exists(module):
    try:
        return get(module)
    except a10_ex.NotFound:
        return None

def _to_axapi(key):
    return translateBlacklist(key, KW_OUT).replace("_", "-")

def _build_dict_from_param(param):
    rv = {}

    for k,v in param.items():
        hk = _to_axapi(k)
        if isinstance(v, dict):
            v_dict = _build_dict_from_param(v)
            rv[hk] = v_dict
        elif isinstance(v, list):
            nv = [_build_dict_from_param(x) for x in v]
            rv[hk] = nv
        else:
            rv[hk] = v

    return rv

def build_envelope(title, data):
    return {
        title: data
    }

def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/network/vlan/{vlan-num}"

    f_dict = {}
    f_dict["vlan-num"] = ""

    return url_base.format(**f_dict)

def validate(params):
    # Ensure that params contains all the keys.
    requires_one_of = sorted([])
    present_keys = sorted([x for x in requires_one_of if x in params and params.get(x) is not None])
    
    errors = []
    marg = []
    
    if not len(requires_one_of):
        return REQUIRED_VALID

    if len(present_keys) == 0:
        rc,msg = REQUIRED_NOT_SET
        marg = requires_one_of
    elif requires_one_of == present_keys:
        rc,msg = REQUIRED_MUTEX
        marg = present_keys
    else:
        rc,msg = REQUIRED_VALID
    
    if not rc:
        errors.append(msg.format(", ".join(marg)))
    
    return rc,errors

def build_json(title, module):
    rv = {}

    for x in AVAILABLE_PROPERTIES:
        v = module.params.get(x)
        if v is not None:
            rx = _to_axapi(x)

            if isinstance(v, dict):
                nv = _build_dict_from_param(v)
                rv[rx] = nv
            elif isinstance(v, list):
                nv = [_build_dict_from_param(x) for x in v]
                rv[rx] = nv
            else:
                rv[rx] = module.params[x]

    return build_envelope(title, rv)

def report_changes(module, result, existing_config, payload):
    if existing_config:
        for k, v in payload["vlan"].items():
            if isinstance(v, str):
                if v.lower() == "true":
                    v = 1
                else:
                    if v.lower() == "false":
                        v = 0
            elif k not in payload:
               break
            else:
                if existing_config["vlan"][k] != v:
                    if result["changed"] != True:
                        result["changed"] = True
                    existing_config["vlan"][k] = v
            result.update(**existing_config)
    else:
        result.update(**payload)
    return result

def create(module, result, payload):
    try:
        post_result = module.client.post(new_url(module), payload)
        if post_result:
            result.update(**post_result)
        result["changed"] = True
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result

def update(module, result, existing_config, payload):
    try:
        post_result = module.client.post(existing_url(module), payload)
        if post_result:
            result.update(**post_result)
        if post_result == existing_config:
            result["changed"] = False
        else:
            result["changed"] = True
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result

def present(module, result, existing_config):
    payload = build_json("vlan", module)
    changed_config = report_changes(module, result, existing_config, payload)
    if module.check_mode:
        return changed_config
    elif not existing_config:
        return create(module, result, payload)
    elif existing_config and not changed_config.get('changed'):
        return update(module, result, existing_config, payload)
    else:
        result["changed"] = True
        return result

def delete(module, result):
    try:
        module.client.delete(existing_url(module))
        result["changed"] = True
    except a10_ex.NotFound:
        result["changed"] = False
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result

def absent(module, result, existing_config):
    if module.check_mode:
        if existing_config:
            result["changed"] = True
            return result
        else:
            result["changed"] = False
            return result
    else:
        return delete(module, result)

def replace(module, result, existing_config, payload):
    try:
        post_result = module.client.put(existing_url(module), payload)
        if post_result:
            result.update(**post_result)
        if post_result == existing_config:
            result["changed"] = False
        else:
            result["changed"] = True
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
    return result

def run_command(module):
    run_errors = []

    result = dict(
        changed=False,
        original_message="",
        message="",
        result={}
    )

    state = module.params["state"]
    ansible_host = module.params["ansible_host"]
    ansible_username = module.params["ansible_username"]
    ansible_password = module.params["ansible_password"]
    ansible_port = module.params["ansible_port"]
    a10_partition = module.params["a10_partition"]
    a10_device_context_id = module.params["a10_device_context_id"]

    if ansible_port == 80:
        protocol = "http"
    elif ansible_port == 443:
        protocol = "https"

    valid = True

    if state == 'present':
        valid, validation_errors = validate(module.params)
        for ve in validation_errors:
            run_errors.append(ve)
    
    if not valid:
        err_msg = "\n".join(run_errors)
        result["messages"] = "Validation failure: " + str(run_errors)
        module.fail_json(msg=err_msg, **result)

    module.client = client_factory(ansible_host, ansible_port, protocol, ansible_username, ansible_password)
    
    if a10_partition:
        module.client.activate_partition(a10_partition)

    if a10_device_context_id:
        module.client.change_context(a10_device_context_id)

    existing_config = exists(module)
    
    if state == 'present':
        result = present(module, result, existing_config)

    elif state == 'absent':
        result = absent(module, result, existing_config)
    
    elif state == 'noop':
        if module.params.get("get_type") == "single":
            result["result"] = get(module)
        elif module.params.get("get_type") == "list":
            result["result"] = get_list(module)
        elif module.params.get("get_type") == "oper":
            result["result"] = get_oper(module)
        elif module.params.get("get_type") == "stats":
            result["result"] = get_stats(module)
    module.client.session.close()
    return result

def main():
    module = AnsibleModule(argument_spec=get_argspec(), supports_check_mode=True)
    result = run_command(module)
    module.exit_json(**result)

# standard ansible module imports
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *

if __name__ == '__main__':
    main()