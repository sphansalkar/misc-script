"""Global base config file.

Set the variables in this file to change the flavour of the deployment
appropriately.

The most important parameter is 'config_template' this points to the
config template we want to pickup. The options are
- init_config_min_dummy ...

The remainder key values are substitutions for these values in the
config template.

"""

#############################
# -------- IMP ----------
# set the variable
# "base_config" at bottom
# of the config file to the
# variant desired
#############################


#############################
# Config to run
# Dummy images
# on Virtualbox on local host
#############################

dummy_config = {
    # Common configuration part
    # do not modify 'config_template'
    'config_template'        : 'init_config_min_dummy',

    # An arbitrary prefix to prepend on VM names, useful if you intend
    # to share the same server for testing.
    'BASECFG_name_prefix'    : 'dummy',
    'BASECFG_cert_base_path' : '/home/rajshree/.docker/machine/certs',
    'BASECFG_etcd_ip'        : '10.10.12.46',
    'BASECFG_etcd_port'      : '2379',
    'BASECFG_swarm_create'   : True,
    'BASECFG_tls_verify'     : True,
    'BASECFG_driver'         : 'vmwarevsphere',
    'BASECFG_images_path'    : '',

    # This configuration is common for vmwarevsphere and OVF driver
    'BASECFG_vsphere_ip'          : '10.10.10.32',
    'BASECFG_vsphere_username'    : 'root',
    'BASECFG_vsphere_passwd'      : 'root123',
    'BASECFG_on_prem_thumbprint'    : '',
    'BASECFG_vsphere_datacenter'  : '',
    'BASECFG_vsphere_datastore'   : 'SSD_DS',
    'BASECFG_vsphere_resource_pool': '',
    'BASECFG_vsphere_cluster'      : '',

    # This configuration is for vmwarevsphere
    'BASECFG_vsphere_disk_size'   : '10000',
    'BASECFG_vsphere_memory_size' : '2048',
    'BASECFG_vsphere_network'     : 'VM Network',

    # This configuration is for OVF driver
    'BASECFG_app_ip'              : '192.168.5.240',
    'BASECFG_app_port'             : '10000',
    'BASECFG_app_iso_path'        : '/tmp/',
    'BASECFG_app_username'        : 'administrator@pio.com',
    'BASECFG_app_password'        : 'admin@123',
    'BASECFG_datacenter_type'   : 'VCENTER',
    'BASECFG_vsphere_cluster'           : 'HA_DevCluster',
    'BASECFG_vsphere_resource_pool'     : 'vAppGanesh',
    'BASECFG_machine_to_deploy' : 'pio-machine'
}

#############################
# Config to run
# Real images
# on a single vCenter
#############################

real_config = {
    # Common configuration
    # do not modify 'config_template'
    'config_template'             : 'init_config_max_real',

    # An arbitrary prefix to prepend on VM names, useful if you intend
    # to share the same server for testing.
    'BASECFG_name_prefix'    : 'Shri',
    'BASECFG_cert_base_path'      : '/root/.docker/machine/certs',
    #'BASECFG_etcd_ip'             : '192.168.5.193',
    'BASECFG_etcd_ip'             : '10.10.15.220',
    'BASECFG_etcd_port'           : '2379',
    'BASECFG_swarm_create'        : False,
    'BASECFG_prem_driver'         : 'ovf',
    'BASECFG_cloud_driver'        : 'ovf',
    'BASECFG_cloud_type'          : 'on_prem',
    'BASECFG_images_path'         : '/images/',

    'BASECFG_on_prem_tls_verify'     : False,
    'BASECFG_on_cloud_tls_verify'    : False,

    # This configuration is for vmwarevsphere driver
    'BASECFG_on_prem_ip'           : '10.10.11.94',
    'BASECFG_on_prem_username'     : 'administrator@vsphere.local',
    'BASECFG_on_prem_passwd'       : 'Root@123',
    'BASECFG_on_prem_thumbprint'   : '29:43:C1:83:B3:98:47:C5:A3:55:C6:A1:CE:4B:50:33:92:74:F9:D3',
    'BASECFG_on_prem_datacenter'   : 'HADatacenter',
    'BASECFG_on_prem_datastore'    : 'SSD_DS',
    'BASECFG_on_prem_disk_size'    : '10000',
    'BASECFG_on_prem_memory_size'  : '2048',
    'BASECFG_on_prem_network'      : 'VM Network',
    'BASECFG_on_prem_resource_pool': 'HA_Dev_RP',
    'BASECFG_on_prem_cluster'      : 'HA_Dev_Cluster',

    'BASECFG_on_prem_datacenter_type'   : 'VCENTER',
    'BASECFG_on_prem_machine_to_deploy' : 'pio-machine',

    # This configuration is common for OVF and vmwarevsphere driver
    # VMC
    'BASECFG_on_cloud_ip'                : 'vcenter.sddc-54-148-141-15.vmc.vmware.com',
    'BASECFG_on_cloud_username'          : 'cloudadmin@vmc.local',
    'BASECFG_on_cloud_passwd'            : 'yX-l2sdd-3',
    'BASECFG_on_cloud_datastore'         : 'WorkloadDatastore',
    'BASECFG_on_cloud_datacenter'        : 'SDDC-Datacenter',
    'BASECFG_on_cloud_cluster'           : 'Cluster-1',
    'BASECFG_on_cloud_resource_pool'     : 'Compute-ResourcePool',
    'BASECFG_app_ip'                     : '10.10.15.220',
    'BASECFG_app_port'                    : '',
    'BASECFG_app_iso_path'               : '/var/www/bundle/',
    'BASECFG_app_username'               : 'administrator@pio.com',
    'BASECFG_app_password'               : 'admin@123',
    'BASECFG_app_bash_username'          : 'root',
    'BASECFG_app_bash_password'          : 'admin@123',

    # This configuration is for cloud mwaresphere driver
    'BASECFG_on_cloud_disk_size'   : '10000',
    'BASECFG_on_cloud_memory_size' : '2048',
    'BASECFG_on_cloud_network'     : 'pio_network',

    'BASECFG_on_cloud_datacenter_type'   : 'VMC',
    'BASECFG_on_cloud_machine_to_deploy' : 'pio-machine'
}



base_config = real_config
