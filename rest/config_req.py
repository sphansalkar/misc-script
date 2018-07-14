import requests
from global_cfg import base_config

headers = {'Content-type': 'application/json'}

ha_mgr = "10.10.15.220"
ha_port = 8000

def config_req():
    url = "http://%s:%s/ha_mgr/v1.0/start" % (ha_mgr, ha_port)
    print("\n url = ", url)

    resp = requests.post(url, json=base_config, verify=False, headers=headers)
    print("status_code = ", resp.status_code)

if __name__ == "__main__":
    config_req()
