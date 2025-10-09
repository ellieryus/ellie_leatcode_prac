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
            target = nums1[i]
            for j in range(len(nums2)):
                if nums2[j] == target:
                    for k in range(j+1, len(nums2)):
                        if target < nums2[k]:
                            output.append(nums2[k])
                            isfound = True
                            break
                    break
            if not isfound:
                output.append(-1)
        return output



        