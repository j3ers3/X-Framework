# encoding:utf8

from core.mycolor import color

def ksf_line(module, module_name):
    ksf_1 = color.blue + color.bold + color.underl + "XF" + color.end
    ksf_1 += ' ' 
    ksf_1 += color.blue + color.bold + module + '(' + color.end
    ksf_1 += color.red + color.bold + module_name + color.end
    ksf_1 += ') > '
    ksf_1 += color.yellow
    return ksf_1


tag_true = color.blue + color.bold + "[+]" + color.end
tag_false = color.blue + color.bold + "[x]" + color.end
tag_info = color.blue + color.bold + "[*]" + color.end
tag_vul = color.blue + color.bold + "[" + color.red + color.bold + "Vul" + color.blue + color.bold + "]" + color.end

def print_info(string):
    print color.bold + color.blue + string + color.end 

def print_err(string):
    print color.bold + color.red + string + color.end 

def show_op():
    print "" 
    print "Name\t\tCurrent Setting\t\t\tDescription" 
    print "-------\t\t---------------------\t\t-----------------" 

