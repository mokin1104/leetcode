list_test = ['python', 'developer']
for i in list_test[:]:
    list_test.append(i.upper())
print(list_test)
# output：
# ['python', 'developer', 'PYTHON', 'DEVELOPER']
#
# Process finished with exit code 0
"""
list_test[:] 会创建一个浅拷贝
list_test[:] 相当于复制一份当前列表，得到一个新列表对象
例如：
list_test = ['python', 'developer']
copy = list_test[:]
print(copy is list_test)   # False，不是同一个对象
循环的时候，for遍历的就是新列表（拷贝）
即使你往原来的list_test不断append，拷贝内容不会变，所以循环是有限的

总结：
for i in list_test: → 遍历的是原列表，受动态修改影响 → 无限循环
for i in list_test[:]: → 遍历的是当时的拷贝，不受修改影响 → 能正常结束

[:] = 拍个“快照”，循环时只看这个快照
没有 [:] = 直接盯着原对象，变化了就跟着变
"""
