from pyVmomi import vim, SoapStubAdapter, vmodl, pbm
from pyVim.connect import SmartConnectNoSSL, Disconnect, SmartConnect
from pyVmomi.SoapAdapter import CONNECTION_POOL_IDLE_TIMEOUT_SEC
# import OpenSSL.SSL as ossl
import ssl
import pdb
import sys

def get_obj(content, vimtype, name):
    obj = None
    container = content.viewManager.CreateContainerView(
                content.rootFolder, vimtype, True)
    for c in container.view:
        if c.name == name:
            obj = c
            return obj

def cancel_recent_tasks(content):
    for task in content.taskManager.recentTask:
        print(task)
        print(dir(task))
        if task.info.state in [vim.TaskInfo.State.running, vim.TaskInfo.State.queued]:
            task.CancelTask()

if __name__ == "__main__":

    host_ip = "192.168.1.112"
    user = "administrator@vsphere.local"
    vm_uuid = "502fa9c7-981d-e00c-a812-f4051c9240e9"
    passwd = "Root@123"
    port = 443
    vm_name = "VM1234"

    si = SmartConnectNoSSL(host=host_ip, user=user, pwd=passwd, port=port)
    content = si.content

    # cancel_recent_tasks(content)

    vm_obj = si.content.searchIndex.FindByUuid(None, vm_uuid, True, True)
    print (vm_obj.name)

    # Create task
    task = content.taskManager.CreateTask(vm_obj, "PrimaryIO Migrate Back",
            "administrator", True, None)

    for t in content.taskManager.recentTask:
        print(">>>>> %s" %t)
        print(">>>>> %s" % task.task._moId)
        if t._moId == task.task._moId:
            tk = t
            break

    print("tk = %s" % tk)
    pdb.set_trace()
    tk.SetState(vim.TaskInfo.State.running)

    for tsk in content.taskManager.recentTask:
        try:
            tsk.SetTaskState(vim.TaskInfo.State.running)
        except:
            continue

    import time; time.sleep(2)
    new_task = vim.Task(tk._moId, stub=vm_obj._stub)

    print("new_task = %s" % new_task)
    new_task.UpdateProgress(10)
    import time; time.sleep(2)
    tk.SetState(vim.TaskInfo.State.success)
