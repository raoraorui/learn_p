# _*_ coding:utf-8 _*_
def singleton(cls, *args, **kwargs):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton


@singleton
class MyClass3(object):
    a = 1


one = MyClass3()
two = MyClass3()
print(id(one))
print(id(two))
