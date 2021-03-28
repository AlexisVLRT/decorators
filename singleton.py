from singleton_decorator import singleton


@singleton
class MyClass:
    pass


instance_1 = MyClass()
instance_2 = MyClass()

print(f"Is is {instance_1 is instance_2} that instance_1 is instance_2")
