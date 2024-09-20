# testsYTBDL.py
# --coding:utf-8--
# Time:2024-09-17 08:14:40
# Author:Luckykefu
# Email:3124568493@qq.com
# Description:
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

#####################################################
# TODO: Add tests for YTBDL

from src.download_from_youtube import download_from_youtube


if __name__ == "__main__":
    url = input("Enter the YouTube URL(s) separated by new line: ")
    proxy = "socks5://192.168.43.1:1088"
    
    # 调用下载函数
    download_from_youtube(url, proxy)

#####################################################
