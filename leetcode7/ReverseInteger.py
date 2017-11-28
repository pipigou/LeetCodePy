class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            sign = -1
        else:
            sign = 1
        strx = str(abs(x))
        r = strx[::-1]
        result = sign * int(r)
        if result > (2 ** 31 - 1) or result < -(2 ** 31):
            return 0
        else:
            return result
s =  Solution()
x = 3245678
x = s.reverse(x)
print(x)