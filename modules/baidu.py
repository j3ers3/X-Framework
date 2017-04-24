# encoding:utf8
import requests
import os
from core import help
from comm import *
from core.req import headers
from core.fun import save_fun
from urllib import quote
from bs4 import BeautifulSoup

options = ["inurl:index.action","10",""]
keyword = options[0]
pagenum = options[1]
savefile = options[2]

def search():

    global keyword
    global pagenum
    global savefile
    global threads
    
    ksf_1 = ksf_line("info","baidu")
    com = raw_input(ksf_1)

    try:
        if com[0:11] == 'set keyword':
            keyword = com[12:]
            print tag_true + "keyword => " + keyword
            search()

        elif com[0:11] == 'set pagenum': 
            pagenum = com[12:]
            print tag_true + "pagenum => " + pagenum
            search()

        elif com[0:12] == 'set savefile':
            savefile = com[13:]
            print tag_true + "savefile => " + savefile
            search()

       # elif com[0:11] == 'set threads':
       #     threads = com[12:]
       #     print tag_true + "threads => " + threads
        #    search()"""

        elif com[0:12] == 'show options':
            show_op()
            print "KEYWORD\t\t" + keyword + "\t\tThe search keyword"
            print "PAGENUM\t\t" + pagenum + "\t\tThe search page number"
            print "SAVEFILE\t\t" + savefile + "\t\tSave file"
          #  print "THREADS\t\t" + threads + "\t\tThe number of concurrent threads"
            search()

        elif com[0:1] == '!':
            os.system(com[1:])
            search()

        elif com[0:4] == 'help':
            help.help()
            search()

        elif com[0:4] == 'back':
            pass

        elif com[0:4] == 'exit':
            exit(0)

        elif com[0:3] == 'run' or com[0:7] == 'exploit':

            Headers = headers.Headers
            def parseBaidu(keyword, pagenum):
                baseurl = 'https://www.baidu.com/s?wd=' + str(quote(keyword)) + '&oq=' + str(quote(keyword)) + '&ie=utf-8' + '&pn='
                pn = 0
                while pn <= int(pagenum):
                    baseurl2 = baseurl + str(pn*10)
                    try:
                        r = requests.get(baseurl2, headers=Headers)
                        soup = BeautifulSoup(r.text, "html.parser")
                        for a in soup.select('div.c-container > h3 > a'):
                            url = requests.get(a['href'], headers=Headers).url
                            yield url
                    except:
                        yield None
                    finally:
                        pn += 1

            for u in parseBaidu(keyword,pagenum):
                if u:
                    print u
                    if savefile:
                        save_fun(savefile,u)
                else:
                    pass
            search()
        else:
            search()
    except KeyboardInterrupt:
        print_err("[*] Detected Ctrl-C ,System Exit...")