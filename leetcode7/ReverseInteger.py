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
        return sign * int(r)

r = Solution()
x = 1534236469
x = r.reverse(x)
print(x)