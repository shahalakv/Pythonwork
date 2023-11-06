class bike:
    wheels=2
    @classmethod
    def get_count(cls):
        print(cls.wheels)
bike.get_count()