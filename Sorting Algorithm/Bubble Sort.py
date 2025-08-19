import random

# 随机生成一个长度为 10，范围在 -100 到 100 的整数列表
random_list = [random.randint(-100, 100) for _ in range(10)]

print("origin random list is: ", random_list)

for i in range(0, len(random_list) - 1):
    for j in range(0, len(random_list) - i - 1):
        if random_list[j] > random_list[j + 1]:
            random_list[j], random_list[j + 1] = random_list[j + 1], random_list[j]
print(random_list)

"""
冒泡排序的核心思想：通过不断比较相邻元素并交换，把较大的（或较小的）元素逐步“冒”到区间的一端

1.  外层：外层的取值范围：range(0, n-1)，根据左开右闭原则，能取到的值为：[0, n-2] 这里的0和n-2都是index，所以实际是比较了n-1次； 
    n个element，比较n-1次，可以完成对元素的排序；
2.  内层：内层的取值范围：range(0, n-i-1) ，这里的n-1是为了保证，最大只能够获取到index为n-2的element，这样在swap的时候，j+1最大为：n-1，不会越界；

冒泡🫧算法中，需要理解：range(0, len(random_list))为index
明白了这些为index，便可以彻底明白冒泡算法的核心

时间复杂度：
最好：O(n)（数组本身有序 + 早停优化）
最坏 / 平均：O(n²)
空间复杂度：O(1)（原地排序，in-place）
"""
