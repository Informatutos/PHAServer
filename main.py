#coding:utf-8
import os


def openbrowser(url:str) :
    if not isinstance(url, str):
        raise TypeError("Invalide url")
    os.system("termux-open-url {}".format(url))
