import os
import pprint
import re


class RegroupFiles:
    def __init__(self, dir_root, star_suffix, id_small, id_big, file_type):

        if os.path.isdir(dir_root):
            pass
        else:
            raise OSError(f"ERROR: {dir_root} is not a directory.")

        self.dir_root = dir_root
        self.star_suffix = star_suffix
        self.id_small = id_small
        self.id_big = id_big
        self.length = id_big - id_small + 1

        self.file_type = file_type

        self.reg_pat = re.compile(f"(?P<filename>(?P<boundary>.+)_{star_suffix}_(?P<timestep>[\d]+).{file_type})")
        self.sub_dir_list = os.listdir(dir_root)
        self.log = f"{dir_root}\\log_regroup_files.txt"

        self.boundary_list = []

    def __move_files(self):
        for sub_dir in self.sub_dir_list:

            # select file only
            if not os.path.isfile(f"{self.dir_root}\\{sub_dir}"):
                continue

            # regex match
            reg_res = re.search(self.reg_pat, sub_dir)
            if not reg_res:
                with open(self.log, 'a') as f:
                    f.write(f"INFO: {sub_dir} doesn't match the regex expression.\n")
                continue

            boundary = reg_res.group('boundary')
            filename = reg_res.group('filename')

            if os.path.isdir(f"{self.dir_root}\\{boundary}"):
                pass
            else:
                os.mkdir(os.path.join(self.dir_root, boundary))
                self.boundary_list.append(boundary)

            os.rename(f"{self.dir_root}\\{filename}",
                      f"{self.dir_root}\\{boundary}\\{filename}")

    def __check_redundant_dir(self):
        for _ in filter(os.path.isdir, os.listdir(self.dir_root)):
            if _ in self.boundary_list:
                pass
            else:
                with open(self.log, 'a') as f:
                    f.write(f"INFO: {_} isn't a boundary.\n")

    def __check_timestep_id(self):
        for boundary in self.boundary_list:
            dir_curr = f"{self.dir_root}\\{boundary}"
            file_list = os.listdir(dir_curr)
            pat = re.compile(f"{boundary}_{self.star_suffix}_(?P<timestep>[\d]+).{self.file_type}")
            id_list = []

            for _ in file_list:
                res = re.search(pat, _)
                assert pat, f"{_} doesn't match regex expression::<__check_timestep_id>"
                id_list.append(int(res.group("timestep")))

            id_list.sort()

            if len(id_list) == self.length and id_list[0] == self.id_small and id_list[-1] == self.id_big:
                pass
            else:

                set_expected = set(range(self.id_small, self.id_big+1))
                set_curr = set(tuple(id_list))

                set_missing = set_expected - set_curr
                set_redundant = set_curr - set_expected

                with open(self.log, 'a') as f:
                    f.write(f"ERROR: {boundary} contains less timestep than expected: {len(id_list)}/{self.length}\n")

                    if set_missing:
                        f.write(f"    MISSING timestep of {boundary}:\n")
                        for _ in sorted(list(set_missing)):
                            f.write(f"        {boundary}::{_}\n")

                    if set_redundant:
                        f.write(f"    REDUNDANT timestep of {boundary}:\n")
                        for _ in sorted(list(set_redundant)):
                            f.write(f"        {boundary}::{_}\n")

    def main(self):
        self.__move_files()
        self.__check_redundant_dir()
        self.__check_timestep_id()


if __name__ == "__main__":
    RegroupFiles(r"S:\stage2",
                 "table",
                 3001,
                 6000,
                 'csv').main()
