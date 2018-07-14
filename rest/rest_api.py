import requests
import time

headers = {'Content-type': 'application/json'}

# cloud_app = '10.10.15.220'
cloud_app = '192.168.4.220'

# prem_app = '10.10.15.220'
prem_app = "192.168.4.220"

# ha_mgr_ip = '10.10.13.59'
ha_mgr_ip = '192.168.5.69'

ha_mgr_port = 8000

def reg_appliance():

    data = {
            'appliance_ip': '%s' % prem_app,
            'vm_uuid': '10101194_4210eb72fe9ab94998907cfc6b328a53_HYP_PIO_APP_PYTHON3',
            'location': 0,
            'type': 'master',
    }

    url = "https://%s/setup/appliance/1" % prem_app

    print("\n url = ", url)
    resp = requests.post(url, json=data, verify=False, headers=headers)

    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)

def reg_pio_service():

    data = {
            'service_ip': '%s' % cloud_app,
            'appliance_ip': '%s' % prem_app,
            'type': 'gateway',
    }

    url = "https://%s/setup/component/1" % prem_app
    print("\n url = ", url)

    resp = requests.post(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)


def update_on_cloud_profiler():

    data = {'vm_uuid': '1010839_422c530432c37b6a5efb8a7afa6702f0_test2',
            'vm_name': 'test2',
            'is_cloud': True}

    url = "https://%s/cloud/update_profiler_db" % cloud_app
    print("\n url = ", url)

    resp = requests.post(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)


def is_migratable():
    data = ["10101194_50109f1d40a172ad9719d9f16edec10f",
            "10101194_5010483fdd24e8eadb80c64485c1e666"
    ]

    url = "https://%s/migrate/is_migratable" % prem_app
    print("\n url = ", url)

    resp = requests.post(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)
    print("data = ", resp.json())

def edit_config_file():
    data = { "section-1": { "y": "144", "x": "122", "new": "500"} }

    url = "https://%s/setup/config_file" % prem_app
    print("\n url = ", url)

    resp = requests.post(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)


def get_config_file():
    url = "https://%s/setup/config_file" % prem_app
    print("\n url = ", url)

    resp = requests.get(url, json={}, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)
    print("data = ", resp.json())


def login():

    url = "https://%s/api-token-auth" % prem_app
    print("\n url = ", url)

    data = { 'username': 'administrator@pio.com',
             'password': 'admin@123'
           }

    resp = requests.post(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)

    return resp.json()

def add_datacenter():

    extra_info = {'datacenter': 'HDM_DC',
                  'cluster': 'HDM_CLUSTER',
                  'compute_resource': 'HDM_RESOURCE_POOL',
                  'datastore': 'QNAP_COMMON_ISCSI',
                  'folder': 'Discovered virtual machine',
                  'network': 'VM Network',
                  'iso': 'ipxe.iso'
                 }

    data = {'url': '10.10.8.55', 'force_add': 0,
            'username': 'administrator@vsphere.local',
            'password': 'Root@123', 'dtype': '8',
            'name': 'VMC', 'location': 'Oregon',
            'global_username': 'administrator@vsphere.local',
            'global_password': 'Root@123',
            'appliance_ip': cloud_app}
            # 'extra_info': extra_info}

    token = login()['token']
    print("token >>> %s" % token)

    url = "https://%s/plugin" % prem_app
    print("\n url = ", url)

    headers['Authorization'] = 'token {}'.format(token)

    print("headers >>>> %s" % headers)

    resp = requests.post(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)


def put_datacenter():

    extra_info = {'datacenter': 'HDM_DC',
                  'cluster': 'HDM_CLUSTER',
                  'compute_resource': 'HDM_CLUSTER',
                  'datastore': 'QNAP_COMMON_ISCSI',
                  'folder': 'Discovered virtual machine',
                  'network': 'VM Network',
                  'iso': 'ipxe.iso'
                 }

    data = {'url': '10.10.8.55', 'force_add': 0,
            'username': 'administrator@vsphere.local',
            'password': 'Root@123', 'dtype': '8',
            'name': 'VMC', 'location': 'Oregon',
            'global_username': 'administrator@vsphere.local',
            'global_password': 'Root@123',
            'appliance_ip': cloud_app,
            'extra_info': extra_info}

    token = login()['token']
    print("token >>> %s" % token)

    url = "https://%s/plugin" % prem_app
    print("\n url = ", url)

    headers['Authorization'] = 'token {}'.format(token)

    print("headers >>>> %s" % headers)

    resp = requests.put(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)


