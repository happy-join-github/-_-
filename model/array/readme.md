## 数组需要了解的内容

常见的数组操作和操作的时间复杂度(有助于了解整个程序的时间复杂度，防止写的程序超时，过不了测试)

访问数组的操作

```python
#读取索引为i的元素
#时间复杂度为O(1)
#数组的访问是随机的，通过索引值可以直接计算出元素的内存地址。
def value(nums,i):
    if 0<=i<=len(nums)-1:
        print(nums[i])
```

查找元素

```python
#读取目标元素value返回索引。
#时间复杂度为O(N)
def find_value(nums,value):
    for i in range(len(nums)):
        if nums[i]==value:
            return i
        return -1
```

插入元素

> 时间复杂度:在尾部插入O(1),在异于尾部插入O(N)
>
> 假设数组arr为arr=[1,4,5,2,3,6] 想在元素5前面插入一个元素0
>
> ![](https://github.com/happy-join-github/-_-/blob/main/model/array/images/inset.png)
> 需要将添加位置之后的元素都向后移动一位，所以时间复杂度为O(N)

矩阵的操作

