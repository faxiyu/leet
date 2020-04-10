class Solution:
    def reverseWords(self, s: str) -> str:
        str1=s.strip().split()#去除头尾空格并以空格分成数组
        return ' '.join(str1[::-1])#数组中字符串以空格连接