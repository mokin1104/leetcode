import random

# 随机生成一个长度为 10，范围在 -100 到 100 的整数列表
random_list = [random.randint(-100, 100) for _ in range(10)]

print("the origin random list is: ", random_list)

number_of_list = len(random_list)
end_index = number_of_list - 1
while end_index > 0:
    last_swap_index = 0
    for j in range(end_index):
        if random_list[j] > random_list[j + 1]:
            random_list[j], random_list[j + 1] = random_list[j + 1], random_list[j]
            last_swap_index = j
    if last_swap_index == 0:
        break
    end_index = last_swap_index

"""
问题：
和ChatGPT的讨论：为什么说：end = last_swap 的作用是缩小下一趟的比较范围，避免对已经有序的尾部继续浪费时间
解析：
你抓到关键点了：外层确实在缩小范围（每趟少比较 1 次）
但 `last_swap` 的作用不是“再少一次”，而是按数据实际无序的最右边界，成块地一次性缩很多
这两者的“缩小方式”完全不同：

* 标准外层（`n-i-1`）：每趟不管数据如何，范围只减少 1
* `last_swap` 边界：每趟把下一轮的范围直接截到本趟“最后一次交换的位置”；
如果无序只在前面，下一趟的范围可能一下子就变得很小，甚至直接为 0，循环立刻结束

---

看个具体对比（差很多，不是“少一次”）

例子：[2, 1, 3, 4, 5, 6, 7, 8, 9, 10]（只有前两个乱了）

带早停但不记录 `last_swap` 的版本

  * 第 1 趟：做 9 次比较，只在 j=0 交换一次；趟末 `swapped=True` → 继续
  * 第 2 趟：做 8 次比较，发现无交换 → 退出
  * 总比较 = 17 次
记录 `last_swap` 的版本

  * 第 1 趟：做 9 次比较，最后一次交换发生在 j=0 → 设 `end = 0`
  * 下一趟 `end == 0`，直接退出
  * 总比较 = 9 次

> 结论：这不是只少 1 次，而是少了整整 8 次（近一半）。

为什么？因为“真正可能无序的区间”只到 `j=0`，`last_swap` 能一次性把后面整个有序尾部砍掉；而标准的 `n-i-1` 每趟只能机械地少 1

---

再换个场景（大段尾部已排好）

假设最后 90% 的元素早就有序，只有前面少量无序：
* 标准外层** 仍要从右边一路比到 `n-i-1`，每趟只少 1
* `last_swap`** 通常第一趟就把边界收缩到很靠前的位置，后续趟数和每趟比较次数都大幅减少

---

复杂度与“常数”的区别

* 最坏情况下两者仍是 O(n²)。
* 但在“几乎有序”的情况下，二者虽然都是 O(n)，`last_swap` 的常数明显更小（像上例节省近一半比较）

---

直观总结

* 外层 `n-i-1`：固定步长缩范围（每趟 -1），不看数据实际情况
* `last_swap`：自适应跳跃缩范围（一次减很多），直接对准“无序最右边界”
* 所以它的收益远不止“少比较一次”，在常见的“局部轻微无序”输入上，能省掉整整一趟甚至多趟的大量比较

"""
