class Solution:
    def titleToNumber(self, s: str) -> int:
        length=len(s)
        sum=0
        i=0
        while i<length:
            sum+=(ord(s[i])-64)*(26**(length-i-1))
            i+=1
        return sum
        