# -*- coding: utf-8 -*-

'''
用于解析出redirect_url中的协议
'''

class RedirectSplit(object):
    def __init__(self, redirect_url):
        self.redirect_url = redirect_url

    def redirect_split(self):
        sp1 = self.redirect_url.split('///')
        sp2 = sp1[1].split('?')
        return sp2[0]


