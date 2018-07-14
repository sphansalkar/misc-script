import requests
import time

headers = {'Content-type': 'application/json'}

cloud_app = '192.168.5.98'
# prem_app = '10.10.15.220'
prem_app = '192.168.4.220'

def vm_op(op_type="create_vm"):
    vm_uuid = "1921681112_422fd9285ba28bf001c21ed10d2e1885_UB11"
    # vm_uuid = "1921681112_422f964eb73c35d6f9fd5ddfa33c8ac3_RHEL"  # DEMO
    url = "https://%s/PIOA_Primary/v1.0/vm_operation?vm_id=%s" % (prem_app, vm_uuid)
    print("\n url = ", url)

    data = { 'vm_uuid': vm_uuid,
             'op_type': '%s' % op_type,
             # 'hosted_on': '10.10.8.55',   # HE
             'hosted_on': '192.168.1.51',   # PUNE
             'vm_name': 'TEST_VM',
             'vm_data': {'iso': 'TFTP_Server0.iso'}
    }

    '''
    # data for create snapshot
    data = {'vm_uuid': vm_uuid, 'op_type': '%s' % op_type,
            'hosted_on': '10.10.8.55', 'snapshot_name': 'pio_snap',
            'is_memory': True, 'quiesce': False, 'description': 'TGT snap',
            'vm_data': {'iso': 'iPXE_Server0.iso'}
            }
    '''

    resp = requests.post(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)
    print("data = ", resp.json())


if __name__ == "__main__":
    vm_op("CREATE_VM")
    # vm_op("POWER_ON_VM")
    # vm_op("POWER_OFF_VM")
    # vm_op("CREATE_SNAPSHOT")
    # vm_op("DELETE_VM")
