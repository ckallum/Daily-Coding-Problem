"""

     Singleton pattern only allows one instance of an object, i.e. we can only retrieve the object
     through using the get_instance method, we set the constructor(inner class) to private so no other objects can
     be created outside of the class.

"""


class Singleton:
    instances = dict()
    even_instance = False

    class __Doubleton:
        def __init__(self, value):
            self.instance_num = value

    def __init__(self):
        pass

    @classmethod
    def __initialize(cls):
        cls.instances[0] = Singleton.__Doubleton(0)
        cls.instances[1] = Singleton.__Doubleton(1)

    @classmethod
    def get_instance(cls):
        if not cls.instances:
            cls.__initialize()

        cls.even_instance = not cls.even_instance
        return cls.instances[int(cls.even_instance)]


def main():
    i1 = Singleton.get_instance()
    assert i1.instance_num == 1
    i2 = Singleton.get_instance()
    assert i2.instance_num == 0
    i3 = Singleton.get_instance()
    assert i3.instance_num == 1
    i4 = Singleton.get_instance()
    assert i4.instance_num == 0
    i5 = Singleton.get_instance()
    assert i5.instance_num == 1


if __name__ == '__main__':
    main()
