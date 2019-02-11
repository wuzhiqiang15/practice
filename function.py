#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

def f2(a,b,c=1,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

print(f1(5,6,7,8,9,'kkk',aa=98,bb=99))

print(f2(11,22,c=58,d=68,pp=33,op=78))

args=(1,2,3,4)
args1=(1,2,3)
kw={'d':99,'x':'#'}

print(f1(*args,**kw))
print(f2(*args1,**kw))