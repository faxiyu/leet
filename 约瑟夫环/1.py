class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        # 直接循环删除
#         seq = [i for i in range(n)]
#         if len(seq) == 1:
#             return seq[0]
#         cur = 0
#         while( len(seq)!= 1):
#             cur = (cur + m -1)%len(seq)
#             del seq[cur]
        
#         return seq[0]
        
    
        # 递归法
        # Python 默认的递归深度不够，需要手动设置
#         sys.setrecursionlimit(100000)
#         def f(n, m):
#             if n == 0:
#                 return 0
#             x = f(n - 1, m)
#             return (m + x) % n

#         return f(n, m)
    
        # 迭代法，减少栈空间的使用
        # 前面的递归如果写成数学公式的话
        # n = 1 的时候f为0
        # n > 1 的时候f为 (f(n-1,m)+m)%n
        # 所以可以直接正向迭代
        f = 0
        for i in range(2,n+1):
            f = (f + m)%i
        
        
        return f

