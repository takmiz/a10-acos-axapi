#!/usr/bin/python

# Copyright 2018 A10 Networks
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")


DOCUMENTATION = ''' 
module: a10_slb_virtual_server_port
description:
    - Virtual Port
short_description: Configures A10 slb.virtual-server.port
author: A10 Networks 2018 
version_added: 2.4
options:
    state:
        description:
        - State of the object to be created.
        choices:
        - present
        - absent
        required: True
    a10_host:
        description:
        - Host for AXAPI authentication
        required: True
    a10_username:
        description:
        - Username for AXAPI authentication
        required: True
    a10_password:
        description:
        - Password for AXAPI authentication
        required: True
    virtual_server:
        description:
        - SLB Virtual Server to Create Port On 
    ha_conn_mirror:
        description:
        - "Enable for HA Conn sync"
        required: False
    protocol:
        description:
        - "'tcp'= TCP LB service; 'udp'= UDP Port; 'others'= for no tcp/udp protocol, do IP load balancing; 'diameter'= diameter port; 'dns-tcp'= DNS service over TCP; 'dns-udp'= DNS service over UDP; 'fast-http'= Fast HTTP Port; 'fix'= FIX Port; 'ftp'= File Transfer Protocol Port; 'ftp-proxy'= ftp proxy port; 'http'= HTTP Port; 'https'= HTTPS port; 'http2'= [Deprecated] HTTP2 Port; 'http2s'= [Deprecated] HTTP2 SSL port; 'imap'= imap proxy port; 'mlb'= Message based load balancing; 'mms'= Microsoft Multimedia Service Port; 'mysql'= mssql port; 'mssql'= mssql; 'pop3'= pop3 proxy port; 'radius'= RADIUS Port; 'rtsp'= Real Time Streaming Protocol Port; 'sip'= Session initiation protocol over UDP; 'sip-tcp'= Session initiation protocol over TCP; 'sips'= Session initiation protocol over TLS; 'smpp-tcp'= SMPP service over TCP; 'spdy'= spdy port; 'spdys'= spdys port; 'smtp'= SMTP Port; 'ssl-proxy'= Generic SSL proxy; 'ssli'= SSL insight; 'tcp-proxy'= Generic TCP proxy; 'tftp'= TFTP Port; 'fast-fix'= Fast FIX port; "
        required: True
    precedence:
        description:
        - "Set auto NAT pool as higher precedence for source NAT"
        required: False
    port_translation:
        description:
        - "Enable port translation under no-dest-nat"
        required: False
    template_reqmod_icap:
        description:
        - "ICAP reqmod template (reqmod-icap template name)"
        required: False
    acl_name_list:
        description:
        - "Field acl_name_list"
        required: False
        suboptions:
            acl_name:
                description:
                - "Apply an access list name (Named Access List)"
            acl_name_src_nat_pool:
                description:
                - "Policy based Source NAT (NAT Pool or Pool Group)"
            acl_name_seq_num:
                description:
                - "Specify ACL precedence (sequence-number)"
    stats_data_action:
        description:
        - "'stats-data-enable'= Enable statistical data collection for virtual port; 'stats-data-disable'= Disable statistical data collection for virtual port; "
        required: False
    template_connection_reuse:
        description:
        - "Connection Reuse Template (Connection Reuse Template Name)"
        required: False
    uuid:
        description:
        - "uuid of the object"
        required: False
    template_tcp_shared:
        description:
        - "TCP Template Name"
        required: False
    template_tcp:
        description:
        - "TCP Template Name"
        required: False
    template_persist_destination_ip:
        description:
        - "Destination IP persistence (Destination IP persistence template name)"
        required: False
    when_down:
        description:
        - "Use alternate virtual port when down"
        required: False
    template_client_ssl_shared:
        description:
        - "Client SSL Template Name"
        required: False
    persist_type:
        description:
        - "'src-dst-ip-swap-persist'= Create persist session after source IP and destination IP swap; 'use-src-ip-for-dst-persist'= Use the source IP to create a destination persist session; 'use-dst-ip-for-src-persist'= Use the destination IP to create source IP persist session; "
        required: False
    use_rcv_hop_for_resp:
        description:
        - "Use receive hop for response to client(For packets on default-vlan, also config 'vlan-global enable-def-vlan-l2-forwarding'.)"
        required: False
    scaleout_bucket_count:
        description:
        - "Number of traffic buckets"
        required: False
    req_fail:
        description:
        - "Use alternate virtual port when L7 request fail"
        required: False
    no_dest_nat:
        description:
        - "Disable destination NAT, this option only supports in wildcard VIP or when a connection is operated in SSLi + EP mode"
        required: False
    name:
        description:
        - "SLB Virtual Service Name"
        required: False
    template_policy:
        description:
        - "Policy Template (Policy template name)"
        required: False
    user_tag:
        description:
        - "Customized tag"
        required: False
    template_diameter:
        description:
        - "Diameter Template (diameter template name)"
        required: False
    sampling_enable:
        description:
        - "Field sampling_enable"
        required: False
        suboptions:
            counters1:
                description:
                - "'all'= all; 'curr_conn'= Current established connections; 'total_l4_conn'= Total L4 connections established; 'total_l7_conn'= Total L7 connections established; 'total_tcp_conn'= Total TCP connections established; 'total_conn'= Total connections established; 'total_fwd_bytes'= Bytes processed in forward direction; 'total_fwd_pkts'= Packets processed in forward direction; 'total_rev_bytes'= Bytes processed in reverse direction; 'total_rev_pkts'= Packets processed in reverse direction; 'total_dns_pkts'= Total DNS packets processed; 'total_mf_dns_pkts'= Total MF DNS packets; 'es_total_failure_actions'= Total failure actions; 'compression_bytes_before'= Data into compression engine; 'compression_bytes_after'= Data out of compression engine; 'compression_hit'= Number of requests compressed; 'compression_miss'= Number of requests NOT compressed; 'compression_miss_no_client'= Compression miss no client; 'compression_miss_template_exclusion'= Compression miss template exclusion; 'curr_req'= Current requests; 'total_req'= Total requests; 'total_req_succ'= Total successful requests; 'peak_conn'= Peak connections; 'curr_conn_rate'= Current connection rate; 'last_rsp_time'= Last response time; 'fastest_rsp_time'= Fastest response time; 'slowest_rsp_time'= Slowest response time; 'loc_permit'= Geo-location Permit count; 'loc_deny'= Geo-location Deny count; 'loc_conn'= Geo-location Connection count; 'curr_ssl_conn'= Current SSL connections; 'total_ssl_conn'= Total SSL connections; 'backend-time-to-first-byte'= Backend Time from Request to Response First Byte; 'backend-time-to-last-byte'= Backend Time from Request to Response Last Byte; 'in-latency'= Request Latency at Thunder; 'out-latency'= Response Latency at Thunder; 'total_fwd_bytes_out'= Bytes processed in forward direction (outbound); 'total_fwd_pkts_out'= Packets processed in forward direction (outbound); 'total_rev_bytes_out'= Bytes processed in reverse direction (outbound); 'total_rev_pkts_out'= Packets processed in reverse direction (outbound); "
    template_ssli:
        description:
        - "SSLi template (SSLi Template Name)"
        required: False
    template_smpp:
        description:
        - "SMPP template"
        required: False
    no_logging:
        description:
        - "Do not log connection over limit event"
        required: False
    reset_on_server_selection_fail:
        description:
        - "Send client reset when server selection fails"
        required: False
    waf_template:
        description:
        - "WAF template (WAF Template Name)"
        required: False
    ipinip:
        description:
        - "Enable IP in IP"
        required: False
    no_auto_up_on_aflex:
        description:
        - "Don't automatically mark vport up when aFleX is bound"
        required: False
    rate:
        description:
        - "Specify the log message rate"
        required: False
    gslb_enable:
        description:
        - "Enable Global Server Load Balancing"
        required: False
    template_persist_ssl_sid:
        description:
        - "SSL session ID persistence (Source IP Persistence Config name)"
        required: False
    template_dns:
        description:
        - "DNS template (DNS template name)"
        required: False
    template_sip:
        description:
        - "SIP template"
        required: False
    template_dblb:
        description:
        - "DBLB Template (DBLB template name)"
        required: False
    shared_partition_server_ssl_template:
        description:
        - "Reference a SSL Server template from shared partition"
        required: False
    template_client_ssl:
        description:
        - "Client SSL Template Name"
        required: False
    enable_playerid_check:
        description:
        - "Enable playerid checks on UDP packets once the AX is in active mode"
        required: False
    service_group:
        description:
        - "Bind a Service Group to this Virtual Server (Service Group Name)"
        required: False
    template_fix:
        description:
        - "FIX template (FIX Template Name)"
        required: False
    shared_partition_udp:
        description:
        - "Reference a UDP template from shared partition"
        required: False
    syn_cookie:
        description:
        - "Enable syn-cookie"
        required: False
    alternate_port:
        description:
        - "Alternate Virtual Port"
        required: False
    template_cache:
        description:
        - "RAM caching template (Cache Template Name)"
        required: False
    rtp_sip_call_id_match:
        description:
        - "rtp traffic try to match the real server of sip smp call-id session"
        required: False
    template_scaleout:
        description:
        - "Scaleout template (Scaleout template name)"
        required: False
    template_ftp:
        description:
        - "FTP port template (Ftp template name)"
        required: False
    serv_sel_fail:
        description:
        - "Use alternate virtual port when server selection failure"
        required: False
    range:
        description:
        - "Virtual Port range (Virtual Port range value)"
        required: False
    action:
        description:
        - "'enable'= Enable; 'disable'= Disable; "
        required: False
    shared_partition_client_ssl_template:
        description:
        - "Reference a Client SSL template from shared partition"
        required: False
    view:
        description:
        - "Specify a GSLB View (ID)"
        required: False
    template_persist_source_ip:
        description:
        - "Source IP persistence (Source IP persistence template name)"
        required: False
    template_dynamic_service:
        description:
        - "Dynamic Service Template (dynamic-service template name)"
        required: False
    use_cgnv6:
        description:
        - "Follow CGNv6 source NAT configuration"
        required: False
    template_persist_cookie:
        description:
        - "Cookie persistence (Cookie persistence template name)"
        required: False
    template_virtual_port:
        description:
        - "Virtual port template (Virtual port template name)"
        required: False
    conn_limit:
        description:
        - "Connection Limit"
        required: False
    trunk_fwd:
        description:
        - "Trunk interface number"
        required: False
    template_udp_shared:
        description:
        - "UDP Template Name"
        required: False
    pool:
        description:
        - "Specify NAT pool or pool group"
        required: False
    snat_on_vip:
        description:
        - "Enable source NAT traffic against VIP"
        required: False
    shared_partition_tcp:
        description:
        - "Reference a tcp template from shared partition"
        required: False
    template_tcp_proxy_server:
        description:
        - "TCP Proxy Config Server (TCP Proxy Config name)"
        required: False
    shared_partition_http_template:
        description:
        - "Reference a HTTP template from shared partition"
        required: False
    template_external_service:
        description:
        - "External service template (external-service template name)"
        required: False
    template_udp:
        description:
        - "L4 UDP Template"
        required: False
    force_routing_mode:
        description:
        - "Force routing mode"
        required: False
    template_file_inspection:
        description:
        - "File Inspection service template (file-inspection template name)"
        required: False
    when_down_protocol2:
        description:
        - "Use alternate virtual port when down"
        required: False
    def_selection_if_pref_failed:
        description:
        - "'def-selection-if-pref-failed'= Use default server selection method if prefer method failed; 'def-selection-if-pref-failed-disable'= Stop using default server selection method if prefer method failed; "
        required: False
    template_smtp:
        description:
        - "SMTP Template (SMTP Config Name)"
        required: False
    redirect_to_https:
        description:
        - "Redirect HTTP to HTTPS"
        required: False
    alt_protocol2:
        description:
        - "'tcp'= TCP LB service; "
        required: False
    alt_protocol1:
        description:
        - "'http'= HTTP Port; "
        required: False
    message_switching:
        description:
        - "Message switching"
        required: False
    template_imap_pop3:
        description:
        - "IMAP/POP3 Template (IMAP/POP3 Config Name)"
        required: False
    scaleout_device_group:
        description:
        - "Device group id"
        required: False
    l7_hardware_assist:
        description:
        - "FPGA assist L7 packet parsing"
        required: False
    template_http_policy:
        description:
        - "http-policy template (http-policy template name)"
        required: False
    reset:
        description:
        - "Send client reset when connection number over limit"
        required: False
    use_alternate_port:
        description:
        - "Use alternate virtual port"
        required: False
    acl_id_list:
        description:
        - "Field acl_id_list"
        required: False
        suboptions:
            acl_id_seq_num:
                description:
                - "Specify ACL precedence (sequence-number)"
            acl_id:
                description:
                - "ACL id VPORT"
            acl_id_src_nat_pool:
                description:
                - "Policy based Source NAT (NAT Pool or Pool Group)"
    trunk_rev:
        description:
        - "Trunk interface number"
        required: False
    eth_fwd:
        description:
        - "Ethernet interface number"
        required: False
    template_respmod_icap:
        description:
        - "ICAP respmod service template (respmod-icap template name)"
        required: False
    template_server_ssl_shared:
        description:
        - "Server SSL Template Name"
        required: False
    use_default_if_no_server:
        description:
        - "Use default forwarding if server selection failed"
        required: False
    auto:
        description:
        - "Configure auto NAT for the vport"
        required: False
    aflex_scripts:
        description:
        - "Field aflex_scripts"
        required: False
        suboptions:
            aflex:
                description:
                - "Bind aFleX Script to the Virtual Port (aFleX Script Name)"
    template_http_shared:
        description:
        - "HTTP Template Name"
        required: False
    template_server_ssl:
        description:
        - "Server Side SSL Template Name"
        required: False
    alternate_port_number:
        description:
        - "Virtual Port"
        required: False
    port_number:
        description:
        - "Port"
        required: True
    template_tcp_proxy_client:
        description:
        - "TCP Proxy Config Client (TCP Proxy Config name)"
        required: False
    template_tcp_proxy:
        description:
        - "TCP Proxy Template Name"
        required: False
    extended_stats:
        description:
        - "Enable extended statistics on virtual port"
        required: False
    template_http:
        description:
        - "HTTP Template Name"
        required: False
    expand:
        description:
        - "expand syn-cookie with timestamp and wscale"
        required: False
    skip_rev_hash:
        description:
        - "Skip rev tuple hash insertion"
        required: False
    on_syn:
        description:
        - "Enable for HA Conn sync for l4 tcp sessions on SYN"
        required: False
    clientip_sticky_nat:
        description:
        - "Prefer to use same source NAT address for a client"
        required: False
    secs:
        description:
        - "Specify the interval in seconds"
        required: False
    auth_cfg:
        description:
        - "Field auth_cfg"
        required: False
        suboptions:
            aaa_policy:
                description:
                - "Specify AAA policy name to bind to the virtual port"
    eth_rev:
        description:
        - "Ethernet interface number"
        required: False

'''

