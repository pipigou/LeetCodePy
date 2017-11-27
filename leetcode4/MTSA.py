# -*-utf-8-*-
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
         :rtype: float
        """
        length = len(nums1) + len(nums2)
        list = []
        if length % 2 == 0:
            print(0)
        else:
            print(1)