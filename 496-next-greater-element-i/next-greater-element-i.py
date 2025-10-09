class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        output = []

        for i in range(len(nums1)):
            isfound = False
            hasGreater = False
            for j in range(len(nums2)):
                if nums2[j] == nums1[i]:
                    isfound = True
                if isfound and nums1[i] < nums2[j]:
                    hasGreater = True
                    output.append(nums2[j])
                    break
            if not hasGreater:
                output.append(-1)
        return output



        