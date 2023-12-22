# 此题简单的解释一下
# 题目会给两个数，一个数是马路的长度，第二个数是有几个区域的树需要移除 然后是区域的起始点。

# 这个题目考的是区间的合并。

# 输入格式
# 第一行 马路长度 和需要合并的区间数目
# 第一行后的n行   合并区间的起始点

# 源代码
# 思想先种在砍,有树为1没有树为0。
# 时间复杂度O(m*l)空间复杂度O(l)
initialization = input().split()  # 获取L和M
l = int(initialization[0])
m = int(initialization[1])
the_tree = [1 for i in range(l + 1)]  # 利用推导式初始化数组，有树为1
for i in range(m):  # 砍树开始，砍掉的点记为1
    num = input().split()
    start = int(num[0])  # 区间左端点
    end = int(num[1]) + 1  # 区间右端点
    for j in range(start, end):
        the_tree[j] = 0
tree_number = the_tree.count(1)  # 利用内置count函数记录剩余的树
print(tree_number)

# 时间复杂度比较小的算法 线段树算法。我不会所以写不出来。
