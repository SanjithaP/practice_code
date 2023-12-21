class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        mylist=[]
        points.sort(key=lambda x: x[0])
        for l in points:
            mylist.append(l[0])
        n=len(mylist)
        maxar=0
        for i in range(n-1):
            if i==(n-1):
                break
            ar=abs(mylist[i+1]-mylist[i])
            if ar>maxar:
                maxar=ar
        return maxar