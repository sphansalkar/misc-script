from pyVmomi import vim, SoapStubAdapter, vmodl, pbm
from pyVim.connect import SmartConnectNoSSL, Disconnect, SmartConnect
from pyVmomi.SoapAdapter import CONNECTION_POOL_IDLE_TIMEOUT_SEC
# import OpenSSL.SSL as ossl
import ssl
import pdb
import sys

def _get_cookie(cookie):
    for c in cookie.split(";"):
        tmp = c.split("=")
        if len(tmp) > 1:
            if tmp[0].strip().lower() == "vmware_soap_session":
                cookie = tmp[1].strip()
                break

    return cookie

def get_cookie(host, user, passwd):

    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    # context = ssl._create_unverified_context()
    context.verify_mode = ssl.CERT_NONE

    print("connectionPoolTimeout = %s" % CONNECTION_POOL_IDLE_TIMEOUT_SEC)

    si = SmartConnect(host=host, user=user, pwd=passwd, sslContext=context,
                      protocol="https",connectionPoolTimeout=CONNECTION_POOL_IDLE_TIMEOUT_SEC)

    print("si %s" % si)
    print ("Old Session %s" % si.content.sessionManager.currentSession.key)
    cookie = _get_cookie(si._GetStub().cookie)

    return cookie

if __name__ == "__main__":

    host_ip = "192.168.1.127"
    user = "administrator@vsphere.local"
    passwd = "Root@123"
    port = 443

    cookie = get_cookie(host_ip, user, passwd)
    print()
    print(cookie)

    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    # context = ssl._create_unverified_context()
    context.verify_mode = ssl.CERT_NONE

    new_stub = SoapStubAdapter(host_ip, port, version="vim.version.version6",
                               path="/sdk", certKeyFile=None, certFile=None,
                               thumbprint=None, sslContext=context,
                               # thumbprint=None,
                               requestContext={"vcSessionCookie": cookie},
                               connectionPoolTimeout=CONNECTION_POOL_IDLE_TIMEOUT_SEC)

    '''
    new_stub = SoapStubAdapter(host_ip, port, version="pbm.version.version2",
                               path="/pbm", certKeyFile=None, certFile=None,
                               thumbprint=None, sslContext=context,
                               # thumbprint=None,
                               requestContext={"vcSessionCookie": cookie},
                               connectionPoolTimeout=CONNECTION_POOL_IDLE_TIMEOUT_SEC)
    '''

    si = vim.ServiceInstance("ServiceInstance", new_stub)
    # si = pbm.PbmServiceInstance("ServiceInstance", new_stub)

    print()
    print("si %s" % si)
    content = None
    try:
        content = si.RetrieveServiceContent()
        # pbm_content = si.PbmRetrieveServiceContent()
        pdb.set_trace()
        print ("New Session %s" % content.sessionManager.currentSession.key)
    except vmodl.MethodFault:
        raise
    except Exception as e:
        fault = vim.fault.HostConnectFault(msg=str(e))
        print("Fault %s" % fault)
        raise Exception(msg=str(e))
