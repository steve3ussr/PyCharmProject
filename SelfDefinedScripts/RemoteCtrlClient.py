import requests
from re import search
import psutil
from threading import Timer
import time
from os import system
from SelfDefinedScripts.common_modules.CycleTimer import CycleTimer


# TODO：
#   1. kill matlab
#   2.


class RemoteCtrlClient:
    def __init__(self, machine_id, log_dir):
        self.machine_id = machine_id

        self.timer_request = CycleTimer(5, self._exec)

        self.instruct = None
        self.log_instruct = None

        self.log_kill = None

        self.status_cool_down = False
        self.timer_reset_cd = None
        self.interval_reset_cd = 30

        self.timer_start_proc = None
        self.interval_start_proc = 10
        self.log_folder = log_dir

    def _kill_proc(self, name):
        for proc in psutil.process_iter():
            if name.lower() in proc.name().lower():
                try:
                    proc.kill()
                except:
                    continue

    def _start_proc_aux(self, name):
        try:
            system(r"start C:\Progra~1\Oray\SunLogin\SunloginClient\SunloginClient.exe")
        except:
            pass
        self.timer_start_proc = None

    def _start_proc(self, name):
        self.timer_start_proc = Timer(self.interval_start_proc, self._start_proc_aux, (name,))
        self.timer_start_proc.start()

    def _restart_proc(self, name):
        self._kill_proc(name)
        self._start_proc(name)

    def _listen(self):
        post = None
        try:
            url = 'http://175.24.227.118/anti_ctrl/config.html'
            post = requests.get(url)
        except requests.exceptions.ConnectionError:  # net not connected
            self.instruct = None
            self.log_instruct = 'NET_ERROR: Not Connected'
            return False

        if post and post.ok:
            post = post.text
        else:
            self.instruct = None
            self.log_instruct = 'NET_ERROR: Not Connected / Receiving empty HTML'
            return False

        res = search(r"<.+>(?P<instruct>\d+)<.+>", post)

        if not res:  # re not match
            self.instruct = None
            self.log_instruct = f"HTML text re-match failed: {post}"
            return False

        self.instruct = res.group('instruct')
        ctrl_code = int(self.instruct[self.machine_id - 1])

        if ctrl_code:
            self.log_instruct = f"Control code received: {self.instruct}[{self.machine_id - 1}]={ctrl_code}, request operation. "
            return ctrl_code
        else:
            self.log_instruct = f"Control code received: {self.instruct}[{self.machine_id - 1}]={ctrl_code}, do nothing. "
            return False

    def _kill_request(self, operation_code):
        if operation_code == 1:
            self._kill_proc('sunlogin')
            self.log_kill = f"VALID command: {operation_code}, kill sunlogin"

        elif operation_code == 2:
            self._kill_proc('starccm')
            self.log_kill = f"VALID command: {operation_code}, kill starccm"

        elif operation_code == 3:
            self._kill_proc('filezilla')
            self.log_kill = f"VALID command: {operation_code}, kill filezilla"

        elif operation_code == 4:
            self._restart_proc('sunlogin')
            self.log_kill = f"VALID command: {operation_code}, restart sunlogin"

        elif operation_code == 5:
            self._kill_proc('explorer')
            self.log_kill = f"VALID command: {operation_code}, kill explorer"

        else:
            self.log_kill = f"INVALID command: {operation_code}"

    def _reset_cd(self):
        self.status_cool_down = False
        self.timer_reset_cd = None

    def _log(self):
        def inner_write(log_dir):
            with open(log_dir, mode='a+') as f:
                time_hms = time.strftime('%H:%M:%S', time_curr)
                f.write(f"{time_hms}, "
                        f"{self.log_instruct}\n")

                if self.log_kill:
                    f.write(f"          {self.log_kill}\n")

        time_curr = time.localtime(time.time())
        try:
            log_dir = f"{self.log_folder}\\{time.strftime('%Y-%m-%d', time_curr)}.log"
            inner_write(log_dir)
        except:
            log_dir = f"C:\\{time.strftime('%Y-%m-%d', time_curr)}.log"
            inner_write(log_dir)

    def _exec(self):
        try:
            res = self._listen()

            if not res:  # no kill action
                self.log_kill = None

            elif self.status_cool_down:  # kill, but cd
                self.log_kill = f"kill request received. Cooling down..."

            else:  # kill, and enter cd
                self._kill_request(res)

                self.status_cool_down = True
                self.timer_reset_cd = Timer(self.interval_reset_cd, self._reset_cd)
                self.timer_reset_cd.start()

        except:
            pass
        # TODO: make log able to receive string arg

        finally:
            self._log()

    def exec(self):
        self.timer_request.start()


if __name__ == '__main__':
    client = RemoteCtrlClient(1, 'dfea')
    client.exec()
