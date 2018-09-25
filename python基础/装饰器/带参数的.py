# _*_ coding:utf-8 _*_
def pre_str(pre=''):
    # old decorator
    def decorator(F):
        def new_F(*args, **kwargs):
            print(pre + "input", *args, **kwargs)
            return F(*args, **kwargs)
        return new_F
    return decorator