# encoding:utf8

from core.mycolor import color

def show_modules():
    
    red_line = color.red + "------------------\t\t\t---------------" + color.end 
    print color.blue + "Information Modules\t\t\tDescription" + color.end      
    print red_line 
    print "info/dir_scan\t\t\t\tDirector Scan" 
    print "info/zoomeye\t\t\t\tZoomeye Search"
    print "info/baidu\t\t\t\tBaidu Search"
    print "info/google\t\t\t\tGoogle Search"
    print "info/shadow\t\t\t\tShadow Search"
    print "\n" 
    print color.blue + "CMS Modules\t\t\t\tDescription" + color.end 
    print red_line 
    print "cms/discuz\t\t\t\tDiscuz " 
    print "cms/nanfang_sqli_newstype\t\t良精南方 NewsType.asp SQLinject"
    print "cms/phpcms"
    print "cms/dede"
    print "exp/sms\t\t\t\t\tSMS attack" 
    print "\n" 
    print color.blue + "EXP Modules\t\t\t\tDescription" + color.end
    print red_line
    print "exp/s2045\t\t\t\tApache Struts Jakarta Multipart Parser OGNL Injection"
    print "\n"
    print color.blue + "Tools Modules\t\t\t\tDescription" + color.end 
    print red_line 
    print "tools/12306\t\t\t\t12306火车票查询" 
    print "tools/ip\t\t\t\tIP查询" 
    print "\n" 
    print color.blue + "Netword Modules\t\t\t\tDescription" + color.end 
    print red_line 
    print "\n" 
    print color.blue + "Password Modules\t\t\tDescription" + color.end 
    print red_line 
    print "burp/web\t\t\t\t对认证页面进行暴力破解" 
    print "\n" 
    print color.blue + "Misc Modules\t\t\t\tDescription" + color.end
    print red_line
    print "misc/webshell\t\t\t\twebshell"
    print "misc/msf\t\t\t\tmetasploit shell generate"
    print "\n"

    