def delete_datacenter():
    data = {'force_delete': 0, 'id': 31}

    url = "https://%s/plugin" % prem_app
    print("\nurl = %s" % url)

    resp = requests.delete(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)

def add_db_entry():
    data = {'vm_uuid': "123454", 'vm_name': "Test_VM"}
    is_cloud = True

    url = "https://%s/cloud/update_profiler_db/%s" % (prem_app, int(is_cloud))
    print("\nurl = %s" % url)

    resp = requests.post(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)

def delete_db_entry():
    data = {'vm_uuid': "123454", 'vm_name': "Test_VM"}
    is_cloud = False

    url = "https://%s/cloud/update_profiler_db/%s" % (prem_app, int(is_cloud))
    print("\nurl = %s" % url)

    resp = requests.post(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)

def get_controller_map():
    vm_uuid = "1010839_422c530432c37b6a5efb8a7afa6702f0_test2"
    url = "https://%s/migrate/disk_controller_map?vm_uuid=%s" % (prem_app, vm_uuid)
    # url = "https://%s/migrate/disk_controller_map" % prem_app
    print("\nurl = %s" % url)

    resp = requests.get(url, json={}, verify=False, headers=headers)

    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)
    print("data = ", resp.json())

def prep_to_migrate():
    # vm_uuid = "cpvc65vmcpiointernallan_423d14e894b437edc44a9cad8746ced5_op_prem_vm"
    # vmdk_uuid = "cpvc65vmcpiointernallan_6000C29f417753bebb8a4c79a1088e13_op_prem_vm"
    vm_uuid = "10101194_423d14e894b437edc44a9cad8746ced5_op_prem_vm"
    vmdk_uuid = "10101194_6000C29f417753bebb8a4c79a1088e13_op_prem_vm"

    data = {"vm_uuid": vm_uuid, "is_migratable": True, "vmdk_uuid": vmdk_uuid}
    # data = {"vm_uuid": vm_uuid, "is_migratable": False}

    url = "https://%s/migrate/prepare_to_migrate" % prem_app

    resp = requests.post(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)
    print("data = ", resp.json())


def get_cloud_details():
    url = "https://%s/cloud/get_cloud_details" % prem_app
    print("\n url = ", url)

    resp = requests.get(url, json={}, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)
    print("data = ", resp.json())


def config_tgt():
    url = "https://%s/migrate/tgt_config" % prem_app
    print("\n url = ", url)


    data = [{# "vmuuid": "10101194_423d14e894b437edc44a9cad8746ced5_op_prem_vm",
             "vmuuid": "1921681126_4227ee89abcb91f374f39a36ef01280e_PythonVM",
             "msg": "Configuring TGT and iPXE", "memory": 1024,
             "taskVal": "task-3091", "cpu": 1, "storage": 10485760,
             "cloud": "vCloud", "prepareToMigrate": "true",
             "name": "op_prem_vm", "progress": "70",
             "state": "GET_CLOUD_DETAILS_FAILED",
             "value": "vm-50", "macAddr": "00:50:56:a7:81:74", "status": "0"}]

    resp = requests.post(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)
    print("data = ", resp.json())

def create_vm(op_type="create_vm"):
    url = "https://%s/vm_op/vm_operation" % prem_app
    print("\n url = ", url)

    '''
    data = {'vm_uuid': '1921681126_42315bd768368ede80f4ff75bee0b88c_ubuntu_vm', 'op_type': '%s' % op_type,
            'hosted_on': '192.168.1.127'}
    '''

    # data for create snapshot
    data = {'vm_uuid': '1921681126_42315bd768368ede80f4ff75bee0b88c_ubuntu_vm', 'op_type': '%s' % op_type,
            'hosted_on': '192.168.1.126', 'snapshot_name': 'pio_snap',
            'is_memory': True, 'quiesce': False, 'description': 'TGT snap'}

    resp = requests.post(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)
    print("data = ", resp.json())

