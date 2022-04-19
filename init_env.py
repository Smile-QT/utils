# -*- coding: utf-8 -*-
"""
@Time       : 2022/04/19 10:24
@Author     : Spring
@FileName   : init_env.py
@Description: 
"""

import os


def init_pip(mirror_url="mirrors.aliyun.com"):
    """
    初始化pip.ini
    :param mirror_url:
    :return:
    """
    pip_ini = os.path.expanduser('~/pip/pip.ini')
    # 判断pip文件夹是否存在
    if not os.path.exists(pip_ini):
        os.makedirs(os.path.dirname(pip_ini), exist_ok=True)

    # 向pip.ini写入镜像配置
    with open(pip_ini, 'w') as f:
        f.write("[global]\n")
        f.write(f"index-url = https://{mirror_url}/pypi/simple/\n")
        f.write("[install]\n")
        f.write(f"trusted-host = {mirror_url}\n")
        print("pip.ini 初始化完成")


def init_condarc(mirror_url="mirrors.bfsu.edu.cn", set_env_dir=True):
    condarc = os.path.expanduser('~/.condarc')
    # 向condarc写入镜像配置
    with open(condarc, 'w') as f:
        if set_env_dir:
            f.write("envs_dirs:\n")
            f.write(f"  - D:\Program Files\Conda\envs\n")
            f.write("pkgs_dirs:\n")
            f.write(f"  - D:\Program Files\Conda\pkgs\n")
        f.write("channels:\n")
        f.write("  - defaults\n")
        f.write("show_channel_urls: true\n")
        f.write("default_channels:\n")
        f.write(f"  - https://{mirror_url}/anaconda/pkgs/main\n")
        f.write(f"  - https://{mirror_url}/anaconda/pkgs/r\n")
        f.write(f"  - https://{mirror_url}/anaconda/pkgs/msys2\n")
        f.write("custom_channels:\n")
        f.write(f"  conda-forge: https://{mirror_url}/anaconda/cloud\n")
        f.write(f"  msys2: https://{mirror_url}/anaconda/cloud\n")
        f.write(f"  bioconda: https://{mirror_url}/anaconda/cloud\n")
        f.write(f"  menpo: https://{mirror_url}/anaconda/cloud\n")
        f.write(f"  pytorch: https://{mirror_url}/anaconda/cloud\n")
        f.write(f"  pytorch-lts: https://{mirror_url}/anaconda/cloud\n")
        f.write(f"  simpleitk: https://{mirror_url}/anaconda/cloud\n")
        f.write(f"  paddle: https://{mirror_url}/anaconda/cloud\n")
        f.write("ssl_verify: true\n")
        print("condarc 初始化完成")


if __name__ == '__main__':
    init_pip()
    init_condarc()
