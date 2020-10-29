# coding=utf-8

import os

def rename_batch(root_path:str, preffix:str, small_file_preffix:str, file_size_threshold_in_bytes:float, file_suffix_set:set, ignore_case:bool):
    files = os.listdir(root_path)

    lower_set = set()
    if ignore_case:
        for s in file_suffix_set:
            lower_set.add(s.lower())

    i = 1

    for old_file_name in files:
        old_full_path = os.path.join(root_path, old_file_name)

        if not os.path.isfile(old_full_path):
            continue

        file_suffix = os.path.splitext(old_file_name)[-1]

        if ignore_case:
            if file_suffix.lower() not in lower_set:
                continue
        elif file_suffix not in file_suffix:
            continue

        file_size_in_bytes = os.path.getsize(old_full_path)

        if file_size_in_bytes < file_size_threshold_in_bytes:
            new_file_name = '{}{}{}'.format(i, small_file_preffix, old_file_name)
            print('小图:{}'.format(new_file_name))
        else:
            new_file_name = '{}{}{}'.format(i, preffix, old_file_name)

        new_full_path = os.path.join(root_path, new_file_name)
        os.rename(old_full_path, new_full_path)

        i += 1
