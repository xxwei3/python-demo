# 读写文件测试，包括log/txt/json/html/csv/excel/word等文件类型
import csv
import json
import os
import random
import xml.etree.cElementTree as ET


def check_path(file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'x', encoding='utf-8'):
            print(f'file path not exists, create new file ----> {file_path}')
            pass


def test_operate_log(file_path, file_type):
    check_path(file_path)
    with open(file_path, 'a+', encoding='utf-8') as fw:
        random_num = random.randint(1, 1000)
        fw.writelines(str(random_num))
        print(f'write {random_num} to {file_path}')
    with open(file_path, 'r') as fr:
        print(f'output {file_type} ....... {fr.readlines()}')


def test_operate_json2(file_path, file_type):
    check_path(file_path)
    dicts = {'a': True, 'b': 3.1415, 'c': "testing"}
    # 写入json文件
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(dicts, f)
        print(f'write {dicts} to {file_path}')
    # 读取json文件
    with open(file_path, 'r') as fr:
        print(f'output {file_type} ....... {json.load(fr)}')


def test_operate_csv(file_path, file_type):
    check_path(file_path)
    # 按行写入csv文件, 每个列表是一行
    content = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
               ["china", "china", "china", "china", "china", "china", "china", "china"],
               [3, 3.14, True, 'China']]
    # 写入操作：newline是指定新一行分隔符，不写newline会隔一行写一行
    with open(file_path, 'w', encoding='utf-8', newline="") as fw:
        csv.writer(fw).writerows(content)
    # 读取操作：
    with open(file_path, 'r', encoding='utf-8') as fr:
        print(f'output {file_type} .............')
        for line in csv.reader(fr):
            print(f'    ....... : {line}')


def test_operate_xml(file_path, file_type):
    check_path(file_path)
    # 写入操作：
    with open(file_path, 'w', encoding='utf-8') as fw:
        lines = '<project>\n' \
                '\t<modelVersion>4.0.0</modelVersion>\n' \
                '\t<packaging>pom</packaging>\n' \
                '</project>'
        fw.writelines(lines)
        pass
    # 读取操作：
    root = ET.parse(file_path).getroot()
    print(f'output {file_type} root ....... {root}')
    for parent_child in root:
        print(f'output {file_type} parent_child ....... parent-tag：{parent_child.tag}, parent-text：{parent_child.text}')


if __name__ == '__main__':
    base_path = 'D:\\My Test\\XXX\\'
    type_list = ['log', 'txt', 'json', 'csv', 'xml']
    test_operate_log(base_path + "test1.log", type_list[0])
    test_operate_log(base_path + "test2.txt", type_list[1])
    test_operate_json2(base_path + "test3.json", type_list[2])
    test_operate_csv(base_path + "test4.csv", type_list[3])
    test_operate_xml(base_path + "test5.xml", type_list[4])
