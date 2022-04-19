# -*- coding: utf-8 -*-
"""
@Time       : 2022/04/19 12:25
@Author     : Spring
@FileName   : dir_file.py
@Description: 
"""
import os


def walk_file(file):
    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        # 遍历文件
        for f in files:
            print(os.path.abspath(f))

        # 遍历所有的文件夹
        for d in dirs:
            print(os.path.abspath(d))


if __name__ == '__main__':
    walk_file(os.curdir)
