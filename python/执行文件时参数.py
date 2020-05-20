#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
参数个数： len(sys.argv)
脚本名： sys.argv[0]
参数1：  sys.argv[1]
参数2：  sys.argv[2]
'''

import sys


def main():
    print('参数个数为:', len(sys.argv), '个参数。')
    print('参数列表:', str(sys.argv))
    print('脚本名为：', sys.argv[0])
    for i in range(1, len(sys.argv)):
        print('参数 %s 为：%s' % (i, sys.argv[i]))


if __name__ == "__main__":
    main()