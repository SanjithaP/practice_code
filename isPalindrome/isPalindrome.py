def isPalindrome(self, x: int) -> bool:
        if len(str(x))==1:
            return True
        l=[]
        l1=[]
        for i in str(x):
            l.append(i)
        n=len(l)
        for j in range(n-1,0,-1):
            l1.append(l[j])
        for i in range(n-1):
            if l1[i]==l[i]:
                return True
            else:
                return False

num=121
res=isPalindrome(121)
print(res)