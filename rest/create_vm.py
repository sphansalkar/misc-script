import sys, pdb
from supervisor.utils.vim_utils import wait_for_task, VCenter
from pyVim import connect
from pyVmomi import vim, VmomiSupport


ip = "cp-vc65-vmc.piointernal.lan"
username = "administrator@vsphere.local"
password = "Root@123"

vm_name = "Test_VM"
# vm_folder_to_select = "Workloads"
datastore = "WorkloadDatastore"
resource_pool_name = "Compute-ResourcePool"
net_name = 'sddc-cgw-network-1'
nic_type = 'E1000'
devices = []

datastore_path = '[' + datastore + '] ' + vm_name
# datastore_path = '[' + datastore + '] ' + vm_name + ".vmx"


def create_vm()
    vmx_file = vim.vm.FileInfo( logDirectory=None,
                                snapshotDirectory=None,
                                suspendDirectory=None,
                                vmPathName=datastore_path)

    vc = VCenter(ip, username, password)
    content = vc.content

    datacenter = content.rootFolder.childEntity[0]

    for f in datacenter.vmFolder.childEntity:
        if f.name.lower() == "Workloads".lower():
            vm_folder = f
            break

    cluster = datacenter.hostFolder.childEntity[0]
    resource_pool = None

    print (vm_folder.name)

    for rp in cluster.resourcePool.resourcePool:
        if rp.name  == resource_pool_name:
            resource_pool = rp
            break

    print (datacenter.name)

    print("vmx_file %s" % vmx_file.vmPathName)
    print("vmFolder %s" % vm_folder)
    print("cluster %s" % cluster.name)
    print("resource_pool %s" % resource_pool.name)

    config = vim.vm.ConfigSpec(name=vm_name, memoryMB=1024, numCPUs=1,
                               files=vmx_file, deviceChange=devices,
                               version='vmx-13'
             )

    task = vm_folder.CreateVm(config=config, pool=resource_pool)
    ret = wait_for_task(task)

    print("ret == %s" % ret)


def delete_vm():
    pass

def configure_vm():
    pass


if __name__ == "__main__":
    create_vm()
