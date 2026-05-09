def add(a):
    def inner_b(b):
        def inner_c(c):
            return a + b + c
        return inner_c
    return inner_b

print(add(1)(2)(3))  # 6
print(add(10)(20)(30))  # 60
