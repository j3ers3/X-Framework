#!/usr/bin/env python
# encoding:utf8

__version__ = "0.5"
__author__  = "kkk"
__prog__    = "OOOOO"

from core.mycolor import color
from core import header
from core import menu,help
from core import modules_database
import os
from modules import dirbb
from modules import baidu
from modules import sms
from modules import query
from modules import burp
from modules import nanfang
from modules import S2045

def main():

    try:
        line = color.blue + color.underl + color.bold + 'xsf' + color.end
        line += ' > '
        line += color.yellow

        terminal = raw_input(line)

        if terminal == 'banner':
            header.main_header()
            menu.main_info()
            main()

        elif terminal == 'exit':
            exit(0)

        elif terminal == 'help':
            help.help()
            main()

        elif terminal[0:1] == '!':
            os.system(terminal[1:])
            main()

        elif terminal[0:12] == 'show modules':
            modules_database.show_modules()
            main()
                
        elif terminal[0:3] == 'use':
            if terminal[4:20] == 'info/dir_scan':
                dirbb.dirscan()
                main()
            elif terminal[4:30] == 'info/baidu':
                baidu.search()
                main()
            elif terminal[4:15] == 'tools/12306':
                query.MyTools().query_12306()
                main()
            elif terminal[4:12] == 'tools/ip':
                query.MyTools().loc_ip()
                main()  
            elif terminal[4:11] == 'exp/sms':
                sms.sms_attack()
                main()
            elif terminal[4:30] == 'cms/nanfang_sqli_newstype':
                nanfang.sql_search()
                main()
            elif terminal[4:30] == 'exp/s2045':
                S2045.exp()
                main()
            elif terminal[4:12]  == 'burp/web':
                burp.burp()
                main()
            elif terminal[4:30] =='misc/msf':
                msf.gen()
                main()
            else:
                print("[-] Not modules")
                main()
            main()

        elif terminal == '':
            main()

        else:
            print("[-] Not Command found")
            main()
    except KeyboardInterrupt:
        print("[*]Tring to exit...")

def exploit():
    header.main_header()
    menu.main_info()
    main()

if __name__ == '__main__':
    exploit()