def create_ipxe():

    url = "https://%s/cloud/create_ipxe" % (prem_app)
    print("\n url = ", url)

    data = [{"on_cloud_gway_ip": "192.168.4.160", "vm_mac_address":
        "00:50:56:8f:d8:40", "on_cloud_gway_port": "10005", "tftp_ip":
        "192.168.128.103", "tgtd_ip": "192.168.4.184", "vm_uuid":
        "1921681126_420f7de982724ef3ae8e2aa444f866d3_NewUbuntuVM", "tgt_port":
        "8500", "aerospike_ip": "192.168.4.33", "vmdk_list": {"Hard_disk_1":
            {"vmdk_size": 17179869184, "disk_id": 2, "label": "Hard_disk_1",
                "vmdk_uuid":
                "1921681126_6000C29f8b5ad14166ec1bc784c149ff_NewUbuntuVM",
                "client_id": 1, "is_boot": True}}, "gateway_flag": "1"}]

    resp = requests.post(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)
    print("data = ", resp.json())

def flush_initiate():
    url = "https://%s/migrate/flush_initiate" % (prem_app)
    print("\n url = ", url)

    '''
    data = [{'datastore_name': 'WorkloadDatastore', 'state': '', 'cloudType':
        'VMC', 'cluster_name': 'Cluster-1', 'taskVal': 'task-1621', 'status':
        '0', 'storage': '12582912', 'prepareToMigrate': 'false', 'network':
        'pio_network', 'memory': '1024', 'value': 'vm-41', 'macAddr':
        '00:50:56:8e:9f:02', 'msg': 'Configuring TGT and iPXE', 'vm_folder':
        'Workloads', 'name': 'u04', 'vmuuid':
        'cpvc65vmc44piointernallan_420e8fb97902b9b9b0068a0900d11f9a_u04',
        'datacenter_name': 'SDDC-Datacenter', 'progress': '80', 'iso':
        'ISO/new.iso', 'resource_pool': 'Compute-ResourcePool', 'cpu': '1'}]
    '''

    data = [{'status': '0', 'datastore_name': 'WorkloadDatastore', 'network':
        'pio_network', 'cluster_name': 'Cluster-1', 'name': 'u10', 'storage':
        '16777216', 'taskVal': 'task-1893', 'vmuuid':
        'cpvc65vmc44piointernallan_420ecbb4c8530c1365621b8629d6082d_u10',
        'msg': 'Configuring cloud machine', 'iso': 'ISO/new.iso', 'value':
        'vm-40', 'state': '', 'progress': '50', 'vm_folder': 'Workloads',
        'cloudType': 'VMC', 'prepareToMigrate': 'false', 'macAddr':
        '00:50:56:8e:2d:76', 'datacenter_name': 'SDDC-Datacenter', 'memory':
        '2048', 'cpu': '1', 'resource_pool': 'Compute-ResourcePool'}]

    resp = requests.post(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)
    print("data = ", resp.json())

def delete_exports():
    url = "https://%s/cloud/delete_exports" % (prem_app)
    print("\n url = ", url)

    data = {'tid': 1}

    resp = requests.post(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)
    print("data = ", resp.json())

def get_cloud_details():
    url = "https://%s/cloud/get_cloud_details" % prem_app
    print("\n url = ", url)

    resp = requests.get(url, json={}, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)
    print("data = ", resp.json())

def dump_db():
    url = "https://%s/migrate/notify/1" % prem_app
    print("\n url = ", url)

    pune_data = [{ 'vCenterIP': '192.168.1.112',
                   'vmuuid': '502f4f69-9445-eef9-dfc8-b3ca85fb7231', # TEST_VM on PUNE
                   # 'vmuuid': '502f379f-c288-fcdc-75cc-33779d09a973', # RHEL in PUNE
                   'cpu': 2, 'memory': 4096,
                   'target': '192.168.1.51'   # PUNE
    }]

    he_data = [{ 'vCenterIP': '10.10.11.94',
                 'vmuuid': '5008664a-bc76-30ef-9a76-1d42b28c196f',
                 # 'vmuuid': '500882b7-ff67-8e35-6d21-13315951ad55',
                 'cpu': 2, 'memory': 4096,
                 'target': '10.10.8.55',
    }]

    data = pune_data

    resp = requests.post(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)
    print("data = ", resp.json())

