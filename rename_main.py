# coding=utf-8

import os
import sys

import configparser
import rename_core


def parse_list(s: str):
    words = s.split(',')
    s_list = list()
    for w in words:
        w = w.strip()
        if w == '':
            continue
        s_list.append(w)
    return s_list


if __name__ == "__main__":
    _curPath = os.path.abspath(os.path.dirname(__file__))
    _rootPath = os.path.split(_curPath)[0]
    sys.path.append(_rootPath)

    config_path = u"./config.ini"
    config_parser = configparser.ConfigParser()
    config_parser.read(config_path)

    root_path = config_parser.get('CONFIG', 'target.path')

    preffix = config_parser.get('CONFIG', 'preffix.standard')
    small_file_preffix = config_parser.get('CONFIG', 'preffix.small')
    ignore_case = config_parser.getboolean('CONFIG', 'case.ignore')
    file_suffix_set = set(parse_list(config_parser.get('CONFIG', 'file.suffix.set')))
    file_size_threshold_in_bytes = config_parser.getfloat('CONFIG', 'file.threshold.bytes')
    print("root path:{}".format(root_path))
    rename_core.rename_batch(root_path=root_path, preffix=preffix, small_file_preffix=small_file_preffix, file_size_threshold_in_bytes=file_size_threshold_in_bytes, file_suffix_set=file_suffix_set, ignore_case=ignore_case)

