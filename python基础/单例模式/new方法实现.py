# _*_ coding:utf-8 _*_
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance


class MyClass(Singleton):
    a = 1


one = MyClass()
two = MyClass()
print(id(one))  #2170011747608
print(id(two))  #2170011747608
