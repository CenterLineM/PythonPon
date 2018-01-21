def create_adder(x):
    def adder(y):
        return x + y
    return adder
add_10 = create_adder(10)
print (add_10(3) )# => 13

# 匿名函數
print((lambda x : x > 2)(3) )

# 高階函數
print (map(add_10, [1,2,3]))
filter(lambda x: x > 5, [3, 4, 5, 6, 7])

# 用列表推导式可以简化映射和过滤。列表推导式的返回值是另一个列表。

print([add_10(i) for i in [1, 2, 3]] )
[x for x in [3, 4, 5, 6,  7] if x >5]

