list_test = ['python', 'developer']
for i in list_test:
    list_test.append(i.upper())
print(list_test)

"""
关键点：迭代器并不会“快照”原列表，而是会按索引访问列表
所以，如果在循环中不断往list_test里追加元素，迭代器会继续访问新加的元素
"""


# Answer 1
list_test = ['python', 'developer']
result = list_test + [i.upper() for i in list_test]
print(result)
# ['python', 'developer', 'PYTHON', 'DEVELOPER']
"""
列表推导式 [i.upper() for i in list_test]
在Python里，列表推导式会先完整遍历list_test的当前内容，生成一个新列表
也就是说，它不会一边遍历一边往list_test加新东西

举例：
遍历开始时 list_test = ['python', 'developer']
推导式就只看这两个元素，生成 ['PYTHON', 'DEVELOPER']
最后再和 list_test 用 + 拼接
所以整个过程是有限的、静态的

for i in list_test: 
    list_test.append(...)
普通for循环，内部是用迭代器来遍历的
这个迭代器会按索引逐个访问列表，而不是提前拍个快照
所以当你在循环里append新元素时，这些新元素会继续被遍历到
结果：循环永远结束不了，出现“无限循环”
"""

# Answer 2
list_test = ['python', 'developer']
for i in list_test[:]:
    list_test.append(i.upper())

print(list_test)
# ['python', 'developer', 'PYTHON', 'DEVELOPER']

