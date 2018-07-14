import requests
import time

headers = {'Content-type': 'application/json'}

# prem_app = '10.10.15.220'
prem_app = '192.168.4.220'

NOT_STARTED = 0
SUCCESS = 1
FAILURE = 2
UNDO_SUCCESS = 3
UNDO_FAILURE = 4

def update_status():

    vm_uuid = "1921681112_422f06bac5d784362593a38b947734c5_UB10"
    # vm_uuid = "1921681112_422f964eb73c35d6f9fd5ddfa33c8ac3_RHEL"  # DEMO

    url = "https://%s/PIOA_Primary/v1.0/update_status" % prem_app
    print("\n url = ", url)

    data = {'vm_uuid': vm_uuid,
            'status': SUCCESS,
            'progress': 100,
            'reason': 'Successfully Executed Step 3'}

    resp = requests.post(url, json=data, verify=False, headers=headers)
    print("status_code = ", resp.status_code)
    print("reason = ", resp.reason)
    print("data = ", resp.json())

if __name__ == "__main__":
    update_status()
