import requests
import time

headers = {'Content-type': 'application/json'}

cloud_app = '192.168.5.98'

# prem_app = '10.10.15.220'
prem_app = '192.168.4.220'

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

def upload_iso():

    token = login()['token']
    headers['Authorization'] = 'token {}'.format(token)

    url = "https://%s/PIOA_Primary/v1.0/upload/vm_iso" % prem_app
    print("\n url = %s" % url)

    data = { 'datacenter': '10.10.11.94',
             'datacenter_username': 'administrator@vsphere.local',
             'datacenter_type': 'VCENTER',
             'datacenter_datastore': 'SSD_DS',
             'iso_name': 'TFTP_Server0.iso',
             'iso_path': '/var/www/bundle/TFTP_Server0.iso'
    }

    # VMC
    '''
    data = { 'datacenter': 'vcenter.sddc-54-148-141-15.vmc.vmware.com',
             'datacenter_username': 'cloudadmin@vmc.local',
             'datacenter_type': 'VMC',
             'datacenter_datastore': 'WorkloadDatastore',
             'iso_name': 'TFTP_Server0.iso',
             'iso_path': '/var/www/bundle/TFTP_Server0.iso'
    }
    '''

    resp = requests.post(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)
    print("data = ", resp.json())

def upload_ovf(ovf_type="machine_ovf"):
    token = login()['token']
    headers['Authorization'] = 'token {}'.format(token)

    url = "https://%s/PIOA_Primary/v1.0/upload/machine_ovf" % prem_app
    print("\n url = %s" % url)

    data = { 'datacenter': '192.168.1.212',
             'datacenter_username': 'administrator@vsphere.local',
             'datacenter_type': 'VCENTER',
             'datacenter_datastore': 'Samsung 1TB SSD',
    }

    '''

    # VMC
    data = { 'datacenter': 'vcenter.sddc-54-148-141-15.vmc.vmware.com',
             'datacenter_username': 'cloudadmin@vmc.local',
             'datacenter_type': 'VMC',
             'datacenter_datastore': 'WorkloadDatastore',
    }
    '''

    resp = requests.post(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)
    print("data = ", resp.json())

def deploy_ovf():
    token = login()['token']
    headers['Authorization'] = 'token {}'.format(token)

    url = "https://%s/PIOA_Primary/v1.0/deploy/machine_ovf" % prem_app
    print("\n url = %s" % url)

    '''
    data = { 'datacenter': '192.168.1.51',
             'datacenter_username': 'administrator@vsphere.local',
             'datacenter_type': 'VCENTER',
             'datacenter_datastore': 'datastore1 (1)',
             'datacenter_cluster_name': 'cloud_cluster',
             'datacenter_resource_pool': 'cloud_resource_pool',
             'vm_name': 'test_vm'
    }

    # VMC
    '''
    data = { 'datacenter': 'vcenter.sddc-54-148-141-15.vmc.vmware.com',
             'datacenter_username': 'cloudadmin@vmc.local',
             'datacenter_type': 'VMC',
             'datacenter_datastore': 'WorkloadDatastore',
             'datacenter_cluster_name': 'Cluster-1',
             'datacenter_resource_pool': 'Compute-ResourcePool',
             'vm_name': 'test_vm'
    }

    resp = requests.post(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)
    print("data = ", resp.json())


if __name__ == "__main__":
    # login()
    # upload_iso()
    upload_ovf()
    # deploy_ovf()
