import re
import os
import shutil


path_root = r"S:\stage2"
# os.mkdir(dir_res := f"{path_root}\\res")
list_boundary = [f"{path_root}\\{i}" for i in os.listdir(path_root) if os.path.isdir(f"{path_root}\\{i}")]
# list_boundary.remove(f"{path_root}\\res")
# list_boundary.remove(f"{path_root}\\smallstep_Z1.3_pressure")

for i, boundary in enumerate(list_boundary):
    if boundary == 'res': continue
    list_res = list(filter(lambda x: re.match("TS|AVG.+\.csv", x), os.listdir(boundary)))
    # assert len(list(list_res)) == 2, f"WARNING: Boundary:{boundary} contains result csv more then 4."

    for _ in list_res:
        if os.path.isfile(f"{path_root}\\res\\{_}"):
            continue
        shutil.move(f"{boundary}\\{_}", f"{path_root}\\res\\")

    print(f"{i+1}/{len(list_boundary)}, {boundary} complete")
