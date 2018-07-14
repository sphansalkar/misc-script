import time, pickle

PROGRESS_LOG_FILE = "/tmp/progress_logs"

def set_progress_logs(progress, msg, datetime, status, append=True):

    sub_log_dict = {}
    status_dict = {'status': status}

    with open(PROGRESS_LOG_FILE, "r") as fd:
        log_dict = pickle.load(fd)

    sub_log_dict['progress'] = progress
    sub_log_dict['message'] = msg
    sub_log_dict['datetime'] = datetime

    if append is True:
        log_dict['logs'].append(sub_log_dict)
    else:
        log_dict['logs'][-1] = sub_log_dict

    log_dict['status'] = [status_dict]

    with open(PROGRESS_LOG_FILE, "w") as fd:
        pickle.dump(log_dict, fd)

if __name__ == "__main__":
    message = "About to begin migration"
    set_progress_logs(10, message, time.ctime(), 0)

    time.sleep(2)
    msg = "Successfully performed network setup on ESXi"
    set_progress_logs(20, msg, time.ctime(), 0)

    time.sleep(2)
    msg = "Successfully exported the disks"
    set_progress_logs(80, msg, time.ctime(), 0)
