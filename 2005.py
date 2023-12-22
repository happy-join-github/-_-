# 题目简单的介绍
#  一个人摘苹果。算一算能摘多少苹果。
#  基础条件:有一个30的凳子
#  附加条件:会给一个伸手能够到的最大高度

# 输入格式
# 两行 一行苹果距离地面的高度，另一行是手能够到的最大高度
# 输出格式
# 输出一个整数，表示摘到的苹果数目

# 源代码
def ableToapple(s:str,max_height:int)->int:
    lst=s.split()
    count=0
    for i in range(len(lst)):
        if max_height+30>=int(lst[i]):
            count+=1
    return count
s=input()
max_height=int(input())
print(ableToapple(s,max_height))