EXAMPLES = ''' 
'''

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'supported_by': 'community',
    'status': ['preview']
}

# Hacky way of having access to object properties for evaluation
AVAILABLE_PROPERTIES = ["acl_id_list","acl_name_list","action","aflex_scripts","alt_protocol1","alt_protocol2","alternate_port","alternate_port_number","auth_cfg","auto","clientip_sticky_nat","conn_limit","def_selection_if_pref_failed","enable_playerid_check","eth_fwd","eth_rev","expand","extended_stats","force_routing_mode","gslb_enable","ha_conn_mirror","ipinip","l7_hardware_assist","message_switching","name","no_auto_up_on_aflex","no_dest_nat","no_logging","on_syn","persist_type","pool","port_number","port_translation","precedence","protocol","range","rate","redirect_to_https","req_fail","reset","reset_on_server_selection_fail","rtp_sip_call_id_match","sampling_enable","scaleout_bucket_count","scaleout_device_group","secs","serv_sel_fail","service_group","shared_partition_client_ssl_template","shared_partition_http_template","shared_partition_server_ssl_template","shared_partition_tcp","shared_partition_udp","skip_rev_hash","snat_on_vip","stats_data_action","syn_cookie","template_cache","template_client_ssl","template_client_ssl_shared","template_connection_reuse","template_dblb","template_diameter","template_dns","template_dynamic_service","template_external_service","template_file_inspection","template_fix","template_ftp","template_http","template_http_policy","template_http_shared","template_imap_pop3","template_persist_cookie","template_persist_destination_ip","template_persist_source_ip","template_persist_ssl_sid","template_policy","template_reqmod_icap","template_respmod_icap","template_scaleout","template_server_ssl","template_server_ssl_shared","template_sip","template_smpp","template_smtp","template_ssli","template_tcp","template_tcp_proxy","template_tcp_proxy_client","template_tcp_proxy_server","template_tcp_shared","template_udp","template_udp_shared","template_virtual_port","trunk_fwd","trunk_rev","use_alternate_port","use_cgnv6","use_default_if_no_server","use_rcv_hop_for_resp","user_tag","uuid","view","waf_template","when_down","when_down_protocol2",]

