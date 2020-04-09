class Solution:
    def myAtoi(self, str: str) -> int:
        num=""
        count=0
        sum1=0
        if str=="":
            return 0
        for i in range(len(str)):
            try :
                if str[i]==" " :
                    if count==0 :
                        sum1+=1
                        continue
                    else :
                        break
                elif str[i]=="-" or str[i]=="+" :
                    if count==0 :
                        num=num+str[i]
                        count=1
                    else :
                        break
                elif 0<=int(str[i])<=9 :
                    num=num+str[i]
                    count=1
            except :
                if count==1 :
                    break
                else :
                    return 0
                    break
        if sum1==len(str) :
            return 0
        if num=="-" or num=="+" :
            return 0 
        num=int(num)
        if num>2**31-1:
            return 2**31-1
        elif num<-2**31 :
            return -2**31
        else :
            return num