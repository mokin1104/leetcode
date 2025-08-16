# shallow copy and deep copy
import copy

a = [[1, 2], [3, 4]]
b = a[:]
# 浅拷贝方法：
# 1. list.copy() - Python 3.3+ 的内置方法，等价于copy.copy(list)
# 2. list[:] - 切片，创建一个新列表，复制了所有引用，最古老、通用的浅拷贝技巧
# 3. copy.copy(list) - 需要 import copy，用于通用对象（不仅仅是 list），会调用对象的 __copy__ 方法
c = copy.deepcopy(a)    # 深拷贝

b[0][0] = 99   # 改变浅拷贝内部的 list
print(a)  # [[99, 2], [3, 4]] → 原始对象被影响
print(c)  # [[1, 2], [3, 4]] → 深拷贝完全独立

"""
浅拷贝 - list_test[:], list.copy()
只复制最外层的列表对象，但内部元素的引用保持不变
如果列表元素是不可变对象（比如 str, int），浅拷贝和深拷贝没有差别
如果元素是可变对象（比如 list、dict），拷贝后的两个列表共享这些内部对象
"""


"""
浅拷贝：
>>> list_1 = [1,2,[3,4],5]
>>> list_1_shallow_copy = list_1[:]
>>> list_1_shallow_copy
[1, 2, [3, 4], 5]
>>> list_2_shallow_copy = list_1[:]
>>> list_2_shallow_copy
[1, 2, [3, 4], 5]
>>> list_2_shallow_copy[2][1] = 7
>>> list_1_shallow_copy
[1, 2, [3, 7], 5]
>>> list_2_shallow_copy
[1, 2, [3, 7], 5]

>>> list_3_deep_copy = copy.deepcopy(list_1)
>>> list_3_deep_copy
[1, 2, [3, 7], 5]
>>> list_3_deep_copy[2][1] = 999
>>> list_3_deep_copy
[1, 2, [3, 999], 5]
>>> list_2_shallow_copy
[1, 2, [3, 7], 5]
>>> list_2_shallow_copy[2][1] = 88
>>> list_2_shallow_copy
[1, 2, [3, 88], 5]
>>> list_1_shallow_copy
[1, 2, [3, 88], 5]
"""
