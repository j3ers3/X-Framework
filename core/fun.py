# encoding:utf
""" some function """

def save_fun(save_file, content):
    with open(save_file, 'a') as f:
        f.writelines(content + '\n')