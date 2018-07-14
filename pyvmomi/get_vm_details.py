from pyVmomi import vim, vmodl, pbm
from pyVim.task import WaitForTask
from pyVim import connect
from pyVim.connect import SmartConnectNoSSL, Disconnect
import pdb

def get_obj(content, vimtype, name):
    obj = None
    container = content.viewManager.CreateContainerView(
                content.rootFolder, vimtype, True)
    for c in container.view:
        if c.name == name:
            obj = c
            return obj


def get_dc_details(si):
    cloud_details = []

    for dc in si.content.rootFolder.childEntity:
        dc_info = {}
        folder_list = []
        print(dc.name)
        for folder in dc.vmFolder.childEntity:
            folder_list.append(folder.name)

        dc_info['dc_name'] = dc.name
        dc_info['folders'] = folder_list

        for cls in dc.hostFolder.childEntity:
            print("\t%s" % cls.name)

    print(cloud_details)

def get_mac_address(config):
    for device in config.hardware.device:
        if isinstance(device, vim.vm.device.VirtualEthernetCard):
            return device.macAddress



if __name__ == "__main__":

    host_ip = "192.168.1.112"
    user = "administrator@vsphere.local"
    passwd = "Root@123"
    port = 443
    vm_name = "Demo_VM_1"

    si = connect.SmartConnectNoSSL(host=host_ip, user=user, pwd=passwd, port=port)

    # get_dc_details(si)
    #import sys
    #sys.exit(0)
    vm_obj = get_obj(si.content, [vim.VirtualMachine], vm_name)
    print (get_mac_address(vm_obj.config))
    print (vm_obj.name)
    print ("Instance UUID: %s" % vm_obj.summary.config.instanceUuid)
    print ("BIOS UUID: %s" % vm_obj.summary.config.uuid)

    device = None

    for dev in vm_obj.config.hardware.device:
        if (dev.key >= 2000) and (dev.key <= 3000):
            device = dev

        if isinstance(device, vim.vm.device.VirtualDisk):
            pass
