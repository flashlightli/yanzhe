# -*- coding: utf-8 -*-
import sys
import test2
from test3 import Test


a = Test()
a.func_dic = {

}
print(sys.modules.get('test2'))
print(sys.modules.get('test2').handle)
a = getattr(sys.modules.get('test2'), 'handle')
print(a)
print(dir(sys.modules.get('test2')))