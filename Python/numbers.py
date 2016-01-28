#!/usr/bin/python
# coding=utf-8

import platform
import os
import sys

import math

def _check_python_version():
    major_ver = sys.version_info[0]
    if major_ver != 3:
        # print "Your python version is %d.%d. \n"\
        #     "But python 3.x is required. \n"\
        #     "Download it here: https://www.python.org/" % (major_ver, sys.version_info[1])
        os.system("echo Sorry, please use python 3.x ")
        return False
    # print("platform.python_version:", platform.python_version(), type(platform.python_version()))
    # print("sys.version:", sys.version, type(sys.version))
    # print("sys.version_info:", sys.version_info, type(sys.version_info))
    # print("major_ver:", major_ver, type(major_ver))
    return True


def is_prime(n):
    if n == 2:
        return True
    if (n % 2 == 0) or (n == 1):
        return False
    k = (int)(math.sqrt(n)) + 1
    for i in range(3, k + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    total = 100
    print("prime number in range")
    for i in range(total):
        if is_prime(i):
            print(i)
    return

if __name__ == '__main__':
    if not _check_python_version():
        exit()
    try:
        main()
    except:
        print("exception catched!")
        traceback.print_exc()
    os.system("pause")
