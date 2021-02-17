def singleton(MyClass):
    instances = {}

    def getInstance(*args, **kwargs):
        if MyClass not in instances:
            instances[MyClass] = MyClass(*args, **kwargs)
        return instances[MyClass]

    return getInstance


@singleton
class MySingletonClass:
    pass


x = MySingletonClass()
print(x)
x.y = 10
print(x.y)
z = MySingletonClass()
print(z.y)
x.y = 0
print(z.y)