# our imports go at the top so we fail fast.
try:
    from a10_ansible import errors as a10_ex
    from a10_ansible.axapi_http import client_factory, session_factory
    from a10_ansible.kwbl import KW_IN, KW_OUT, translate_blacklist as translateBlacklist

except (ImportError) as ex:
    module.fail_json(msg="Import Error:{0}".format(ex))
except (Exception) as ex:
    module.fail_json(msg="General Exception in Ansible module import:{0}".format(ex))


def get_default_argspec():
    return dict(
        a10_host=dict(type='str', required=True),
        a10_username=dict(type='str', required=True),
        a10_password=dict(type='str', required=True, no_log=True),
        state=dict(type='str', default="present", choices=["present", "absent"])
    )

def get_argspec():
    rv = get_default_argspec()
    rv.update(dict(
        virtual_server=dict(type='str', required=True),
        ha_conn_mirror=dict(type='bool',),
        protocol=dict(type='str',required=True,choices=['tcp','udp','others','diameter','dns-tcp','dns-udp','fast-http','fix','ftp','ftp-proxy','http','https','http2','http2s','imap','mlb','mms','mysql','mssql','pop3','radius','rtsp','sip','sip-tcp','sips','smpp-tcp','spdy','spdys','smtp','ssl-proxy','ssli','tcp-proxy','tftp','fast-fix']),
        precedence=dict(type='bool',),
        port_translation=dict(type='bool',),
        template_reqmod_icap=dict(type='str',),
        acl_name_list=dict(type='list',acl_name=dict(type='str',),acl_name_src_nat_pool=dict(type='str',),acl_name_seq_num=dict(type='int',)),
        stats_data_action=dict(type='str',choices=['stats-data-enable','stats-data-disable']),
        template_connection_reuse=dict(type='str',),
        uuid=dict(type='str',),
        template_tcp_shared=dict(type='str',),
        template_tcp=dict(type='str',),
        template_persist_destination_ip=dict(type='str',),
        when_down=dict(type='bool',),
        template_client_ssl_shared=dict(type='str',),
        persist_type=dict(type='str',choices=['src-dst-ip-swap-persist','use-src-ip-for-dst-persist','use-dst-ip-for-src-persist']),
        use_rcv_hop_for_resp=dict(type='bool',),
        scaleout_bucket_count=dict(type='int',),
        req_fail=dict(type='bool',),
        no_dest_nat=dict(type='bool',),
        name=dict(type='str',),
        template_policy=dict(type='str',),
        user_tag=dict(type='str',),
        template_diameter=dict(type='str',),
        sampling_enable=dict(type='list',counters1=dict(type='str',choices=['all','curr_conn','total_l4_conn','total_l7_conn','total_tcp_conn','total_conn','total_fwd_bytes','total_fwd_pkts','total_rev_bytes','total_rev_pkts','total_dns_pkts','total_mf_dns_pkts','es_total_failure_actions','compression_bytes_before','compression_bytes_after','compression_hit','compression_miss','compression_miss_no_client','compression_miss_template_exclusion','curr_req','total_req','total_req_succ','peak_conn','curr_conn_rate','last_rsp_time','fastest_rsp_time','slowest_rsp_time','loc_permit','loc_deny','loc_conn','curr_ssl_conn','total_ssl_conn','backend-time-to-first-byte','backend-time-to-last-byte','in-latency','out-latency','total_fwd_bytes_out','total_fwd_pkts_out','total_rev_bytes_out','total_rev_pkts_out'])),
        template_ssli=dict(type='str',),
        template_smpp=dict(type='str',),
        no_logging=dict(type='bool',),
        reset_on_server_selection_fail=dict(type='bool',),
        waf_template=dict(type='str',),
        ipinip=dict(type='bool',),
        no_auto_up_on_aflex=dict(type='bool',),
        rate=dict(type='int',),
        gslb_enable=dict(type='bool',),
        template_persist_ssl_sid=dict(type='str',),
        template_dns=dict(type='str',),
        template_sip=dict(type='str',),
        template_dblb=dict(type='str',),
        shared_partition_server_ssl_template=dict(type='bool',),
        template_client_ssl=dict(type='str',),
        enable_playerid_check=dict(type='bool',),
        service_group=dict(type='str',),
        template_fix=dict(type='str',),
        shared_partition_udp=dict(type='bool',),
        syn_cookie=dict(type='bool',),
        alternate_port=dict(type='bool',),
        template_cache=dict(type='str',),
        rtp_sip_call_id_match=dict(type='bool',),
        template_scaleout=dict(type='str',),
        template_ftp=dict(type='str',),
        serv_sel_fail=dict(type='bool',),
        range=dict(type='int',),
        action=dict(type='str',choices=['enable','disable']),
        shared_partition_client_ssl_template=dict(type='bool',),
        view=dict(type='int',),
        template_persist_source_ip=dict(type='str',),
        template_dynamic_service=dict(type='str',),
        use_cgnv6=dict(type='bool',),
        template_persist_cookie=dict(type='str',),
        template_virtual_port=dict(type='str',),
        conn_limit=dict(type='int',),
        trunk_fwd=dict(type='str',),
        template_udp_shared=dict(type='str',),
        pool=dict(type='str',),
        snat_on_vip=dict(type='bool',),
        shared_partition_tcp=dict(type='bool',),
        template_tcp_proxy_server=dict(type='str',),
        shared_partition_http_template=dict(type='bool',),
        template_external_service=dict(type='str',),
        template_udp=dict(type='str',),
        force_routing_mode=dict(type='bool',),
        template_file_inspection=dict(type='str',),
        when_down_protocol2=dict(type='bool',),
        def_selection_if_pref_failed=dict(type='str',choices=['def-selection-if-pref-failed','def-selection-if-pref-failed-disable']),
        template_smtp=dict(type='str',),
        redirect_to_https=dict(type='bool',),
        alt_protocol2=dict(type='str',choices=['tcp']),
        alt_protocol1=dict(type='str',choices=['http']),
        message_switching=dict(type='bool',),
        template_imap_pop3=dict(type='str',),
        scaleout_device_group=dict(type='int',),
        l7_hardware_assist=dict(type='bool',),
        template_http_policy=dict(type='str',),
        reset=dict(type='bool',),
        use_alternate_port=dict(type='bool',),
        acl_id_list=dict(type='list',acl_id_seq_num=dict(type='int',),acl_id=dict(type='int',),acl_id_src_nat_pool=dict(type='str',)),
        trunk_rev=dict(type='str',),
        eth_fwd=dict(type='str',),
        template_respmod_icap=dict(type='str',),
        template_server_ssl_shared=dict(type='str',),
        use_default_if_no_server=dict(type='bool',),
        auto=dict(type='bool',),
        aflex_scripts=dict(type='list',aflex=dict(type='str',)),
        template_http_shared=dict(type='str',),
        template_server_ssl=dict(type='str',),
        alternate_port_number=dict(type='int',),
        port_number=dict(type='int',required=True,),
        template_tcp_proxy_client=dict(type='str',),
        template_tcp_proxy=dict(type='str',),
        extended_stats=dict(type='bool',),
        template_http=dict(type='str',),
        expand=dict(type='bool',),
        skip_rev_hash=dict(type='bool',),
        on_syn=dict(type='bool',),
        clientip_sticky_nat=dict(type='bool',),
        secs=dict(type='int',),
        auth_cfg=dict(type='dict',aaa_policy=dict(type='str',)),
        eth_rev=dict(type='str',)
    ))

    return rv


