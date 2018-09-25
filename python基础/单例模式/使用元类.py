# _*_ coding:utf-8 _*_
'''
class Singleton中的__init__在Myclass声明的时候被执行Myclass=Singleton()
Myclass()执行时，最先执行父类的__call__方法（object,Singleton都作为Myclass的父类，
根据深度优先算法，会执行Singleton中的__call__()，Singleton中的__call__()写了单例模式）
"""
'''

class Singleton(type):

    def __init__(self, name, bases, dict):
        super(Singleton,self).__init__(name,bases, dict)
        self._instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super(Singleton,self).__call__(*args, **kwargs)
        return self._instance

class MyClass(object,metaclass=Singleton):
    a = 1

one=MyClass()
two=MyClass()
print(id(one))  # 1553247294800
print(id(two))  # 1553247294800
print(one == two)   # True
print(one is two)   # True