#pyvmomi related imports
import atexit
import os
import sys
import time
import errno
import ssl
import requests
import datetime

from pyVmomi import vim, vmodl, pbm
from pyVim.task import WaitForTask
from pyVim import connect
from pyVim.connect import SmartConnectNoSSL, Disconnect


def get_contoller_map(si, vm_uuid):
    search_index = si.content.searchIndex

    # print "dir(search_index) %s" % dir(search_index)
    vm = search_index.FindByIp(None, "192.168.3.203", True)
    # print search_index.Array()
    extra_conf = vm.config.extraConfig
    # print extra_conf

    map_list = []

    for device in vm.config.hardware.device:

        map_dict = {}

        if (device.key >= 2000) and (device.key <= 3000):
            # print "device %s" % type(device.__name__)
            pass

        return


        if isinstance(device, vim.vm.device.VirtualDisk):
            print "Device %s" % type(device).__name__
            print "Device %s" % device
            print
            print "DeviceInfo %s" % device.deviceInfo

            if device.backing is None:
                continue

            '''
            print "dir(device)", dir(device)
            print "device.slotInfo ", device.slotInfo

            print "\n\n"
            print type(device).__name__
            print "Label %s" % device.deviceInfo.label
            '''
            map_dict['label'] = device.deviceInfo.label
            # print "unitNumber %s" % device.unitNumber
            map_dict['unit_number'] = device.unitNumber
            # print "controllerKey %s" % device.controllerKey
            map_dict['controller_key'] = device.controllerKey
            map_dict['bus_number'] = device.busNumber

            if hasattr(device.backing, "fileName"):
                # print "fileName %s" % device.backing.fileName
                map_dict['file_name'] = device.backing.fileName
            if hasattr(device.backing, "uuid"):
                # print "uuid = %s" % device.backing.uuid
                map_dict['uuid'] = device.backing.uuid

            map_list.append(map_dict)

    return map_list

if __name__ == "__main__":

    host_ip = "192.168.1.43"
    user = "administrator@vsphere.local"
    passwd = "Root@123"
    port = 443
    # vm_uuid = "422C5304-32C3-7B6A-5EFB-8A7AFA6702F0"
    vm_uuid = "422C5304-32C3-7B6A-5EFB-8A7AFA6702F0"

    si = connect.SmartConnectNoSSL(host=host_ip, user=user, pwd=passwd, port=port)
    atexit.register(connect.Disconnect, si)

    map_ls = get_contoller_map(si, vm_uuid)

    # print map_ls
