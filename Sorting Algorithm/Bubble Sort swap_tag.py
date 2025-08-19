import random

# 随机生成一个长度为 10，范围在 -100 到 100 的整数列表
random_list = [random.randint(-100, 100) for _ in range(10)]

print("the origin random list is: ", random_list)

for i in range(0, len(random_list) - 1):
    swap_tag = False
    for j in range(0, len(random_list) - i - 1):
        if random_list[j] > random_list[j + 1]:
            random_list[j], random_list[j + 1] = random_list[j + 1], random_list[j]
            swap_tag = True
    if not swap_tag:
        break
print("after sorting, the random_list is: ", random_list)

"""
外层循环的作用：
控制趟数：外层循环表示要进行多少趟“冒泡”
缩小范围：每一趟都会把一个最大（或最小）的元素放到正确位置，所以未排序的区间会逐步缩小

内层循环的作用：
在当前未排序范围内，逐对比较相邻元素
如果发现顺序不对，就交换，让较大元素往后“冒”，较小元素往前“沉”

一趟结束时，未排序区间的末尾就放好了一个最大值
👉 内层循环就是“在规定范围中，逐一比对元素”
👉 外层循环就是在“规定比较的范围”

我在这里引入了swap_tag
如果在一趟比较中，没有元素被swap，那么说明所有的元素都是有序的，直接break，提前结束Bubble sorting
"""