def migration_req():
    url = "http://%s:%s/ha_mgr/v1.0/migrate_request" % (ha_mgr_ip, ha_mgr_port)
    print("\n url = ", url)

    data = [{'mac_address': ['00:50:56:b1:c9:e0'], 'vm_uuid':
        '192168151_42315bd768368ede80f4ff75bee0b88c_ubuntu_vm', 'source':
        '192.168.1.51', 'is_cloud': True, 'vm_name': 'ubuntu_vm', 'memory':
        4096, 'cpu': 2, 'vmdk_list':
        {'192168151_6000C29646f8e2a93f15de0ea9fff5a6_ubuntu_vm': {'client_id':
            0, 'vmdk_path': '[datastore1] ubuntu_vm/ubuntu_vm-000006.vmdk',
            'ds_uuid': '192168151_5aafabdb0736069ff0960050568b37db',
            'vmdk_size': '16777216', 'vmdk_uuid':
            '192168151_6000C29646f8e2a93f15de0ea9fff5a6_ubuntu_vm', 'disk_id':
            0, 'label': 'Hard disk 1'},
            '192168151_6000C2934b48d98a163a9d0eb41fa30b_ubuntu_vm':
            {'client_id': 0, 'vmdk_path': '[datastore1] ubuntu_vm/ubuntu_vm_1-000006.vmdk',
              'ds_uuid': '192168151_5aafabdb0736069ff0960050568b37db', 'vmdk_size':
            '20971520', 'vmdk_uuid':
            '192168151_6000C2934b48d98a163a9d0eb41fa30b_ubuntu_vm', 'disk_id':
            0, 'label': 'Hard disk 2'}}}]

    resp = requests.post(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)

def update_status():
    url = "https://%s/migrate/update_status" % prem_app
    print("\n url = ", url)

    data = {'vm_uuid': '10101194_4208a1053248efbb7492ee6ece22879f_TEST_VM',
            'state': 1, 'message': 'Successfully Executed Step 3'}

    resp = requests.post(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)
    print("data = ", resp.json())

def stord_create_vm():
    url = "http://%s:8001/StorD/v1.0/new_vm" % prem_app
    print("\n url = ", url)

    data = {'vm_id': 'vm_123'}

    resp = requests.post(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)
    print("data = ", resp.text)

def stord_create_vmdk():
    url = "http://%s:8001/StorD/v1.0/new_vm" % prem_app
    print("\n url = ", url)

    data = {'vm_id': 'vm_123'}

    resp = requests.post(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)
    print("data = ", resp.text)

def tgt_create_target():
    url = "http://%s:8005/TGT_Server/v1.0/create_target?tid=tid_123" % prem_app
    print("\n url = ", url)

    data = {'tid': 'tid_123'}

    resp = requests.post(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)
    print("data = ", resp.text)

def tgt_create_lun():
    url = "http://%s:8005/TGT_Server/v1.0/create_lun" % prem_app
    print("\n url = ", url)

    data = {'vm_id': 'vm_123'}

    resp = requests.post(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)
    print("data = ", resp.text)

def get_daemons():
    url = "http://%s:8007/PIOA_Primary/v1.0/get_daemons" % prem_app
    print("\n url = ", url)

    resp = requests.get(url, json={}, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)
    print("data = ", resp.text)

def create_boot_entry():
    url = "http://%s:8001/TFTP_Server/v1.0/create_boot_entry" % prem_app
    print("\n url = ", url)

    data = {'vm_id': 'vm_123'}

    resp = requests.post(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)
    print("data = ", resp.text)


if __name__ == "__main__":
    # reg_appliance()
    # reg_pio_service()
    # update_on_cloud_profiler()
    # is_migratable()
    # edit_config_file()
    # get_config_file()
    print
    # get_config_file()
    # add_datacenter()
    # put_datacenter()
    # delete_datacenter()
    # add_db_entry()
    # import time; time.sleep(10)
    # delete_db_entry()
    # get_controller_map()
    # prep_to_migrate()
    # get_cloud_details()
    # config_tgt()
    # time.sleep(5)
    # create_vm("delete_vm")
    # time.sleep(5)
    # create_vm("create_vm")
    # time.sleep(5)
    # create_vm("power_on_vm")
    # time.sleep(5)
    # create_vm("power_off_vm")
    # create_vm("reconfigure_vm")
    # create_vm("delete_vm")
    # create_ipxe()
    # flush_initiate()
    # delete_exports()
    # get_cloud_details()
    dump_db()
    # create_vm("create_snapshot")
    # migration_req()
    # update_status()
    # time.sleep(2)
    # stord_create_vm()
    # stord_create_vmdk()
    # tgt_create_target()
    # tgt_create_lun()
    # get_daemons()
    # create_boot_entry()
