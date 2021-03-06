#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Copyright 2018 A10 Networks
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")

DOCUMENTATION = r'''
module: a10_interface_loopback_isis
description:
    - ISIS
short_description: Configures A10 interface.loopback.isis
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
    loopback_ifnum:
        description:
        - Key to identify parent object    priority_list:
        description:
        - "Field priority_list"
        required: False
        suboptions:
            priority:
                description:
                - "Set priority for Designated Router election (Priority value)"
            level:
                description:
                - "'level-1'= Specify priority for level-1 routing; 'level-2'= Specify priority
          for level-2 routing;"
    padding:
        description:
        - "Add padding to IS-IS hello packets"
        required: False
    hello_interval_minimal_list:
        description:
        - "Field hello_interval_minimal_list"
        required: False
        suboptions:
            hello_interval_minimal:
                description:
                - "Set Hello holdtime 1 second, interval depends on multiplier"
            level:
                description:
                - "'level-1'= Specify hello-interval for level-1 IIHs; 'level-2'= Specify hello-
          interval for level-2 IIHs;"
    mesh_group:
        description:
        - "Field mesh_group"
        required: False
        suboptions:
            value:
                description:
                - "Mesh group number"
            blocked:
                description:
                - "Block LSPs on this interface"
    uuid:
        description:
        - "uuid of the object"
        required: False
    authentication:
        description:
        - "Field authentication"
        required: False
        suboptions:
            send_only_list:
                description:
                - "Field send_only_list"
            mode_list:
                description:
                - "Field mode_list"
            key_chain_list:
                description:
                - "Field key_chain_list"
    csnp_interval_list:
        description:
        - "Field csnp_interval_list"
        required: False
        suboptions:
            csnp_interval:
                description:
                - "Set CSNP interval in seconds (CSNP interval value)"
            level:
                description:
                - "'level-1'= Speficy interval for level-1 CSNPs; 'level-2'= Specify interval for
          level-2 CSNPs;"
    retransmit_interval:
        description:
        - "Set per-LSP retransmission interval (Interval between retransmissions of the
          same LSP (seconds))"
        required: False
    password_list:
        description:
        - "Field password_list"
        required: False
        suboptions:
            password:
                description:
                - "Configure the authentication password for interface"
            level:
                description:
                - "'level-1'= Specify password for level-1 PDUs; 'level-2'= Specify password for
          level-2 PDUs;"
    bfd_cfg:
        description:
        - "Field bfd_cfg"
        required: False
        suboptions:
            disable:
                description:
                - "Disable BFD"
            bfd:
                description:
                - "Bidirectional Forwarding Detection (BFD)"
    wide_metric_list:
        description:
        - "Field wide_metric_list"
        required: False
        suboptions:
            wide_metric:
                description:
                - "Configure the wide metric for interface"
            level:
                description:
                - "'level-1'= Apply metric to level-1 links; 'level-2'= Apply metric to level-2
          links;"
    hello_interval_list:
        description:
        - "Field hello_interval_list"
        required: False
        suboptions:
            hello_interval:
                description:
                - "Set Hello interval in seconds (Hello interval value)"
            level:
                description:
                - "'level-1'= Specify hello-interval for level-1 IIHs; 'level-2'= Specify hello-
          interval for level-2 IIHs;"
    circuit_type:
        description:
        - "'level-1'= Level-1 only adjacencies are formed; 'level-1-2'= Level-1-2
          adjacencies are formed; 'level-2-only'= Level-2 only adjacencies are formed;"
        required: False
    hello_multiplier_list:
        description:
        - "Field hello_multiplier_list"
        required: False
        suboptions:
            hello_multiplier:
                description:
                - "Set multiplier for Hello holding time (Hello multiplier value)"
            level:
                description:
                - "'level-1'= Specify hello multiplier for level-1 IIHs; 'level-2'= Specify hello
          multiplier for level-2 IIHs;"
    metric_list:
        description:
        - "Field metric_list"
        required: False
        suboptions:
            metric:
                description:
                - "Configure the metric for interface (Default metric)"
            level:
                description:
                - "'level-1'= Apply metric to level-1 links; 'level-2'= Apply metric to level-2
          links;"
    lsp_interval:
        description:
        - "Set LSP transmission interval (LSP transmission interval (milliseconds))"
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
AVAILABLE_PROPERTIES = [
    "authentication",
    "bfd_cfg",
    "circuit_type",
    "csnp_interval_list",
    "hello_interval_list",
    "hello_interval_minimal_list",
    "hello_multiplier_list",
    "lsp_interval",
    "mesh_group",
    "metric_list",
    "padding",
    "password_list",
    "priority_list",
    "retransmit_interval",
    "uuid",
    "wide_metric_list",
]

from ansible_collections.a10.acos_axapi.plugins.module_utils import \
    errors as a10_ex
from ansible_collections.a10.acos_axapi.plugins.module_utils.axapi_http import \
    client_factory
from ansible_collections.a10.acos_axapi.plugins.module_utils.kwbl import \
    KW_OUT, translate_blacklist as translateBlacklist


def get_default_argspec():
    return dict(
        ansible_host=dict(type='str', required=True),
        ansible_username=dict(type='str', required=True),
        ansible_password=dict(type='str', required=True, no_log=True),
        state=dict(type='str',
                   default="present",
                   choices=['noop', 'present', 'absent']),
        ansible_port=dict(type='int', choices=[80, 443], required=True),
        a10_partition=dict(
            type='dict',
            name=dict(type='str', ),
            shared=dict(type='str', ),
            required=False,
        ),
        a10_device_context_id=dict(
            type='int',
            choices=[1, 2, 3, 4, 5, 6, 7, 8],
            required=False,
        ),
        get_type=dict(type='str', choices=["single", "list", "oper", "stats"]),
    )


def get_argspec():
    rv = get_default_argspec()
    rv.update({
        'priority_list': {
            'type': 'list',
            'priority': {
                'type': 'int',
            },
            'level': {
                'type': 'str',
                'choices': ['level-1', 'level-2']
            }
        },
        'padding': {
            'type': 'bool',
        },
        'hello_interval_minimal_list': {
            'type': 'list',
            'hello_interval_minimal': {
                'type': 'bool',
            },
            'level': {
                'type': 'str',
                'choices': ['level-1', 'level-2']
            }
        },
        'mesh_group': {
            'type': 'dict',
            'value': {
                'type': 'int',
            },
            'blocked': {
                'type': 'bool',
            }
        },
        'uuid': {
            'type': 'str',
        },
        'authentication': {
            'type': 'dict',
            'send_only_list': {
                'type': 'list',
                'send_only': {
                    'type': 'bool',
                },
                'level': {
                    'type': 'str',
                    'choices': ['level-1', 'level-2']
                }
            },
            'mode_list': {
                'type': 'list',
                'mode': {
                    'type': 'str',
                    'choices': ['md5']
                },
                'level': {
                    'type': 'str',
                    'choices': ['level-1', 'level-2']
                }
            },
            'key_chain_list': {
                'type': 'list',
                'key_chain': {
                    'type': 'str',
                },
                'level': {
                    'type': 'str',
                    'choices': ['level-1', 'level-2']
                }
            }
        },
        'csnp_interval_list': {
            'type': 'list',
            'csnp_interval': {
                'type': 'int',
            },
            'level': {
                'type': 'str',
                'choices': ['level-1', 'level-2']
            }
        },
        'retransmit_interval': {
            'type': 'int',
        },
        'password_list': {
            'type': 'list',
            'password': {
                'type': 'str',
            },
            'level': {
                'type': 'str',
                'choices': ['level-1', 'level-2']
            }
        },
        'bfd_cfg': {
            'type': 'dict',
            'disable': {
                'type': 'bool',
            },
            'bfd': {
                'type': 'bool',
            }
        },
        'wide_metric_list': {
            'type': 'list',
            'wide_metric': {
                'type': 'int',
            },
            'level': {
                'type': 'str',
                'choices': ['level-1', 'level-2']
            }
        },
        'hello_interval_list': {
            'type': 'list',
            'hello_interval': {
                'type': 'int',
            },
            'level': {
                'type': 'str',
                'choices': ['level-1', 'level-2']
            }
        },
        'circuit_type': {
            'type': 'str',
            'choices': ['level-1', 'level-1-2', 'level-2-only']
        },
        'hello_multiplier_list': {
            'type': 'list',
            'hello_multiplier': {
                'type': 'int',
            },
            'level': {
                'type': 'str',
                'choices': ['level-1', 'level-2']
            }
        },
        'metric_list': {
            'type': 'list',
            'metric': {
                'type': 'int',
            },
            'level': {
                'type': 'str',
                'choices': ['level-1', 'level-2']
            }
        },
        'lsp_interval': {
            'type': 'int',
        }
    })
    # Parent keys
    rv.update(dict(loopback_ifnum=dict(type='str', required=True), ))
    return rv


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/interface/loopback/{loopback_ifnum}/isis"

    f_dict = {}
    f_dict["loopback_ifnum"] = module.params["loopback_ifnum"]

    return url_base.format(**f_dict)


def list_url(module):
    """Return the URL for a list of resources"""
    ret = existing_url(module)
    return ret[0:ret.rfind('/')]


def get(module):
    return module.client.get(existing_url(module))


def get_list(module):
    return module.client.get(list_url(module))


def exists(module):
    try:
        return get(module)
    except a10_ex.NotFound:
        return None


def _to_axapi(key):
    return translateBlacklist(key, KW_OUT).replace("_", "-")


def _build_dict_from_param(param):
    rv = {}

    for k, v in param.items():
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
    return {title: data}


def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/interface/loopback/{loopback_ifnum}/isis"

    f_dict = {}
    f_dict["loopback_ifnum"] = module.params["loopback_ifnum"]

    return url_base.format(**f_dict)


def validate(params):
    # Ensure that params contains all the keys.
    requires_one_of = sorted([])
    present_keys = sorted([
        x for x in requires_one_of if x in params and params.get(x) is not None
    ])

    errors = []
    marg = []

    if not len(requires_one_of):
        return REQUIRED_VALID

    if len(present_keys) == 0:
        rc, msg = REQUIRED_NOT_SET
        marg = requires_one_of
    elif requires_one_of == present_keys:
        rc, msg = REQUIRED_MUTEX
        marg = present_keys
    else:
        rc, msg = REQUIRED_VALID

    if not rc:
        errors.append(msg.format(", ".join(marg)))

    return rc, errors


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
        for k, v in payload["isis"].items():
            if isinstance(v, str):
                if v.lower() == "true":
                    v = 1
                else:
                    if v.lower() == "false":
                        v = 0
            elif k not in payload:
                break
            else:
                if existing_config["isis"][k] != v:
                    if result["changed"] is not True:
                        result["changed"] = True
                    existing_config["isis"][k] = v
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
    payload = build_json("isis", module)
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

    result = dict(changed=False, original_message="", message="", result={})

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

    module.client = client_factory(ansible_host, ansible_port, protocol,
                                   ansible_username, ansible_password)

    if a10_partition:
        module.client.activate_partition(a10_partition)

    if a10_device_context_id:
        module.client.change_context(a10_device_context_id)

    existing_config = exists(module)

    if state == 'present':
        result = present(module, result, existing_config)

    if state == 'absent':
        result = absent(module, result, existing_config)

    if state == 'noop':
        if module.params.get("get_type") == "single":
            result["result"] = get(module)
        elif module.params.get("get_type") == "list":
            result["result"] = get_list(module)
    module.client.session.close()
    return result


def main():
    module = AnsibleModule(argument_spec=get_argspec(),
                           supports_check_mode=True)
    result = run_command(module)
    module.exit_json(**result)


# standard ansible module imports
from ansible.module_utils.basic import AnsibleModule

if __name__ == '__main__':
    main()
