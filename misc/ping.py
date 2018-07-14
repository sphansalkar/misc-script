import pyping
import subprocess
import paramiko

ip_list = []

def run_cmd_set(ip, username="root", passwd="root123"):
    print("Running cmd set")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, username=username, password=passwd)

    cmd = "ls"
    stdin, stdout, stderr = ssh.exec_command(cmd)

    file_name = "file_%s" % ip.replace(".", "")
    print("File Name %s", file_name)

    with open("%s" % file_name, "w+") as fd:
        fd.write("IP: %s" % ip)
        fd.write("cmd: %s" % cmd)
        fd.write("IP: %s" % stdout.read())

def test_ips():
    try:
        with open('ip_files', 'r') as fd:
            ip_list = fd.readlines()

    except OSError as e:
        print(e)
        raise e

    for ip in ip_list:
        try:
            print("\n Now pinging IP: %s" % ip)
            ip = ip.strip()
            r = pyping.ping(ip)

            # IP is reachable
            if r.ret_code == 0:
                print("IP: %s is reachable running few commands" % ip)
                if ip == "10.10.8.38":
                    ret = run_cmd_set(ip, "root", "Root@123")
                else:
                    ret = run_cmd_set(ip, passwd="admin@123")
            else:
                print("IP: %s is not reachable trying next IP" % ip)
        except Exception as e:
            print(e)
            continue


if __name__ == "__main__":
    test_ips()
