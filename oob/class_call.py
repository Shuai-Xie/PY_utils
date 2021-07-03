class A:
    def __call__(self, *args, **kwargs):
        return sum(args)


a = A()
print(a(1, 2, 3))