def new_url(module):
    """Return the URL for creating a resource"""
    # To create the URL, we need to take the format string and return it with no params
    url_base = "/axapi/v3/slb/virtual-server/{name}/port/{port-number}+{protocol}"
    f_dict = {}
    f_dict["port-number"] = ""
    f_dict["protocol"] = ""
    # Override with the specified hint key
    f_dict["name"] = module.params["virtual_server"]

    return url_base.format(**f_dict)


def existing_url(module):
    """Return the URL for an existing resource"""
    # Build the format dictionary
    url_base = "/axapi/v3/slb/virtual-server/{name}/port/{port-number}+{protocol}"

    f_dict = {}
    f_dict["port-number"] = module.params["port_number"]
    f_dict["protocol"] = module.params["protocol"]
    f_dict["name"] = module.params["virtual_server"]
    
    return url_base.format(**f_dict)


def build_envelope(title, data):
    return {
        title: data
    }


def _to_axapi(key):
    return translateBlacklist(key, KW_OUT).replace("_", "-")


def _build_dict_from_param(param):
    rv = {}

    for k,v in param.items():
        hk = _to_axapi(k)
        if isinstance(v, dict):
            v_dict = _build_dict_from_param(v)
            rv[hk] = v_dict
        if isinstance(v, list):
            nv = [_build_dict_from_param(x) for x in v]
            rv[hk] = nv
        else:
            rv[hk] = v

    return rv


