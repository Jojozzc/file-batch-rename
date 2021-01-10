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

def rename_mode(config_parser):
    root_path = config_parser.get('CONFIG', 'target.path')

    prefix = config_parser.get('CONFIG', 'prefix.standard')
    small_file_prefix = config_parser.get('CONFIG', 'prefix.small')
    ignore_case = config_parser.getboolean('CONFIG', 'case.ignore', fallback=True)
    file_suffix_set = set(parse_list(config_parser.get('CONFIG', 'file.suffix.set')))
    file_size_threshold_in_bytes = config_parser.getfloat('CONFIG', 'file.threshold.bytes')
    start_index = config_parser.getint('CONFIG', 'index.start', fallback=1)
    print("root path:{}".format(root_path))
    print()
    rename_core.rename_batch(root_path=root_path,
                             prefix=prefix,
                             small_file_prefix=small_file_prefix,
                             file_size_threshold_in_bytes=file_size_threshold_in_bytes,
                             file_suffix_set=file_suffix_set,
                             ignore_case=ignore_case,
                             start_index=start_index)


def recall_mode(config_parser):
    root_path = config_parser.get('CONFIG', 'target.path')
    print("root path:{}".format(root_path))
    print()
    file_suffix_set = set(parse_list(config_parser.get('CONFIG', 'file.suffix.set')))
    ignore_case = config_parser.getboolean('CONFIG', 'case.ignore', fallback=True)
    prefix_remove_mark = config_parser.get('CONFIG', 'prefix.remove.mark')

    rename_core.recall(root_path=root_path, file_suffix_set=file_suffix_set, ignore_case=ignore_case, prefix_remove_mark=prefix_remove_mark)

if __name__ == "__main__":
    try:
        _curPath = os.path.abspath(os.path.dirname(__file__))
        _rootPath = os.path.split(_curPath)[0]
        sys.path.append(_rootPath)

        config_path = u"./config.ini"
        config_parser = configparser.ConfigParser()
        config_parser.read(config_path, encoding='utf-8')

        if len(sys.argv) <= 1:
            print('开始批量修改...')
            print('===========================================')
            rename_mode(config_parser)
            print('===========================================')
            print('批量修改成功')
        elif sys.argv[1] == '-z':
            print('撤回中...')
            print('===========================================')
            recall_mode(config_parser)
            print('===========================================')
            print('撤回成功')
        else:
            print('未知参数:{}'.format(sys.argv))
    except Exception as e:
        print('执行出错:', e)
    finally:
        os.system('pause')