def build_json(title, module):
    rv = {}

    for x in AVAILABLE_PROPERTIES:
        v = module.params.get(x)
        if v:
            rx = _to_axapi(x)

            if isinstance(v, dict):
                nv = _build_dict_from_param(v)
                rv[rx] = nv
            if isinstance(v, list):
                nv = [_build_dict_from_param(x) for x in v]
                rv[rx] = nv
            else:
                rv[rx] = module.params[x]

    return build_envelope(title, rv)


def validate(params):
    # Ensure that params contains all the keys.
    requires_one_of = sorted([])
    present_keys = sorted([x for x in requires_one_of if params.get(x)])
    
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

def get(module):
    return module.client.get(existing_url(module))

def exists(module):
    try:
        return get(module)
    except a10_ex.NotFound:
        return False

def create(module, result):
    payload = build_json("port", module)
    try:
        post_result = module.client.post(new_url(module), payload)
        result.update(**post_result)
        result["changed"] = True
    except a10_ex.Exists:
        result["changed"] = False
    except a10_ex.ACOSException as ex:
        module.fail_json(msg=ex.msg, **result)
    except Exception as gex:
        raise gex
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

def update(module, result, existing_config):
    payload = build_json("port", module)
    try:
        post_result = module.client.post(existing_url(module), payload)
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
    if not exists(module):
        return create(module, result)
    else:
        return update(module, result, existing_config)

def absent(module, result):
    return delete(module, result)

def run_command(module):
    run_errors = []

    result = dict(
        changed=False,
        original_message="",
        message=""
    )

    state = module.params["state"]
    a10_host = module.params["a10_host"]
    a10_username = module.params["a10_username"]
    a10_password = module.params["a10_password"]
    # TODO(remove hardcoded port #)
    a10_port = 443
    a10_protocol = "https"

    valid = True

    if state == 'present':
        valid, validation_errors = validate(module.params)
        map(run_errors.append, validation_errors)
    
    if not valid:
        result["messages"] = "Validation failure"
        err_msg = "\n".join(run_errors)
        module.fail_json(msg=err_msg, **result)

    module.client = client_factory(a10_host, a10_port, a10_protocol, a10_username, a10_password)
    existing_config = exists(module)

    if state == 'present':
        result = present(module, result, existing_config)
        module.client.session.close()
    elif state == 'absent':
        result = absent(module, result)
        module.client.session.close()
    return result

def main():
    module = AnsibleModule(argument_spec=get_argspec())
    result = run_command(module)
    module.exit_json(**result)

# standard ansible module imports
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *

if __name__ == '__main__':
    main()
